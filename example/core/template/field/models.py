
from db_models.template.data_source_api.models import TemplateDataSourceAPI
from db_models.template.field.group.models import TemplateFieldGroup
from library.constant.input_type import INPUT_TYPE_FORMAT_CHOICE, INPUT_TYPE_TEXT_FORMAT_NORMAL
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.metadata.models import Metadata
from db_models.models import BaseModel
from db_models.template.models import Template
from library.constant.template import TEMPLATE_FIELD_OFFSET_CHOICE, TEMPLATE_FIELD_OFFSET_COL_12


class TemplateField(BaseModel):
    id = models.BigAutoField(db_column='id', primary_key=True)

    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    key = models.CharField(max_length=100, db_column='key', blank=True, null=True)

    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE, null=True, default=None)

    ord = models.IntegerField(db_column='ord', null=True, default=None)

    label = models.CharField(max_length=255, db_column='label')

    input_type_format_id = models.IntegerField(db_column='input_type_format_id',
                                               default=INPUT_TYPE_TEXT_FORMAT_NORMAL,
                                               choices=INPUT_TYPE_FORMAT_CHOICE)

    input_condition_json = models.JSONField(db_column='input_condition_json', default=dict)

    require_flag = models.BooleanField(db_column='require_flag', default=True)

    output_flag = models.BooleanField(db_column='output_flag', default=True)

    output_edit_flag = models.BooleanField(db_column='output_edit_flag', default=True)

    template_data_source_api = models.ForeignKey(TemplateDataSourceAPI, on_delete=models.CASCADE,
                                                 null=True, default=None)

    output_result_key = models.CharField(db_column='output_result_key', max_length=100, null=True, default=None)

    row_index = models.IntegerField(db_column='row_index', null=True, default=None)

    c_offset = models.IntegerField(db_column='c_offset', default=TEMPLATE_FIELD_OFFSET_COL_12,
                                   choices=TEMPLATE_FIELD_OFFSET_CHOICE)

    default_data = models.CharField(db_column='default_data', max_length=500, blank=True, default='')

    template_field_group = models.ForeignKey(TemplateFieldGroup, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'tms_template_field'
        verbose_name_plural = _('Template Field')
