from db_models.template.form.models import TemplateForm
import json
from django.urls import path, reverse
from django.conf.urls import include
from library.constant.test_case import (
    METADATA_GROUP_LIST,
    METADATA_LIST,
    OUTPUT_AUTHORIZATION_API_LIST,
    TEMPLATE_FIELD_LIST,
    TEMPLATE_FORM_LIST,
    TEMPLATE_LIST,
    TEMPLATE_SOURCE_API_LIST,
    USER_NAME_TEST_CASE,
    PASSWORD_TEST_CASE,
)
from api.v1.metadata.test_datas import DATA_AUTHORIZATION_APIS, DATA_CREATE_METADATA, DATA_METADATAS, \
    DATA_METADATA_GROUPS, METADATA_ID_FOR_DELETE
from rest_framework.test import APIClient, APITestCase, URLPatternsTestCase
from db_models.user.models import User
from db_models.metadata.models import Metadata, MetadataGroup
from db_models.output_authorization_api.models import OutputAuthorizationAPI
from db_models.template.source_api.models import TemplateSourceAPI
from db_models.template.models import Template
from db_models.template.field.models import TemplateField


class BaseAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("api/", include("api.urls")),
    ]

    def setUp(self):
        self.user = User.objects.create(name=USER_NAME_TEST_CASE, username=USER_NAME_TEST_CASE)
        self.user.set_password(PASSWORD_TEST_CASE)
        self.user.save()

        self.token = User.get_token(self.user)
        self.client = APIClient()
        self.api_authentication()

        # Created Data Default.
        # self.create_default()
        self.making_database()

        # Create Metadata for Delete
        self.create_metadata_for_delete(DATA_CREATE_METADATA)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def making_database(self):
        output_authorization_apis = []
        for output_authorization_api in OUTPUT_AUTHORIZATION_API_LIST:
            output_authorization_apis.append(
                OutputAuthorizationAPI(
                    name=output_authorization_api["name"],
                    type=output_authorization_api["type"],
                    auth_json=output_authorization_api["auth_json"],
                    domain=output_authorization_api["domain"],
                )
            )
        OutputAuthorizationAPI.objects.bulk_create(output_authorization_apis)

        metadata_groups = []
        for metadata_group in METADATA_GROUP_LIST:
            metadata_groups.append(MetadataGroup(name=metadata_group))
        MetadataGroup.objects.bulk_create(metadata_groups)

        metadatas = []
        for metadata in METADATA_LIST:
            metadatas.append(Metadata(
                metadata_group=MetadataGroup.objects.get(
                    id=metadata["metadata_group_id"]),
                name=metadata["name"],
                code=metadata["code"],
                c_system_type=metadata["c_system_type"],
                active_flag=metadata["active_flag"],
                note=metadata["note"],
                data_input_flag=metadata["data_input_flag"],
                data_output_flag=metadata["data_output_flag"],
                output_keyword=metadata["output_keyword"],
                output_authorization_api_id=metadata["output_authorization_api_id"],
                c_output_method_type=metadata["c_output_method_type"],
                output_api=metadata["output_api"],
                output_token=metadata["output_token"],
                output_parameter_list=metadata["output_parameter_list"],
                output_result_key=metadata["output_result_key"],
                input_type_format_id=metadata["input_type_format_id"],
                input_condition_json=metadata["input_condition_json"],
            ))
        Metadata.objects.bulk_create(metadatas)

        templates = []
        for template in TEMPLATE_LIST:
            templates.append(Template(
                name=template["name"],
                start_date=template["start_date"],
                end_date=template["end_date"],
                number=template["number"],
                title=template["title"],
                code=template["code"],
                c_status=template["c_status"],
                khcn_flag=template["khcn_flag"],
                khdn_flag=template["khdn_flag"],
                dntn_flag=template["dntn_flag"],
                scb_flag=template["scb_flag"],
                template_api=template["template_api"],
                file_uuid=template["file_uuid"],
            ))
        Template.objects.bulk_create(templates)

        template_fields = []
        for template_field in TEMPLATE_FIELD_LIST:
            template_fields.append(TemplateField(
                template=Template(id=template_field["template_id"]),
                metadata=Metadata(id=template_field["metadata_id"]),
                key=template_field['key']
            ))
        TemplateField.objects.bulk_create(template_fields)

        template_source_apis = []
        for template_source_api in TEMPLATE_SOURCE_API_LIST:
            template_source_apis.append(
                TemplateSourceAPI(
                    template=Template(id=template_source_api["template_id"]),
                    output_authorization_api=OutputAuthorizationAPI(
                        id=template_source_api["output_authorization_api_id"]),
                    c_output_method_type=template_source_api["c_output_method_type"],
                    output_api=template_source_api["output_api"],
                    output_token=template_source_api["output_token"],
                    output_parameter_list=template_source_api["output_parameter_list"],
                )
            )
        TemplateSourceAPI.objects.bulk_create(template_source_apis)

        template_forms = []
        for template_form in TEMPLATE_FORM_LIST:
            template_forms.append(TemplateForm(
                template=Template(id=template_form["template_id"]),
                template_field=TemplateField(id=template_form["template_field_id"]),
                ord=template_form["ord"],
                row=template_form["row"],
                c_offset=template_form["c_offset"],
                label=template_form["label"],
                output_flag=template_form["output_flag"],
                output_edit_flag=template_form["output_edit_flag"],
                require_flag=template_form["require_flag"],
                c_type=template_form["c_type"],
                default_data=template_form["default_data"],
            ))
        TemplateForm.objects.bulk_create(template_forms)

    def create_default(self):
        self.create_metadata_group(DATA_METADATA_GROUPS)
        self.create_output_authorization(DATA_AUTHORIZATION_APIS)

    def create_metadata_group(self, data):
        metadata_groups = [MetadataGroup(name=item["name"]) for item in data]
        MetadataGroup.objects.bulk_create(metadata_groups)

    def create_output_authorization(self, data):
        output_authorizations = [
            OutputAuthorizationAPI(name=item["name"], type=item["type"], auth_json=item["auth_json"],
                                   domain=item["domain"]) for item in data
        ]
        OutputAuthorizationAPI.objects.bulk_create(output_authorizations)

    def create_metadata_for_delete(self, data):
        Metadata.objects.create(
            id=METADATA_ID_FOR_DELETE,
            code="Test Delete",
            name=data['name'],
            note=data['note'],
            c_system_type=data['c_system_type'],
            active_flag=data['active_flag'],
            output_keyword=data['output_keyword'],
            c_output_method_type=data['c_output_method_type'],
            output_api=data['output_api'],
            output_token=data['output_token'],
            output_parameter_list=data['output_parameter_list'],
            output_result_key=data['output_result_key'],
            data_input_flag=data['data_input_flag'],
            data_output_flag=data['data_output_flag'],
            input_type_format_id=data['input_type_format_id'],
            input_condition_json=data['input_condition_json'],
            metadata_group=MetadataGroup(id=data['metadata_group_id']),
            output_authorization_api=OutputAuthorizationAPI(id=data['output_authorization_api_id']),
        )
