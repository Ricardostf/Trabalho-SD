from django.db import models

class Sensors(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # define o que vai ser exibido
    def __str__(self):
        return self.name