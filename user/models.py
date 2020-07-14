from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

Sex_choice = (
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Giới tính thứ ba', 'Giới tính thứ ba'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profiles_pic', blank=True, null=True, default='static/user/default_pro.jpg')
    gender = models.CharField(choices=Sex_choice, blank=True, max_length=20, null=True, default='Nam')
    time_join = models.DateTimeField(default=timezone.datetime.now(), blank=True, null=True)
    ctv = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
