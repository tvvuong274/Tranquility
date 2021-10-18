from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel


class Department(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    name = models.CharField(max_length=255, db_column='name')

    class Meta:
        db_table = 'tms_department'
        verbose_name_plural = _('Department')