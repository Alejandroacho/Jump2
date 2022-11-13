from django.db.models import Model
from rest_framework.serializers import ModelSerializer

from Companies.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model: Model = Company
        fields: str = "__all__"
