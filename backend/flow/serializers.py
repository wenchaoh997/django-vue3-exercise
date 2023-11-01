from rest_framework import serializers

from .models import AuditFlow, AuditFlowDetail

class AuditFlowSerializer(serializers.ModelSerializer):
    class META:
        model = AuditFlow
        fields = "__all__"

class AuditFlowDetailSerializer(serializers.ModelSerializer):
    class META:
        model = AuditFlowDetail
        fields = "__all__"
