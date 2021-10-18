from django.urls import path

from api.v2.user.views import UserView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view({'post': 'login'})),
    path('', UserView.as_view({'post': 'create', 'get': 'list'})),
    path('<int:user_id>/', UserView.as_view({'get': 'read', 'patch': 'update', 'delete': 'delete'})),
]
