from distutils.command.upload import upload
from statistics import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name="my_friends")

    def __str__(self) -> str:
        return self.name


class Friend(models.Model):
    profile= models.OneToOneField(Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name

class chat_mes(models.Model):
      message = models.TextField()
      msg_sender = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="msg_sender")
      msg_reciever = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="msg_reciever")
      seen = models.BooleanField(default=False)

      def  __str__(self) -> str:
        return self.message
