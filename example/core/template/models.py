from db_models.organization.department.models import Department
from db_models.organization.block.models import Block
from db_models.template.folder.models import TemplateFolder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from db_models.models import BaseModel

from library.constant.template import TEMPLATE_STATUS_TYPE_USED, TEMPLATE_STATUS_TYPE_CHOICE, TEMPLATE_TYPE_GENERAL, \
    TEMPLATE_TYPE_CHOICE


class Template(BaseModel):
    id = models.BigAutoField(db_column='id', primary_key=True)

    c_status = models.IntegerField(db_column='c_status', default=TEMPLATE_STATUS_TYPE_USED,
                                   choices=TEMPLATE_STATUS_TYPE_CHOICE)

    parent = models.ForeignKey('self', db_column='parent_id', on_delete=models.CASCADE, null=True, default=None)

    version = models.FloatField(db_column='version')

    list_child_version_id = models.JSONField(db_column='list_child_version_id', default=list)

    identify_number = models.CharField(db_column='identify_number', max_length=100)

    name = models.CharField(db_column='name', max_length=255)

    code = models.CharField(db_column='code', max_length=100)

    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    c_type = models.IntegerField(db_column='c_type', default=TEMPLATE_TYPE_GENERAL,
                                 choices=TEMPLATE_TYPE_CHOICE)

    khcn_flag = models.BooleanField(db_column='khcn_flag', default=False)

    khdn_flag = models.BooleanField(db_column='khdn_flag', default=False)

    dntn_flag = models.BooleanField(db_column='dntn_flag', default=False)

    scb_flag = models.BooleanField(db_column='scb_flag', default=False)

    start_date = models.DateTimeField(db_column='start_date')

    end_date = models.DateTimeField(db_column='end_date')

    template_api = models.CharField(max_length=500, db_column='template_api')

    list_c_system_type = models.JSONField(db_column='list_c_system_type', default=list)

    file_uuid = models.CharField(max_length=32, db_column='file_uuid')

    file_name = models.CharField(max_length=500, db_column='file_name')

    preview_file_uuid = models.CharField(max_length=32, db_column='preview_file_uuid')

    template_folder = models.ForeignKey(TemplateFolder, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_template'
        verbose_name_plural = _('Template')
