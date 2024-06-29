from django.contrib import admin
from .models import Articles

# Afficher nos artiches dans la page administrateur
admin.site.register(Articles)
