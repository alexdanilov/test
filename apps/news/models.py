from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from tinymce import models as tinymce_models



class CatalogNews(models.Model):
    entity = models.CharField(max_length=64, db_index=True, verbose_name=_("entity"))
    id_entities = models.IntegerField(db_index=True, verbose_name=_("entity_id"))

    title = models.CharField(max_length=255, verbose_name=_("title"))
    description = models.CharField(max_length=255, verbose_name=_("description"))
    body = tinymce_models.HTMLField(verbose_name=_("body"))

    show_count = models.IntegerField(default=0, verbose_name=_('show_count'))
    comments_count = models.IntegerField(default=0, verbose_name=_('comments_count'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    visibility = models.BooleanField(default=True, db_index=True, verbose_name=_("visibility"))

    def __unicode__(self):
        return self.title

    @property
    def url(self):
        return '/news/%s' % self.id

    class Meta:
        ordering = ['-created']
        db_table = 'catalog_news'
        verbose_name = _("news")
        verbose_name_plural = _("news")


# Admin classes
class CatalogNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'entity', 'id_entities', 'created', 'visibility']
    list_filter = ['entity', 'visibility']
    search_fields = ['title']

admin.site.register(CatalogNews, CatalogNewsAdmin)