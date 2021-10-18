import json
from api.v2.test_data import TEMPLATE_GROUP_CREATE_DATA, TEMPLATE_GROUP_UPDATE_DATA
from db_models.template.models import Template
from django.urls import reverse
from api.v2.base_test import BaseAPITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from api.v2.template.urls import urlpatterns


class TemplateGroupAPITestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.url_template_group_create_list = reverse("template_group_create_list")
        self.url_template_group_list_menu = reverse("template_group_list_menu")
        self.url_template_group_detail_update_delete = reverse("template_group_detail_update_delete", args=[1])

    def _api_template_group_detail(self):
        response = self.client.get(self.url_template_group_detail_update_delete, content_type="application/json")
        return response

    def _api_template_group_create(self):
        response = self.client.post(self.url_template_group_create_list, data=json.dumps(TEMPLATE_GROUP_CREATE_DATA), content_type="application/json")
        return response

    def test_url_template_group_create(self):
        response = self._api_template_group_create()
        self.assertEqual(response.status_code, HTTP_201_CREATED, msg=response.data)

    def test_url_template_group_update(self):
        template_group = self._api_template_group_create()

        before_response = self._api_template_group_detail()
        response = self.client.put(self.url_template_group_detail_update_delete, data=json.dumps(TEMPLATE_GROUP_UPDATE_DATA), content_type="application/json")
        after_response = self._api_template_group_detail()

        self.assertEqual(response.status_code, HTTP_200_OK, msg=response.data)
        self.assertNotEqual(before_response.data, after_response.data, msg= "Data is not updated")

    def test_url_template_group_detail(self):
        template_group = self._api_template_group_create()
        response = self._api_template_group_detail()
        self.assertEqual(response.status_code, HTTP_200_OK, msg=response.data)

    def test_url_template_group_delete(self):
        template_group = self._api_template_group_create()
        response = self.client.get(self.url_template_group_detail_update_delete, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_200_OK, msg=response.data)

    def test_url_template_group_list(self):
        response = self.client.get(self.url_template_group_create_list, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_200_OK, msg=response.data)
