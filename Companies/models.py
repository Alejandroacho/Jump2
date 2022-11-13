from django.db.models import CharField
from django.db.models import Field
from django.db.models import IntegerField
from django.db.models import Model


class Company(Model):
    id: Field = CharField(primary_key=True, max_length=100)
    website: Field = CharField(max_length=100, blank=True, null=True)
    name: Field = CharField(max_length=100, blank=True, null=True)
    founded: Field = IntegerField(blank=True, null=True)
    size: Field = CharField(max_length=10, blank=True, null=True)
    locality: Field = CharField(max_length=100, blank=True, null=True)
    region: Field = CharField(max_length=100, blank=True, null=True)
    country: Field = CharField(max_length=100, blank=True, null=True)
    industry: Field = CharField(max_length=100, blank=True, null=True)
    linkedin_url: Field = CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return getattr(self, "name") or getattr(self, "id")
