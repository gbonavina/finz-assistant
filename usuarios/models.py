from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(default=timezone.now)
    last_active = models.DateTimeField(default=timezone.now)  # novo campo

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        self.last_active = timezone.now()  # atualiza o campo last_active
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username