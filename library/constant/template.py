import datetime
from django.utils.translation import ugettext_lazy as _

TEMPLATE_STATUS_TYPE_UNUSED = 1
TEMPLATE_STATUS_TYPE_USED = 2

TEMPLATE_STATUS_TYPE = {
    TEMPLATE_STATUS_TYPE_UNUSED: _('Unused'),
    TEMPLATE_STATUS_TYPE_USED: _('Used')
}

TEMPLATE_STATUS_TYPE_CHOICE = ((k, v) for k, v in TEMPLATE_STATUS_TYPE.items())
TEMPLATE_STATUS_TYPE_LIST = [(k, v) for k, v in TEMPLATE_STATUS_TYPE.items()]

################################################################################################
################################################################################################

TEMPLATE_TYPE_GENERAL = 1
TEMPLATE_TYPE_PRIVATE = 2

TEMPLATE_TYPE = {
    TEMPLATE_TYPE_GENERAL: _('General'),
    TEMPLATE_TYPE_PRIVATE: _('Private')
}

TEMPLATE_TYPE_CHOICE = ((k, v) for k, v in TEMPLATE_STATUS_TYPE.items())
TEMPLATE_TYPE_LIST = [(k, v) for k, v in TEMPLATE_STATUS_TYPE.items()]

################################################################################################
################################################################################################


TEMPLATE_FIELD_OFFSET_COL_1 = 1
TEMPLATE_FIELD_OFFSET_COL_2 = 2
TEMPLATE_FIELD_OFFSET_COL_3 = 3
TEMPLATE_FIELD_OFFSET_COL_4 = 4
TEMPLATE_FIELD_OFFSET_COL_6 = 6
TEMPLATE_FIELD_OFFSET_COL_7 = 7
TEMPLATE_FIELD_OFFSET_COL_8 = 8
TEMPLATE_FIELD_OFFSET_COL_9 = 9
TEMPLATE_FIELD_OFFSET_COL_12 = 12

TEMPLATE_FIELD_OFFSET = {
    TEMPLATE_FIELD_OFFSET_COL_1: _('COL-1'),
    TEMPLATE_FIELD_OFFSET_COL_2: _('COL-2'),
    TEMPLATE_FIELD_OFFSET_COL_3: _('COL-3'),
    TEMPLATE_FIELD_OFFSET_COL_4: _('COL-4'),
    TEMPLATE_FIELD_OFFSET_COL_6: _('COL-6'),
    TEMPLATE_FIELD_OFFSET_COL_7: _('COL-7'),
    TEMPLATE_FIELD_OFFSET_COL_8: _('COL-8'),
    TEMPLATE_FIELD_OFFSET_COL_9: _('COL-9'),
    TEMPLATE_FIELD_OFFSET_COL_12: _('COL-12')
}

TEMPLATE_FIELD_OFFSET_CHOICE = ((k, v) for k, v in TEMPLATE_FIELD_OFFSET.items())
TEMPLATE_FIELD_OFFSET_LIST = [(k, v) for k, v in TEMPLATE_FIELD_OFFSET.items()]


TEMPLATE_DEFAULT_SORT_A_TO_Z = 0
TEMPLATE_DEFAULT_SORT_Z_TO_A = 1
TEMPLATE_DEFAULT_SORT = {
    TEMPLATE_DEFAULT_SORT_A_TO_Z: _("A-Z"),
    TEMPLATE_DEFAULT_SORT_Z_TO_A: _("Z-A")
}
TEMPLATE_DEFAULT_SORT_CHOICE = ((k, v) for k, v in TEMPLATE_DEFAULT_SORT.items())
TEMPLATE_DEFAULT_SORT_LIST = [(k, v) for k, v in TEMPLATE_DEFAULT_SORT.items()]
