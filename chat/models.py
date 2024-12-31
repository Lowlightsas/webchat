from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=125, unique=True)
 
    def __str__(self):
        return self.group_name
    

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE,related_name='chat_messages')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='group_messages',null=True)  
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering = ['-created']