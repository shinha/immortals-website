from secrets import choice
from django.db import models

# Create your models here.
class Application(models.Model):
    c1 = [('friend', 'Friend'),('internet', 'Internet'),('performance', 'Performance'),('recruited', 'Recruited'),('other', 'Other'),]
    c2 = [('looks fun', 'Looks Fun'),('culture', 'Culture'),('physical activity', 'Physical Activity'),('something new', 'Something New'),('everything', 'Everything'),]
    c3 = [('head', 'Head'),('tail', 'Tail'),('martial arts', 'Martial Arts'),('music', 'Music'),('everything', 'Everything'),]
    c4 = [('somewhat', 'Somewhat'),('interested', 'Interested'),('very interested', 'Very Interested'),]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    how_did_you_hear = models.CharField(max_length=255, choices=c1)
    what_attracted_you = models.CharField(max_length=255, choices=c2)
    interest_in_lion_dance = models.CharField(max_length=255, choices=c3)
    level_of_interest = models.CharField(max_length=255, choices=c4)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'

class MemberEntry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    class_year = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'