from db_models.template.group.models import TemplateGroup
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel


class TemplateFolder(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    name = models.CharField(max_length=255, db_column='name')

    slug = models.CharField(max_length=255, db_column='slug')

    parent = models.ForeignKey('self', db_column='parent_id', on_delete=models.CASCADE, null=True, default=None)

    template_group = models.ForeignKey(TemplateGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_template_folder'
        verbose_name_plural = _('Template Folder')
