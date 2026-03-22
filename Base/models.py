from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    number = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    
    # Case Study Fields
    slug = models.SlugField(unique=True, blank=True, null=True)
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    tech_used = models.TextField(blank=True, help_text="Comma separated list of technologies")
    challenges = models.TextField(blank=True)
    learnings = models.TextField(blank=True)

    def __str__(self):
        return self.title