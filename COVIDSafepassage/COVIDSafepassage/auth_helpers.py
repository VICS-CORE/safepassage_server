import os
import firebase_admin
from firebase_admin import auth, credentials
from firebase_admin.auth import InvalidIdTokenError, InvalidSessionCookieError
from firebase_admin.exceptions import FirebaseError
from rest_framework import exceptions


# JSON formatted key file you get directly from firebase
FIREBASE_ACCOUNT_KEY_FILE = os.path.abspath(os.getcwd()) + '/static/firebase/service-account.json'

credentials = credentials.Certificate(FIREBASE_ACCOUNT_KEY_FILE)
firebase = firebase_admin.initialize_app(credentials)


def verify_id_token(id_token):
    try:
        verified_claims = auth.verify_id_token(id_token)
    except ValueError:
        raise exceptions.AuthenticationFailed('Authentication Token Format Error')
    except InvalidIdTokenError:
        raise exceptions.AuthenticationFailed('Invalid Authentication Token')

    return verified_claims


def create_session_cookie(id_token, expires_in):
    try:
        session_claims = auth.create_session_cookie(id_token, expires_in)
    except ValueError:
        raise exceptions.AuthenticationFailed('Invalid Cookie Parameters')
    except FirebaseError:
        raise exceptions.AuthenticationFailed('Firebase error while creating cookie')

    return session_claims


def verify_session_cookie(session_cookie):
    try:
        verified_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)

    except ValueError:
        raise exceptions.ValidationError('Invalid Cookie Parameters')
    except InvalidSessionCookieError:
        raise exceptions.ValidationError('Not a valid Firebase session cookie')

    return verified_claims
