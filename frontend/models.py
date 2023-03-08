from django.db import models
import uuid


class Permit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    project_address = models.CharField(max_length=255)
    project_documents = models.CharField(max_length=255)


class PermitFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permit = models.ForeignKey(Permit, models.RESTRICT)
    document = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)