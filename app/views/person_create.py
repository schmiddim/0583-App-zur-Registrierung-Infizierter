from pyramid.view import view_config
import logging
import random
import string
from .. import models

log = logging.getLogger(__name__)


@view_config(route_name='person_create', renderer='../templates/submit_person_info/main.jinja2')
def person_info(request):
    person = models.Person()
    firstname_has_error = False
    lastname_has_error = False
    phonenumber_has_error = False
    email_has_error = False
    firstname = ''
    lastname = ''
    phonenumber = ''
    email = ''

    if request.method == "POST":
        firstname = request.POST['firstname'].strip()
        lastname = request.POST['lastname'].strip()
        phonenumber = request.POST['phonenumber'].strip()
        email = request.POST['email'].strip()

        firstname_has_error = False if firstname != '' else True
        lastname_has_error = False if lastname != '' else True
        phonenumber_has_error = False if phonenumber != '' else True
        email_has_error = False if email != '' else True

        if firstname_has_error == False and lastname_has_error == False and phonenumber_has_error == False and email_has_error == False:
            #case_number ="2erc3f"
            symbols = string.ascii_lowercase + string.digits
            case_number = ''.join(random.choice(symbols) for _ in range(6))
            person.firstname = firstname
            person.lastname = lastname
            person.phone_number = phonenumber
            person.email = email
            person.case_number = case_number
            request.dbsession.add(person)

            request.response.set_cookie('case_number', case_number)

            return {
                'successfully_submitted': True,
                "case_number": case_number

            }

    return {
        'successfully_submitted': False,
        'firstname_has_error': firstname_has_error,
        'lastname_has_error': lastname_has_error,
        'phonenumber_has_error': phonenumber_has_error,
        'email_has_error': email_has_error,
        'firstname': firstname,
        'lastname': lastname,
        'phonenumber': phonenumber,
        'email': email,

    }


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
