from django.db import models
from django.utils.text import slugify
import datetime
from django.conf import settings
#created by
# Name : Asaf Louk .

class Messeages_H(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='',editable=False,max_length=200)
    user_sender = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, related_name='user_sender')
    user_receiver = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, related_name='user_receiver')
    message_content = models.TextField(max_length=500)
    creation_date = models.DateField( default=datetime.date.today)
    is_read = models.BooleanField(default=False)
    
    
    def __str__(self):
     return self.title
