import dj_database_url
from decouple import config

class DB:

    @classmethod
    def config(cls, debug):
        return cls.development() if debug else cls.production()

    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'naijahelpers',
                'HOST': config('DBHOST'),
                'USER': config('DBUSER'),
                'PASSWORD': config('DBPASSWORD')
            }
        }

    @classmethod
    def production(cls):
        return {
            'default': {
                **dj_database_url(config('DATABASE_URL'))
            }
        }
