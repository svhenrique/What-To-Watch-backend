from tabnanny import verbose
from embed_video.fields import EmbedVideoField
from core.utils import get_file_path
from django.db import models
from pydoc import describe

CHOICES_RATTING = [
    (0, "L"),
    (10, "10"),
    (12, "12"),
    (14, "14"),
    (16, "16"),
    (18, "18"),
]

class Base(models.Model):

    created_at = models.DateField('Criação', auto_now_add=True)
    updated_at = models.DateField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class WatchableContent(Base):
    title = models.TextField(verbose_name="Título")
    description = models.TextField(verbose_name='Descrição')
    ratting_age = models.IntegerField(choices=CHOICES_RATTING)
    poster = models.ImageField(verbose_name='Poster', upload_to=get_file_path, max_length=50)
    genres = models.TextField(verbose_name="Gêneros")
    release_date = models.DateField(verbose_name="Data de Lançamento", null=True, blank=True)
    daily_views = models.PositiveIntegerField(verbose_name="Vizualizações Diária", default=0)
    week_views = models.PositiveIntegerField(verbose_name="Vizualizações Semanal",default=0)
    year_views = models.PositiveIntegerField(verbose_name="Vizualizações Anual", default=0)

    def __str__(self):
        return self.title

class Episode(Base):
    name = models.TextField(verbose_name="Nome")
    episode = models.PositiveIntegerField(verbose_name="Vizualizações Diária", default=0)
    content = models.ForeignKey(verbose_name="Conteúdo", to=WatchableContent, on_delete=models.CASCADE, related_name="episodes")
    description = models.TextField(verbose_name="Descrição")
    season = models.PositiveIntegerField(verbose_name="Temporada")
    video = EmbedVideoField()

    def __str__(self):
        return self.name

class HighlightedArea(Base):
    contents = models.ManyToManyField(verbose_name="Conteúdo", to=WatchableContent)
    title = models.TextField(verbose_name="Título")
    genres = models.TextField(verbose_name="Gêneros")
    position = models.PositiveIntegerField(verbose_name="Posição")
