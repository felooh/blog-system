from django.apps import AppConfig


class UsersConfig(AppConfig):
<<<<<<< HEAD
    name = 'users'
=======
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
>>>>>>> v2
