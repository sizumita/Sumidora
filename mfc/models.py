from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models



class MfcBet(models.Model):
    fight_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()
    name = models.CharField(max_length=40)
    uuid = models.CharField(max_length=40)
    bet = models.FloatField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    fighter_uuid = models.CharField(max_length=40)
    fighter_name = models.CharField(max_length=40)
    odds = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    profit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfc_bet'

    def __str__(self):
        return self.name




class MfcFight(models.Model):
    datetime = models.DateTimeField()
    kit = models.CharField(max_length=40)
    stage = models.CharField(max_length=40)
    uuid1 = models.CharField(max_length=40)
    uuid2 = models.CharField(max_length=40)
    player1 = models.CharField(max_length=40)
    player2 = models.CharField(max_length=40)
    odds1 = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    odds2 = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    bet1 = models.IntegerField(blank=True, null=True)
    bet2 = models.IntegerField(blank=True, null=True)
    totalbet = models.FloatField(blank=True, null=True)
    prize = models.FloatField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=40, blank=True, null=True)
    loser = models.CharField(max_length=40, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfc_fight'

    def __str__(self):
        return self.player2


class MfcproBet(models.Model):
    fight_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()
    name = models.CharField(max_length=40)
    uuid = models.CharField(max_length=40)
    bet = models.FloatField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    fighter_uuid = models.CharField(max_length=40)
    fighter_name = models.CharField(max_length=40)
    odds = models.DecimalField(blank=True, null=True,max_digits=100, decimal_places=2)
    profit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfcpro_bet'


    def __str__(self):
        return self.name


    def __float__(self):
        return self.profit




class MfcproFight(models.Model):
    datetime = models.DateTimeField()
    kit = models.CharField(max_length=40)
    stage = models.CharField(max_length=40)
    uuid1 = models.CharField(max_length=40)
    uuid2 = models.CharField(max_length=40)
    player1 = models.CharField(max_length=40)
    player2 = models.CharField(max_length=40)
    odds1 = models.DecimalField(blank=True, null=True,max_digits=100, decimal_places=2)
    odds2 = models.DecimalField(blank=True, null=True,max_digits=100, decimal_places=2)
    bet1 = models.IntegerField(blank=True, null=True)
    bet2 = models.IntegerField(blank=True, null=True)
    totalbet = models.FloatField(blank=True, null=True)
    prize = models.FloatField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=40, blank=True, null=True)
    loser = models.CharField(max_length=40, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfcpro_fight'

    def __str__(self):
        return self.player1