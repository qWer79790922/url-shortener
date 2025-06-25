import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ShortURLForm
from .models import ShortURL, generate_unique_code
from django.contrib.auth.hashers import check_password
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# 建立短網址
@require_http_methods(['GET', 'POST'])
def create_short_url(request):
    short_url = None

    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data.get('short_code'):
                form.instance.short_code = generate_unique_code()
            short_url = form.save()
            form = ShortURLForm()
    else:
        form = ShortURLForm()

    return render(request, "page/create.html", {
        "form": form,
        "short_url": short_url
    })

# 短網址跳轉
@require_http_methods(["GET", "POST"])
def redirect_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)

    if short_url.is_protected:
        if request.method == 'POST':
            password = request.POST.get('password')
            if check_password(password, short_url.password):
                return redirect(short_url.original_url)
            else:
                return render(request, 'page/password_check.html', {
                    'error': '密碼錯誤，請重新輸入',
                    'short_url': short_url
                })
        return render(request, 'page/password_check.html', {'short_url': short_url})

    return redirect(short_url.original_url)

@require_GET
def fetch_page_info(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': '缺少 URL 參數'}, status=400)

    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else ''
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        description = desc_tag['content'].strip() if desc_tag and 'content' in desc_tag.attrs else ''

        return JsonResponse({'title': title, 'description': description})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)