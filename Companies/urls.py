from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from Companies.views import CompanyViewSet


router: DefaultRouter = DefaultRouter()
router.register("companies", CompanyViewSet, basename="companies")

urlpatterns: list = [path("", include(router.urls))]