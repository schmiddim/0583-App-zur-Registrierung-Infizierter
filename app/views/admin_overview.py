from pyramid.view import view_config
import logging

log = logging.getLogger(__name__)



@view_config(route_name='admin_overview', renderer='../templates/admin/overview.jinja2')
def admin_overview(request):
    return {}

@view_config(route_name='admin_overview_json', renderer='json')
def admin_overview_json(request):

    #@todo fetch data from db!
    return {
        'data': [

                    {"id": 1,
                     "first_name": "Michael",
                     "last_name": "Schmitt",
                     "phone_number": "0171 957 97 20",
                     "case_number": "acsmoi24bv",
                     "covid_status": "healthy",
                     "email": "klaus@web.de"
                     },
                    {"id": 2,
                     "first_name": "Hansi",
                     "last_name": "Hamster",
                     "phone_number": "0171 957 97 20",
                     "case_number": "acsmoi24bv",
                     "covid_status": "healthy",
                     "email": "klaus@web.de"
                     },
                    {"id": 3,
                     "first_name": "Foo",
                     "last_name": "Bar",
                     "phone_number": "0171 957 97 20",
                     "case_number": "acsmoi24bv",
                     "covid_status": "healthy",
                     "email": "klaus@web.de"
                     }

                ]
    }