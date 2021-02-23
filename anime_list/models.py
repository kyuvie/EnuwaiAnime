from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f'Anime(title={self.title}, url={self.url})'
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    anime = models.ManyToManyField('anime_list.Anime')
    name = models.CharField(max_length=100)
    
    def __repr__(self):
        return f'Tage(anime={self.anime}, name={self.name})'
    
    def __str__(self):
        return self.name
