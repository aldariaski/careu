'''module for modeling the Post'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#User
class Profile(models.Model):
    '''class profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField()
    profile_picture_url = models.URLField(blank = True, default = "https://iupac.org/wp-content/uploads/2018/05/default-avatar-300x300.png")
    description = models.TextField(blank = True, default = "Hi! Ini profil kamu.")

#Post dan artikel
class Post(models.Model):
    '''class post'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        '''url absolut'''
        return reverse('journal-detail', kwargs={'pk':self.pk})
