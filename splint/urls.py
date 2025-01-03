"""
URL configuration for splint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#url('{% static "back1.jpg"%}')
from django.contrib import admin
from django.urls import path
from mainsite import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('register', views.register, name='Register'),
    path('content', views.content_on, name='Content'),
    path('exercise', views.exercise, name='Exercise'),
    path('login', views.login_view, name='login'),
    path('student_home', views.student_home, name='student_home'),
    path('teacher_home', views.teacher_home, name='teacher_home'),
    path('questionnaire', views.questionnaire_view, name='questionnaire'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
