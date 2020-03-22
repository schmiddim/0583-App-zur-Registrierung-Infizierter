from pyramid.view import view_config
from .. import models
import json
from ..alchemy_encoder import AlchemyEncoder


@view_config(route_name="json_person_status", renderer='json')
def json_person_view(request):
    case_number = request.matchdict['case_number']
    person_query = request.dbsession.query(models.Person).filter_by(case_number=case_number)
    person = person_query.first()
    return json.loads(json.dumps(person, cls=AlchemyEncoder))



@view_config(route_name='person_status', renderer='../templates/status/main.jinja2')
def person_view(request):
    email_has_error = False
    case_number_has_error = False
    case_number = ""
    email = ""

    if request.method == 'POST':
        not_found = False
        email = request.POST['email'].strip()
        case_number = request.POST['case_number'].strip()
        email_has_error = False if email != '' else True
        case_number_has_error = False if case_number != '' else True

        person_query = request.dbsession.query(models.Person).filter_by(case_number=case_number)
        case_number_found = person_query.scalar() is not None

        if case_number_has_error == False and email_has_error == False:
            person = person_query.first()
            if person is None:
                not_found = True

            return {
                'not_found': not_found,
                'successfully_submitted': True,
                'case_number_has_error': case_number_has_error,
                'email_has_error': email_has_error,
                'case_number': case_number,
                'case_number_found': case_number_found,
                'person': person,
                'email': email,

            }

    return {
        'successfully_submitted': False,
        'case_number_has_error': case_number_has_error,
        'email_has_error': email_has_error,
        'case_number': case_number,
        'email': email,

    }
