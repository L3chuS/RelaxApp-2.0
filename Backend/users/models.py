from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .validators import *


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
    
class Profiles(models.Model):
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    default_profile = models.BooleanField(default=False)
    visual_configuration = models.CharField(
        max_length=15,
        validators=[check_timer_settings],
        blank=True)
    stretch_configuration = models.CharField(
        max_length=15,
        validators=[check_timer_settings],
        blank=True)
    final_sounds_configuration = models.CharField(max_length=300, blank=True)
    lapse_sounds_configuration = models.CharField(max_length=300, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "profile_name"],
                name="unique_profile_name_per_user"
            )
        ]
    
    