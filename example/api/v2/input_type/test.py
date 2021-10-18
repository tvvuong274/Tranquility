from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from api.base.base_test import BaseAPITestCase


class InputTypeAPITestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.url_list = reverse("input_type_list")
        self.url_list_format = reverse("input_type_list_format", args=[1])
        self.url_json_condition = reverse("input_type_json_condition", kwargs={"input_type_id": 1, "input_type_format_id": 1})

    def test_url_list_is_resolved(self):
        response = self.client.get(self.url_list, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_url_list_format_is_resolved(self):
        response = self.client.get(self.url_list_format, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_url_list_json_contidion_is_resolved(self):
        response = self.client.get(self.url_json_condition, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
