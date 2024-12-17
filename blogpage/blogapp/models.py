from django.db import models

class AddPost(models.Model):
    head = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='uploads/', default='uploads/default.jpg')  
    
    def __str__(self):
        return self.head
