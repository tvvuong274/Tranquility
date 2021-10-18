from db_models.metadata.models import Metadata
from db_models.user.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel


class MetadataComment(BaseModel):
    id = models.BigAutoField(db_column='id', primary_key=True)

    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    log_flag = models.BooleanField(db_column='log_flag', default=True)

    content = models.CharField(max_length=500, db_column='content', blank=True, null=True)

    class Meta:
        db_table = 'tms_metadata_comment'
        verbose_name_plural = _('Metadata Comment')
