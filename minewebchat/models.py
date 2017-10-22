from django.db import models

# Create your models here.
class PdaChatLog(models.Model):
    name = models.CharField(max_length=50)
    uuid = models.CharField(max_length=50)
    chat = models.CharField(max_length=1024)
    world = models.CharField(max_length=128)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    date_time = models.DateTimeField(blank=True, null=True)
    time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pda_chat_log'