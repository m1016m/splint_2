# accounts/forms.py 中創建自定義的用戶創建表單
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'is_student', 'is_teacher')


from .models import QuestionnaireResponse

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = '__all__'
        widgets = {
            'device_used': forms.CheckboxSelectMultiple,
            'suggestions': forms.Textarea(attrs={'rows': 3}),
        }