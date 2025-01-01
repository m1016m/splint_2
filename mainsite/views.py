# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# 首頁
#@login_required(login_url="Log")
def index(request):
    return render(request, "index.html", locals())

#副木呈現
def content_on(request):
    return render(request, 'content.html')

#註冊
# def register(request):
#     return render(request, 'register.html')

#手指運動
def exercise(request):
    return render(request, 'exercise.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
#註冊
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # 用戶註冊後需要管理員審核
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_approved:
                login(request, user)
                if user.is_student:
                    return redirect('student_home')
                elif user.is_teacher:
                    return redirect('teacher_home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Account not approved yet.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def student_home(request):
    return render(request, 'content.html')

@login_required
def teacher_home(request):
    return render(request, 'exercise.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import QuestionnaireForm

def questionnaire_view(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            response = form.save()
            # 發送郵件
            send_mail(
                subject="新的問卷提交",
                message=f"問卷結果：\n{response}",
                from_email="m1016m@gmail.com",
                recipient_list=["m1016m@gmail.com","rehand2024@gmail.com"],
                fail_silently=False,
            )
            return redirect('thank_you')
    else:
        form = QuestionnaireForm()
    return render(request, 'form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('/')
