from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    date_of_birth = models.IntegerField()
    age = models.IntegerField()
    defense =  models.IntegerField()
    midfield = models.IntegerField()
    attack = models.IntegerField()
    skill = models.IntegerField(default=0)
    potential = models.IntegerField(default=0)
    mentality = models.IntegerField(default=0)
    form = models.IntegerField(default=0)
    aggression = models.IntegerField(default=0)
    injured = models.BooleanField(default=False)
    condition = models.IntegerField(default=12)
    # stats
    games_ts = models.IntegerField(default=0)
    trained_ts = models.IntegerField(default=0)
    developed_ts = models.IntegerField(default=0)
    goals_ts = models.IntegerField(default=0)
    assists_ts = models.IntegerField(default=0)
    games_at = models.IntegerField(default=0)
    trained_at= models.IntegerField(default=0)
    developed_at= models.IntegerField(default=0)
    goals_at= models.IntegerField(default=0)
    assists_at = models.IntegerField(default=0)
    injured_at = models.IntegerField(default=0)


    def get_defence(self):
        return self.defense + self.power_modifiers()

    def get_midfield(self):
        return self.midfield + self.power_modifiers()

    def get_attack(self):
        return self.attack + self.power_modifiers()

    def power_modifiers(self):
        return self.form + self.skill
