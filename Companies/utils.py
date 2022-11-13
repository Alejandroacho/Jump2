from io import FileIO
from json import load

from Companies.models import Company


def save_in_db_companies_from_json_file(json_file: FileIO) -> None:
    companies: list = load(json_file)
    for company in companies:
        Company.objects.create(**company)

def get_field_options_from_db(field_name: str) -> list:
    return Company.objects.values_list(
        field_name, flat=True
    ).distinct().order_by(field_name)
