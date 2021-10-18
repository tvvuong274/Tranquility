from django.db import models
from django.utils.translation import ugettext_lazy as _
import requests
import binascii
import os


class BaseModel(models.Model):

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
