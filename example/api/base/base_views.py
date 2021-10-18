from api.base.api_view import CustomAPIView

from rest_framework import HTTP_HEADER_ENCODING


class BaseAPIView(CustomAPIView):
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        self.user = request.user


class BaseAPIAnonymousView(CustomAPIView):
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        # có bearer token trong header thì check token mới hoạt động
        if self.get_authorization_header(request).split():
            self.user = request.user

    @staticmethod
    def get_authorization_header(request):
        content = request.META.get('HTTP_AUTHORIZATION', b'')
        try:
            content = content.encode(HTTP_HEADER_ENCODING)
        except:
            content = b''
        return content
