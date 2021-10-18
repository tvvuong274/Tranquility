from db_models.template.data_source_api.models import TemplateDataSourceAPI
from db_models.template.models import Template
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel


class TemplateFieldGroup(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    name = models.CharField(max_length=100, db_column='name', blank=True, null=True)

    template_data_source_api = models.ForeignKey(TemplateDataSourceAPI, on_delete=models.CASCADE,
                                                 blank=True, null=True, default=None)

    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_template_field_group'
        verbose_name_plural = _('Template Field Group')
