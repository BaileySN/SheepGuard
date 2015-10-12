from django.db import models
from django.core.validators import RegexValidator


class Title(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Anrede')
    change_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Update')

    def __unicode__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Name')
    change_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Update')

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    phone_regex = RegexValidator(regex=r'^1?\d{8,15}', message="Telefonnummer muss in diesem Format: '06606020111' eingegeben werden und kann bis zu 15 Stellen lang sein.")
    pc_regex = RegexValidator(regex=r'^1?\d{4,5}', message="Postleitzahl 4 -5 Stellen")

    fk_title = models.ForeignKey(Title, verbose_name=u'Anrede')
    fname = models.CharField(max_length=150, blank=True, verbose_name=u'Vorname')
    lname = models.CharField(max_length=150, verbose_name=u'Nachname')
    phone = models.CharField(validators=[phone_regex], max_length=15, verbose_name=u'Telefonnnummer', blank=True)
    phone2 = models.CharField(validators=[phone_regex], max_length=15, verbose_name=u'Telefonnummer 2', blank=True)
    fax = models.CharField(validators=[phone_regex], max_length=15, verbose_name=u'Fax', blank=True)
    email = models.EmailField(verbose_name=u'E-Mail', blank=True)
    email2 = models.EmailField(verbose_name=u'E-Mail 2', blank=True)

    postalcode = models.CharField(validators=[pc_regex],blank=True, max_length=5, verbose_name=u'Postleitzahl')
    street = models.CharField(max_length=150, blank=True, verbose_name=u'Strasse')
    place = models.CharField(max_length=150, blank=True, verbose_name=u'Ort')

    fk_profession = models.ForeignKey(Profession, verbose_name=u'Beziehung', default="0")

    comments = models.TextField(blank=True, verbose_name=u'Kommentar')
    change_time = models.DateTimeField(auto_now_add=True, editable=False)


    def __unicode__(self):
        return self.lname
