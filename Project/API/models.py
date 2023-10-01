from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=1000)
    is_check = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):        
        return f"{self.user} need todo {self.todo}"
    
