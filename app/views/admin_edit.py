from pyramid.view import view_config
import logging
from .. import models

log = logging.getLogger(__name__)


@view_config(route_name='admin_edit_case', renderer='../templates/admin/edit_status.jinja2')
def admin_edit_case(request):
    db_id = request.GET['id']
    has_error = False
    if "" == db_id:
        has_error = True

    if request.method == "POST" and not has_error:
        status = request.POST['status']
        log.log(logging.INFO, "update status to {} for user {}".format(status, db_id))
        person = request.dbsession.query(models.Person).get(db_id)
        person.covid_status = status

        return {"id": person.id,
                "first_name": person.firstname,
                "last_name": person.lastname,
                "phone_number": person.phone_number,
                "case_number": person.case_number,
                "covid_status": person.covid_status,
                "email": person.email,
                "uddated": True
                }

    person = request.dbsession.query(models.Person).get(db_id)
    if person is None:
        has_error = True

    return {"id": person.id,
            "first_name": person.firstname,
            "last_name": person.lastname,
            "phone_number": person.phone_number,
            "case_number": person.case_number,
            "covid_status": person.covid_status,
            "email": person.email,
            "has_error": has_error
            }
