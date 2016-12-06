from django.db import models
from AuthenticationApp.models import MyUser
class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
    	return self.comment

class SubComment(models.Model):
    parent_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
