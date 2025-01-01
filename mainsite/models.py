from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class QuestionnaireResponse(models.Model):
    gender = models.CharField(max_length=10, choices=[('male', '男'), ('female', '女'), ('prefer_not', '不願透露')])
    age_group = models.CharField(max_length=20, choices=[
        ('under_18', '18 歲以下'),
        ('18_25', '18-25 歲'),
        ('26_35', '26-35 歲'),
        ('36_45', '36-45 歲'),
        ('above_46', '46 歲以上')
    ])
    education = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    usage_frequency = models.CharField(max_length=50)
    device_used = models.TextField()
    overall_experience = models.IntegerField()
    suggestions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Response by {self.id}"
