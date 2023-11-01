from django.db import models
import uuid

# Create your models here.
class AuditFlow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)

    AUDITTYPES = (
        ("b", "book"),
    )
    auditType = models.CharField(
        max_length=2,
        choices=AUDITTYPES,
        blank=False,
        default="b",
    )

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=False)
    createTime = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ("a", "approve"),
        ("r", "reject"),
        ("w", "work in progress"),
        ("c", "cancel"),
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=False, default="w")
    totalStep = models.IntegerField(default=3)

    def __str__(self) -> str:
        return self.title

class AuditFlowDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    flowid = models.ForeignKey("AuditFlow", on_delete=models.CASCADE, null=False)
    auditor = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=False)
    remark = models.CharField(max_length=500)
    auditTime = models.DateTimeField(auto_now_add=True)
    step = models.IntegerField()