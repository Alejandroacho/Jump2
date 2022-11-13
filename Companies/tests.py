from django.test import TestCase
from django.core.management import call_command
from rest_framework.test import APIClient

from Companies.models import Company

class TestPopulate(TestCase):
    def test_populate(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        call_command('populate_companies')
        company_count = Company.objects.count()
        self.assertFalse(company_count == 0)

class TestOrderingEndpoint(TestCase):
    def test_get_companies_ordered_by_size_ascending(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        Company.objects.create(id="test", name='Company 1', size='1-10')
        Company.objects.create(id="test2", name='Company 2', size='11-50')
        url: str = '/api/companies/?ordering=size'
        client: APIClient = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Company 1')
        self.assertEqual(response.data[1]['name'], 'Company 2')

    def test_get_companies_ordered_by_size_descending(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        Company.objects.create(id="test", name='Company 1', size='1-10')
        Company.objects.create(id="test2", name='Company 2', size='11-50')
        url: str = '/api/companies/?ordering=-size'
        client: APIClient = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Company 2')
        self.assertEqual(response.data[1]['name'], 'Company 1')

    def test_get_companies_ordered_by_size_ascending(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        Company.objects.create(id="test", name='Company 1', founded=2020)
        Company.objects.create(id="test2", name='Company 2', founded=2022)
        url: str = '/api/companies/?ordering=founded'
        client: APIClient = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Company 1')
        self.assertEqual(response.data[1]['name'], 'Company 2')
        url: str = '/api/companies/?ordering=-founded'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Company 2')
        self.assertEqual(response.data[1]['name'], 'Company 1')

    def test_get_companies_ordered_by_size_descending(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        Company.objects.create(id="test", name='Company 1', founded=2020)
        Company.objects.create(id="test2", name='Company 2', founded=2022)
        url: str = '/api/companies/?ordering=-founded'
        client: APIClient = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Company 2')
        self.assertEqual(response.data[1]['name'], 'Company 1')

    def test_get_companies_overviewg(self) -> None:
        company_count: int = Company.objects.count()
        self.assertEqual(company_count, 0)
        Company.objects.create(
            name='Company 1', founded=2020, industry='software', size='1-10'
        )
        url: str = '/api/companies/overview/'
        client: APIClient = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['industries'][0]['industry'], 'software')
        self.assertEqual(response.data['industries'][0]['count'], 1)
        self.assertEqual(response.data['sizes'][0]['size'], '1-10')
        self.assertEqual(response.data['sizes'][0]['count'], 1)
        self.assertEqual(response.data['found_years'][0]['founded'], 2020)
        self.assertEqual(response.data['found_years'][0]['count'], 1)
