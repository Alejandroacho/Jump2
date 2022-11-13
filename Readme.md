# Jump2Digital Backend

This project is my purpose for the backend challenge.

## Background
This project was born in order to participate in the [Jump2Digital](https://barcelonadigitaltalent.com/jump2digital/) hackathon in its 2022 edition.

## Usage
After running the project (see the installation step), you will be able to interact with the data using the django admin in the following url:

    http://0.0.0.0:8000/admin/

If you are not seeing any kind of data in the company section, you may run the populate command:

    python3 manage.py populate_companies


### API
Once you have ran and set the project with its data, you can use the API:

In order to see the companies according to the founded year:

    http://0.0.0.0:8000/api/companies?ordering=founded ##ascending
    http://0.0.0.0:8000/api/companies?ordering=-founded  ##descending


In order to see the companies according to the size:

    http://0.0.0.0:8000/api/companies?ordering=size  ##ascending
    http://0.0.0.0:8000/api/companies?ordering=-size  ##descending

To see the overview of the companies:

    http://0.0.0.0:8000/api/companies/overview

## Installation
Inside the main folder after the cloning the repo:

    pip install requirements.txt
    python3 manage.py runserver 0.0.0.0:8000

    # Test command
    python manage.py test

## Stack
- [Django (4.1.2).](https://www.djangoproject.com/)
- [Django Rest Framework (3.12.4).](https://www.django-rest-framework.org/)

## Contact info
- [LinkedIn.](https://www.linkedin.com/in/alejandroacho/)
- [GitHub.](https://github.com/Alejandroacho)

## License
MIT
