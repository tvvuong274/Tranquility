from django.utils.translation import ugettext_lazy as _


OUTPUT_AUTHORIZATION_API_TYPE_BASIC_AUTH = 1
OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN = 2

OUTPUT_AUTHORIZATION_API_TYPE = {
  OUTPUT_AUTHORIZATION_API_TYPE_BASIC_AUTH: _('Basic Auth'),
  OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN: _('Bearer Token')
}

OUTPUT_AUTHORIZATION_API_TYPE_CHOICE = ((k, v) for k, v in OUTPUT_AUTHORIZATION_API_TYPE.items())
OUTPUT_AUTHORIZATION_API_TYPE_LIST = [(k, v) for k, v in OUTPUT_AUTHORIZATION_API_TYPE.items()]

################################################################################################
################################################################################################

OUTPUT_API_METHOD_TYPE_GET = 1
OUTPUT_API_METHOD_TYPE_POST = 2

OUTPUT_API_METHOD_TYPE = {
  OUTPUT_API_METHOD_TYPE_GET: _('GET'),
  OUTPUT_API_METHOD_TYPE_POST: _('POST')
}

OUTPUT_API_METHOD_TYPE_CHOICE = ((k, v) for k, v in OUTPUT_API_METHOD_TYPE.items())
OUTPUT_API_METHOD_TYPE_LIST = [(k, v) for k, v in OUTPUT_API_METHOD_TYPE.items()]
