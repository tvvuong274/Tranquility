from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel


class TemplateGroup(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    code = models.CharField(max_length=255, db_column='code')

    name = models.CharField(max_length=255, db_column='name')

    slug = models.CharField(max_length=255, db_column='slug')

    active_flag = models.BooleanField(db_column='active_flag', default=True)

    parent = models.ForeignKey('self',  db_column='parent_id', on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'tms_template_group'
        verbose_name_plural = _('Template Group')
