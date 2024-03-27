from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveBigIntegerField(null=True)


    def __str__(self):
        return f'{self.title} from {self.year}' 