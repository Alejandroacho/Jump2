from django.db.models import QuerySet
from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from Companies.models import Company
from Companies.serializers import CompanySerializer
from Companies.utils import get_field_options_from_db


class CompanyViewSet(ListModelMixin, GenericViewSet):
    queryset: QuerySet = Company.objects.all()
    serializer_class: CompanySerializer = CompanySerializer
    permission_classes: list = []
    filter_backends: list = [OrderingFilter]
    ordering_fields = ['size', 'founded']

    @action(detail=False, methods=['get'])
    def overview(self, request: HttpRequest) -> Response:
        industries: list = get_field_options_from_db('industry')
        sizes: list = get_field_options_from_db('size')
        found_years: list = get_field_options_from_db('founded')
        return Response({
            'industries': self.get_field_overview(industries, 'industry'),
            'sizes': self.get_field_overview(sizes, 'size'),
            'found_years': self.get_field_overview(found_years, 'founded'),
        })

    def get_field_overview(self, options: list, field: str) -> list:
        return [
            {
                field: option,
                'count': Company.objects.filter(**{field: option}).count()
            }
            for option in options
        ]
