from drf_spectacular.utils import extend_schema
from rest_framework import status
from api.base.serializers import ExceptionResponseSerializer
from api.v2.user.schemas import EXAMPLE_RESPONSE_LIST_USERS_SUCCESS, EXAMPLE_RESPONSE_LOGIN_SUCCESS1, EXAMPLE_RESPONSE_LOGIN_SUCCESS2, \
    EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_LOGIN, EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_USERNAME, \
    EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_PASSWORD
from api.v2.user.serializers import UserListSuccessResponeSerializer, UserLoginSuccessResponseSerializer, UserCreateSuccessResponseSerializer, \
    UserCreateRequestSerializer, UserDetailSuccessResponseSerializer, UserUpdateRequestSerializer
from db_models.user.models import User

from api.base.base_views import BaseAPIView
from api.base.authentication import BasicAuthentication


class UserView(BaseAPIView):
    @extend_schema(
        operation_id='user-register',
        summary='Register',
        tags=["User"],
        description='Register new user',
        request=UserCreateRequestSerializer,
        responses={
            status.HTTP_201_CREATED: UserCreateSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def create(self, request):
        serializer = UserCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        username = serializer.validated_data['username'].lower()
        password = serializer.validated_data['password']

        if User.objects.filter(username=username).exists():
            return self.http_exception(description='username is exist')

        user = User.objects.create(
            name=name,
            username=username
        )
        user.set_password(password)
        user.save()

        return self.response_success({
            'user_id': user.id,
            'name': user.name
        }, status_code=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id='user-detail',
        summary='Detail',
        tags=["User"],
        description='Detail an user',
        responses={
            status.HTTP_200_OK: UserDetailSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def read(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as ex:
            return self.http_exception(description=str(ex))

        return self.response_success({
            'id': user.id,
            'name': user.name,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        })

    @extend_schema(
        operation_id='user-update',
        summary='Update',
        tags=["User"],
        description='Update an user',
        request=UserUpdateRequestSerializer,
        responses={
            status.HTTP_200_OK: UserDetailSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def update(self, request, user_id):
        serializer = UserUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as ex:
            return self.http_exception(description=str(ex))

        user.name = name
        user.save()

        return self.response_success({
            'id': user.id,
            'name': user.name,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        })

    @extend_schema(
        operation_id='user-delete',
        summary='Delete',
        tags=["User"],
        description='Delete an user',
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as ex:
            return self.http_exception(description=str(ex))

        user.delete()

        return self.response_success(None, status_code=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        operation_id="list-all-users",
        summary="List",
        tags=["User"],
        description="List all users in system",
        responses={
            status.HTTP_200_OK: UserListSuccessResponeSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_LIST_USERS_SUCCESS],
    )
    def list(self, request):
        """
        [API] Get all users in system
        """
        users = User.objects.all().values("name", "username", "id")
        response = UserListSuccessResponeSerializer(users, many=True)

        return self.response_success(
            response.data,
            status_code=status.HTTP_204_NO_CONTENT,
        )


# Login hông dùng Bearer token mà dùng Basic authentication (truyền username, password)
# nên sửa riêng authentication_classes
class LoginView(BaseAPIView):
    # setting user/password authentication.
    authentication_classes = (BasicAuthentication,)

    @extend_schema(
        operation_id='user-login',
        summary='Login',
        tags=["User"],
        description='Login to get Bearer token to use in others API',
        responses={
            status.HTTP_200_OK: UserLoginSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LOGIN_SUCCESS1,
            EXAMPLE_RESPONSE_LOGIN_SUCCESS2,
            EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_LOGIN,
            EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_USERNAME,
            EXAMPLE_RESPONSE_LOGIN_FAIL_INVALID_PASSWORD
        ]
    )
    def login(self, request):
        user = self.user

        return self.response_success({
            'user_id': user.id,
            'name': user.name,
            'token': user.get_token(),
        })
