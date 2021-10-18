from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.metadata.group.models import MetadataGroup
from db_models.models import BaseModel

from library.constant.input_type import INPUT_TYPE_FORMAT_CHOICE, INPUT_TYPE_TEXT_FORMAT_NORMAL


class Metadata(BaseModel):
    id = models.BigAutoField(db_column='id', primary_key=True)

    metadata_group = models.ForeignKey(MetadataGroup, on_delete=models.CASCADE)

    code = models.CharField(max_length=100, db_column='code')

    name = models.CharField(max_length=255, db_column='name')

    list_c_system_type = models.JSONField(db_column='list_c_system_type', default=list)

    active_flag = models.BooleanField(db_column='active_flag', default=True)

    note = models.CharField(max_length=255, db_column='note', blank=True, null=True)

    output_edit_flag = models.BooleanField(db_column='output_edit_flag', default=False)

    input_type_format_id = models.IntegerField(db_column='input_type_format_id',
                                               default=INPUT_TYPE_TEXT_FORMAT_NORMAL,
                                               choices=INPUT_TYPE_FORMAT_CHOICE)

    input_condition_json = models.JSONField(db_column='input_condition_json', default=dict)

    class Meta:
        db_table = 'tms_metadata'
        verbose_name_plural = _('Metadata')
