from django.db import models
class Data(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null = True)

    def __str__(self) -> str:
        return self.title