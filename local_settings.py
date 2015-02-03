
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "b3dd3ce5-e3fe-4d50-949b-abca479f9b7bfc735ed2-330c-450b-b14d-1224836cccb8fba8eae8-430d-482a-94f8-f6fcaa913d0d"
NEVERCACHE_KEY = "44f89743-a2e1-4503-a162-5fb1a8ea7474893b5142-0853-476a-85d7-9d8931b3977f32ea9dc2-a4d1-48a2-b92d-567b87fbfb97"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "tantest01",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "root",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
