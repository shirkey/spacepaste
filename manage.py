#!/usr/bin/env python

from werkzeug import script, create_environ, run_wsgi_app

from spacepaste import local
from spacepaste.application import make_app
from spacepaste.database import db

dburi = 'sqlite:////tmp/spacepaste.db'

SECRET_KEY = 'no secret key'


def run_app(app, path='/'):
    env = create_environ(path, SECRET_KEY)
    return run_wsgi_app(app, env)

action_runserver = script.make_runserver(
    lambda: make_app(dburi, SECRET_KEY, debug=True),
    use_reloader=True)

action_shell = script.make_shell(
    lambda: {
        'app': make_app(dburi, SECRET_KEY, False, True),
        'local': local,
        'db': db,
        'run_app': run_app
    },
    ('\nWelcome to the interactive shell environment of spacepaste!\n'
     '\n'
     'You can use the following predefined objects: app, local, db.\n'
     'To run the application (creates a request) use *run_app*.')
)

if __name__ == '__main__':
    script.run()
