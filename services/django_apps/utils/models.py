# Django
from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        abstract = True


class BaseModelExternalID(BaseModel):
    external_id = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.external_id

    class Meta:
        abstract = True
