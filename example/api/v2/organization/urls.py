from django.urls import path
from api.v2.organization.views import OrganizationView

urlpatterns = [
    path('blocks/', OrganizationView.as_view({"get": "list_block"})),
    path('departments/', OrganizationView.as_view({"get": "list_department"})),
]
