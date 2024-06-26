from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50, blank= False, primary_key= True)
    content = models.CharField(max_length=10000, blank= False, default="Description")
    publication_date = models.DateField(auto_now= True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
        verbose_name_plural ="Articles"
