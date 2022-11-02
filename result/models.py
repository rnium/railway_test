from django.db import models

class Result(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    test_score = models.FloatField()
    merit_score = models.FloatField()
    position = models.IntegerField()
    college = models.CharField(max_length=100)
    selection = models.CharField(max_length=100)

    def __str__(self):
        return str(self.position)
