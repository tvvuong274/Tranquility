from db_models.template.field.models import TemplateField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel
from db_models.user.models import User


class TemplateFieldLog(BaseModel):
    id = models.BigAutoField(db_column='id', primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    template_field = models.ForeignKey(TemplateField, on_delete=models.CASCADE)

    content = models.CharField(db_column='content', max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'tms_template_field_log'
        verbose_name_plural = _('Template Field Log')
