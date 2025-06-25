from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ShortURLForm
from .models import ShortURL
from django.contrib.auth.hashers import check_password

# 建立短網址
@require_http_methods(['GET', 'POST'])
def create_short_url(request):
    short_url = None

    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
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