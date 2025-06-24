from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ShortURLForm
from .models import ShortURL

# 建立短網址
@require_http_methods(['GET', 'POST'])
def create_short_url(request):
    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short_url = form.save()
            return render(request, "page/create_success.html", {"short_url": short_url})
    else:
        form = ShortURLForm()
    return render(request, "page/create.html", {"form": form})

# 短網址跳轉
@require_http_methods(['GET'])
def redirect_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)