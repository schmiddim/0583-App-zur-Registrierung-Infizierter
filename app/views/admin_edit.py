from pyramid.view import view_config
import logging

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

        # @todo update status for user and return the user object
        return {"id": 1,
                "first_name": "Michael",
                "last_name": "Schmitt",
                "phone_number": "0171 957 97 20",
                "case_number": "acsmoi24bv",
                "covid_status": "infected",
                "email": "klaus@web.de",
                "uddated": True
                }

    # @todo fetch user by id - set has_error to True if nothing is found or raise exception
    return {"id": 1,
            "first_name": "Michael",
            "last_name": "Schmitt",
            "phone_number": "0171 957 97 20",
            "case_number": "acsmoi24bv",
            "covid_status": "infected",
            "email": "klaus@web.de",
            "has_error": has_error
            }
