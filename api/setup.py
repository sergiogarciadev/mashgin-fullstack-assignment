from setuptools import setup

setup(
    name='shopping_api',
    packages=['shopping_api'],
    install_requires=[
        'flask',
        'flask-restplus',
        'flask-marshmallow',
        'flask-sqlalchemy',
        'flask-migrate',
        'marshmallow-sqlalchemy',
        'werkzeug==0.16.0',
        'psycopg2'
    ],
    extras_require = {
        'prod':  ['gunicorn']
    }
)
