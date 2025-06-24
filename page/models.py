import string
import random
from urllib.parse import urlparse, parse_qs
from django.db import models

def generate_unique_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not ShortURL.objects.filter(short_code=code).exists():
            return code

class ShortURL(models.Model):
    original_url = models.URLField("原始網址")
    short_code = models.CharField("短網址代碼", max_length=100, unique=True, default=generate_unique_code)
    description = models.CharField("備註說明", max_length=255, blank=True)
    is_protected = models.BooleanField("是否啟用密碼保護", default=False)
    password = models.CharField("密碼", max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # UTM 欄位
    utm_source = models.CharField("UTM 來源", max_length=100, blank=True)
    utm_medium = models.CharField("UTM 媒介", max_length=100, blank=True)
    utm_campaign = models.CharField("UTM 活動", max_length=100, blank=True)
    utm_term = models.CharField("UTM 關鍵字", max_length=100, blank=True)
    utm_content = models.CharField("UTM 內容", max_length=100, blank=True)

    def save(self, *args, **kwargs):
        # 自動解析 utm 參數
        parsed_url = urlparse(self.original_url)
        query_params = parse_qs(parsed_url.query)

        self.utm_source = query_params.get("utm_source", [""])[0]
        self.utm_medium = query_params.get("utm_medium", [""])[0]
        self.utm_campaign = query_params.get("utm_campaign", [""])[0]
        self.utm_term = query_params.get("utm_term", [""])[0]
        self.utm_content = query_params.get("utm_content", [""])[0]

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"