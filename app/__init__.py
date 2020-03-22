from pyramid.config import Configurator
from pyramid.settings import aslist
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def my_locale_negotiator(request):
    languages = aslist(request.registry.settings['available_languages'])

@subscriber(NewRequest)
def prepare_env(event):
    request = event.request
    # set locale depending on browser settings
    settings = request.registry.settings
    locale = settings.get('pyramid.default_locale_name', 'en')
    available = [loc['code'] for loc in AVAILABLE_LOCALES]
    if request.accept_language:
        accepted = request.accept_language
        locale = accepted.best_match(available, locale)
    request._LOCALE_ = locale

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
