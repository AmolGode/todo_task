from django.db import models
from user_api.models import User
# Create your models here.


class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=200)
    created_date_time = models.DateTimeField(auto_now_add=True)
    completed_date_time = models.DateTimeField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)