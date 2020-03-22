from pyramid.view import view_config
import logging
from .. import models

log = logging.getLogger(__name__)


@view_config(route_name='admin_overview', renderer='../templates/admin/overview.jinja2')
def admin_overview(request):
    return {}


@view_config(route_name='admin_overview_json', renderer='json')
def admin_overview_json(request):
    db_data = []
    for person in request.dbsession.query(models.Person).all():
        person_dict = person.__dict__.copy()
        del person_dict['_sa_instance_state']
        db_data.append(person_dict)
    return db_data  # use json.dumps() instead?
