from django.db import models
from django_prose_editor.fields import ProseEditorField


class Track(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    title = models.TextField()
    image = models.ImageField(upload_to="speakers")

    def __str__(self) -> str:
        return self.name


class Talk(models.Model):
    track = models.ForeignKey(Track, on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = ProseEditorField(blank=True)
    date = models.DateTimeField()
    speakers = models.ManyToManyField(Speaker)

    class Meta:
        ordering = ["date"]

    def __str__(self) -> str:
        return self.name


class Visitor(models.Model):
    id = models.UUIDField(primary_key=True)

    def __str__(self) -> str:
        return self.id.hex


class Question(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self) -> str:
        return f'"{self.question}"'


class Rating(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

    class Meta:
        unique_together = ("talk", "visitor")

    def __str__(self) -> str:
        return f'{self.rating}/5: "{self.comment}"'