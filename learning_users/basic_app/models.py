from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# this is a model for user to add some different parameter that the original don't have
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,
            on_delete = models.CASCADE,
    )

    #additional
    portfolio_site = models.URLField(blank = True)

    #whenever the user add the profile it will store in profile_pics folder which is inside media folder
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
