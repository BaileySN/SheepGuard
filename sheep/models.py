from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
from customer.models import Customer
from SheepGuard.settings import START_ID

# Todo: CRUDS bei html files hinzufuegen.

def code_gen():
    try:
        lastid = Sheep.objects.latest('id')
        ids = int(lastid.pk) + int(1)
        return int(START_ID) + int(ids)
    except:
        return int(START_ID) + int(1)


class CHOICES(models.Model):
    STATE = (
        ('LEB', 'LEBENDIG'),
        ('VK', 'VERKAUFT'),
        ('TOD', 'TOD'),
        ('SHH', 'SCHLACHTHOF'),
    )
    SEX = (
        ('F', 'Weiblich'),
        ('M', 'Maennlich'),
    )


class Pasture(models.Model):
    pc_regex = RegexValidator(regex=r'^1?\d{4,5}', message="Postleitzahl 4 -5 Stellen")

    name = models.CharField(max_length=150, verbose_name=u'Platz Name')
    place = models.CharField(max_length=150, blank=True, verbose_name=u'Ort')
    postalcode = models.CharField(validators=[pc_regex],blank=True, max_length=5, verbose_name=u'Postleitzahl')
    comments = models.TextField(blank=True, verbose_name=u'Kommentar')

    def __unicode__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Farbe')

class Sheep(models.Model):
    code = models.IntegerField(unique=True, verbose_name=u'Fortlaufender Code', default=code_gen)
    name = models.CharField(max_length=150, blank=True, verbose_name=u'Name')
    birthdate = models.DateField(verbose_name=u'Geburtsdatum', blank=True)
    date_of_death = models.DateField(verbose_name=u'Sterbetag', blank=True)
    state = models.CharField(max_length=3, choices=CHOICES.STATE, default='LEB', verbose_name=u'Status')
    fk_color = models.ForeignKey(Color, verbose_name=u'Farbe')
    sex = models.CharField(max_length=1, choices=CHOICES.SEX, verbose_name=u'Geschlecht', default='M')

    fk_customer = models.ForeignKey(Customer, verbose_name=u'Abnehmer')

    fk_pasture_ground = models.ForeignKey(Pasture, blank=True, verbose_name=u'Weideplatz')
    comments = models.TextField(blank=True, verbose_name=u'Info')


    def __unicode__(self):
        return self.name


# # Datei von disk nach dem Loeschen von der DB auch loeschen
# # @receiver(post_delete, sender=SIM)
# # def image_post_delete_handler(sender, **kwargs):
# #     document = kwargs['instance']
# #     storage, path = document.document1.storage, document.document1.path
# #     storage.delete(path)
