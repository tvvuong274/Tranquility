from rest_framework import serializers

from api.base.serializers import InheritedSerializer


class InputTypeListSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of input type (constant)")
    name = serializers.CharField(help_text="`name` of input type")
    total_used = serializers.IntegerField(help_text="Cho biết loại này đã được sử dụng bao nhiêu lần")


class InputTypeFormatListSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of input type format (constant)")
    description = serializers.CharField(help_text="`description` of input type format")
    conditions = serializers.ListField(child=serializers.JSONField(), help_text="Danh sách điều kiện của format đó")


class InputTypeFormatConditionListSuccessResponseSerializer(InheritedSerializer):
    checked_flag = serializers.BooleanField(help_text="Giá trị cho radio hay checkbox trước `name` nếu có")
    name = serializers.CharField(help_text="`name`")
    type = serializers.CharField(help_text="Kiểu của element phía sau `name`")
    action = serializers.CharField(help_text="Check các ràng buộc cho `value` của dòng hiện tại (nếu có)")
    value = serializers.ListField(child=serializers.JSONField(), help_text="Giá trị các điều kiện con (nếu có) hoặc giá trị ô hiện tại")

