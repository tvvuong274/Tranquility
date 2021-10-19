from django.db import models
from django.utils.translation import ugettext_lazy as _
import requests
import binascii
import os


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=_('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=_('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=_('Updated by'))

    class Meta:
        abstract = True
        # using = 'postgres_db'

    def get_required_fields(self):
        fields = self._meta.get_fields()
        required_fields = []

        # Required means `blank` is False
        for f in fields:
            # Note - if the field doesn't have a `blank` attribute it is probably
            # a ManyToOne relation (reverse foreign key), which you probably want to ignore.
            if hasattr(f, 'blank') and f.blank is False:
                required_fields.append(f)
        return required_fields

    def get_required_fields_as_names(self):
        str_required_field_names = []
        required_fields = self.get_required_fields()
        for required_field in required_fields:
            str_required_field_names.append(required_field.name)
        return str_required_field_names

    @staticmethod
    def generate_key(num):
        return binascii.hexlify(os.urandom(num)).decode()
