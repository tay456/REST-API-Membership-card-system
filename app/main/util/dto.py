""""the dto will be responsible for carrying data between processes"""

from flask_restplus import Namespace, fields

""""reates a new namespace for user related operations."""


class UserDto:
    api = Namespace('user', description='user related operations')

    """creates a new user dto through the model interface provided by the api namespace """

    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
