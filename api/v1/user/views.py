import uuid

from django.db.models import F, Value, CharField, Case, When, Exists, BooleanField, OuterRef, Q
from django.db.models.functions import Concat
from django.utils.timezone import now

from drf_spectacular.utils import extend_schema
from rest_framework import status
from api.base.serializers import ExceptionResponseSerializer


from api.base.base_views import BaseAPIAnonymousView


class BranchView(BaseAPIAnonymousView):
    pass