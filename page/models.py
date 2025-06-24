import string
import random
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

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"