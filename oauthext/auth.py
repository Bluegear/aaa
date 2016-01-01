from django.contrib.auth.models import User


class WalletAuthenticationBackend(object):

    def authenticate(self, username=None, password=None):

        # TODO: Replace credential validate with the orion API call
        if username != 'wallet':
            return None

        if password != 'wallet':
            return None

        # Create wallet user if not exists.
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username, password=password)
            user.is_staff = False
            user.is_superuser = False
            user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
