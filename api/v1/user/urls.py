from django.urls import path

from api.v1.user.views import BranchView

urlpatterns = [
    # path('<str:user>/', BranchView.as_view({'get': 'info', 'put': 'update', 'delete': 'delete'})),

]
