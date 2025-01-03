from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'is_student', 'is_teacher', 'is_approved', 'is_staff')
    list_filter = ('is_student', 'is_teacher', 'is_approved')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_approved', 'is_student', 'is_teacher')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_student', 'is_teacher', 'is_approved')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


from .models import QuestionnaireResponse

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'age_group', 'education', 'profession', 'usage_frequency', 'overall_experience')
    search_fields = ('gender', 'age_group', 'profession')
    list_filter = ('gender', 'age_group', 'usage_frequency')
