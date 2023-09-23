from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name