from ceba_builders.wsgi import application

# This is not needed in the standard environment
# from google.appengine.api import wrap_wsgi_app

app = application  # No need for wrap_wsgi_app in the standard environment
