import phonenumbers
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from COVIDSafepassage.auth_helpers import verify_session_cookie
from passsystem.models import User

FIREBASE_UID_FIELD = 'user_id'
FIREBASE_PHONE_FIELD = 'phone_number'


class BaseFirebaseAuthentication(BaseAuthentication):
    """
    Token based authentication using firebase.
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using Firebase authentication.  Otherwise returns `None`.
        """
        firebase_session = request.COOKIES.get('SESSION')
        if firebase_session is None:
            return None

        payload = verify_session_cookie(firebase_session)
        user = self._authenticate_credentials(payload)
        return user, payload

    def _authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        uid_field = FIREBASE_UID_FIELD
        phone_field = FIREBASE_PHONE_FIELD
        uid = payload[uid_field]
        if not uid:
            raise exceptions.AuthenticationFailed('Invalid payload.')
        try:
            if payload['iss'] != 'https://session.firebase.google.com/safe-passage-india':
                raise exceptions.AuthenticationFailed('Wrong issuer.')
            if phone_field not in payload:
                msg = _('User Phone number not yet available.')
                raise exceptions.AuthenticationFailed(msg)

            phone_number = phonenumbers.parse(payload[phone_field], None)
            return User.objects.get(**{'user_phonenumber': phone_number.national_number})
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not existing in the database')
