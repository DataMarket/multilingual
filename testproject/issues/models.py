"""
Models and unit tests for issues reported in the tracker.

>>> from multilingual import set_default_language

# test for issue #15
# http://code.google.com/p/django-multilingual/issues/detail?id=15

>>> set_default_language('pl')
>>> g = Gallery.objects.create(id=2, title_pl='Test polski', title_en='English Test')
>>> g.title
'Test polski'
>>> g.title_en
'English Test'
>>> g = Gallery.objects.select_related(depth=1).get(id=2)
>>> g.title
'Test polski'
>>> g.title_en
'English Test'
"""

from django.db import models
import multilingual

class Gallery(models.Model):
    ref = models.ForeignKey('self', verbose_name=_('Parent gallery'),
                            blank=True, null=True)
    modified = models.DateField(_('Modified'), auto_now=True)

    class Translation(multilingual.Translation):
        title = models.CharField(_('Title'), maxlength=50)
        description = models.TextField(_('Description'), blank=True)
