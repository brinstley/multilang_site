from django.db import models

# Creation de notre modele avec les champs title, content et publication date
class Articles(models.Model):
    title = models.CharField(max_length=50, blank= False, primary_key= True)
    content = models.CharField(max_length=10000, blank= False, default="Description")
    publication_date = models.DateField(auto_now= True)

    def __str__(self):
        return self.title # Afficher le titre pour chaque article
        
    class Meta:
        ordering = ['title'] # Classement se base sur le titre
        verbose_name_plural ="Articles" # Definition du pluriel
