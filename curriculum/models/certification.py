from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from curriculum.models.utils import YEARS, MONTHS

from django.conf import settings

@python_2_unicode_compatible
class Certification(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    authority = models.CharField(max_length=200, verbose_name=_("authority"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))
   
    class Meta:
        app_label = 'curriculum'
        unique_together = ('title', 'authority')

    def __str__(self):
        return _('%(title)s at %(authority)s') % \
                {'title': self.title, 'authority': self.authority}


@python_2_unicode_compatible
class CertificationItem(models.Model):
    certification = models.ForeignKey("curriculum.Certification", related_name='items',on_delete=models.CASCADE)

    resume = models.ForeignKey("curriculum.Resume", related_name='certifications',on_delete=models.CASCADE,default=None)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='certifications',on_delete=models.CASCADE,default=None)

    end_year = models.IntegerField(choices=YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=MONTHS, null=True, blank=True, verbose_name=_("end month"))

    class Meta:
        app_label = 'curriculum'
        unique_together = ('certification', 'user')

    def __str__(self):
        return _('%(title)s at %(authority)s') % \
                {'title': self.certification.title, 'authority': self.certification.authority}
