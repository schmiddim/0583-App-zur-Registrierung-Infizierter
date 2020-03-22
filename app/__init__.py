from pyramid.config import Configurator
from pyramid.settings import aslist
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.events import NewRequest
from pyramid.events import subscriber
import logging

log = logging.getLogger(__name__)


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()

    request.add_finished_callback(cleanup)

    return session


def my_locale_negotiator(request):
    locale_name = request.params.get('lang')
    if locale_name is not None:
        return locale_name

    languages = aslist(request.registry.settings['available_languages'])
    if request.accept_language:
        accepted = request.accept_language
        settings = request.registry.settings
        locale = accepted.best_match(languages, settings.get('pyramid.default_locale_name', 'en'))
        return locale


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        engine = engine_from_config(settings, prefix='sqlalchemy.')
        config.registry.dbmaker = sessionmaker(bind=engine)
        config.add_request_method(db, reify=True)
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.add_translation_dirs('app:locale')
        config.set_locale_negotiator(my_locale_negotiator)
        config.scan()

    return config.make_wsgi_app()
