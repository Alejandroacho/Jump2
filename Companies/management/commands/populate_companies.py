from io import FileIO
from pathlib import Path

from django.core.management.base import BaseCommand

from Companies.utils import save_in_db_companies_from_json_file


class Command(BaseCommand):

    help: str = "Populate companies into DB from json file"

    def handle(self, *args: tuple, **options: dict) -> None:
        base_path: str = Path(__file__).resolve().parent.parent.parent
        json_file_path: str = f"{base_path}/company_list.json"
        json_file: FileIO = open(json_file_path)
        save_in_db_companies_from_json_file(json_file)
        json_file.close()
