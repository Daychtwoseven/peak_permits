from django.db import models
import uuid


class Permit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name} | Email: {self.email} | Phone Number: {self.phone_number}'


class PEStamp(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    residential = models.BooleanField(default=False)
    commercial = models.BooleanField(default=False)
    mounting_roof = models.BooleanField(default=False)
    mounting_ground = models.BooleanField(default=False)
    mounting_both = models.BooleanField(default=False)
    stamping_email = models.BooleanField(default=False)
    stamping_wet = models.BooleanField(default=False)
    stamping_both = models.BooleanField(default=False)
    request_structural = models.BooleanField(default=False)
    request_electrical = models.BooleanField(default=False)
    request_stamp = models.BooleanField(default=False)
    request_both = models.BooleanField(default=False)
    job_pv = models.BooleanField(default=False)
    job_battery = models.BooleanField(default=False)
    job_both = models.BooleanField(default=False)
    lock_yes = models.BooleanField(default=False)
    lock_no = models.BooleanField(default=False)
    third_party_yes = models.BooleanField(default=False)
    third_party_no = models.BooleanField(default=False)
    attic_photo = models.FileField(upload_to='uploads/')
    roof_photo = models.FileField(upload_to='uploads/')
    plan_set = models.FileField(upload_to='uploads/')
    other_attachment = models.FileField(upload_to='uploads/')
    comments = models.TextField()