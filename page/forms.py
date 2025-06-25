from django import forms
from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url', 'short_code', 'password', 'description', 'is_protected']

        widgets = {
            'original_url': forms.URLInput(attrs={
                'placeholder': '請輸入或貼上完整的網址'
            }),
            'short_code': forms.HiddenInput(),
            'password': forms.PasswordInput(),
            'description': forms.Textarea(attrs={
                'rows': 3
            }),
        }

        help_texts = {
            'original_url': '貼上的網址若包含 utm 標籤，會自動解析並支援 Google Analytics',
            'short_code': '可自行填寫，或是自動產生',
            'password': '若不使用密碼保護，將此欄位清空即可',
            'description': '備註說明',
        }

    def clean_short_code(self):
        short_code = self.cleaned_data.get('short_code')
        if not short_code:
            return None 
        if ShortURL.objects.filter(short_code=short_code).exists():
            raise forms.ValidationError("此短網址已被使用")
        return short_code

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        # 如果有輸入密碼，強制啟用密碼保護
        cleaned_data["is_protected"] = bool(password)
        return cleaned_data