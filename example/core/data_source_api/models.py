from django.db import models
from django.utils.translation import ugettext_lazy as _
from db_models.models import BaseModel
from library.constant.output_api import OUTPUT_API_METHOD_TYPE_GET, OUTPUT_API_METHOD_TYPE_CHOICE, \
    OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN, OUTPUT_AUTHORIZATION_API_TYPE_CHOICE


class DataSourceAPI(BaseModel):
    id = models.AutoField(db_column='id', primary_key=True)

    name = models.CharField(max_length=255, db_column='name')

    c_method_type = models.IntegerField(db_column='c_method_type',
                                        default=OUTPUT_API_METHOD_TYPE_GET,
                                        choices=OUTPUT_API_METHOD_TYPE_CHOICE)

    url = models.CharField(max_length=1000, db_column='url')

    c_auth_type = models.IntegerField(db_column='c_auth_type',
                                      default=OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN,
                                      choices=OUTPUT_AUTHORIZATION_API_TYPE_CHOICE,
                                      null=True)

    auth_json = models.JSONField(db_column='auth_json', default=dict)
    header_list = models.JSONField(db_column='header_list', default=list)
    parameter_list = models.JSONField(db_column='parameter_list', default=dict)
    body_json = models.JSONField(db_column='body_json', default=dict)

    class Meta:
        db_table = 'tms_data_source_api'
        verbose_name_plural = _('Data Source API')
