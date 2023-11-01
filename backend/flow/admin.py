from django.contrib import admin
from .models import AuditFlow, AuditFlowDetail

# Register your models here.
admin.site.register(AuditFlow)
admin.site.register(AuditFlowDetail)