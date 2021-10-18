from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.data_source_api.models import DataSourceAPI
from db_models.models import BaseModel
from db_models.template.models import Template


class TemplateDataSourceAPI(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    data_source_api = models.ForeignKey(DataSourceAPI, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_template_data_source_api'
        verbose_name_plural = _('Template Data Source API')
