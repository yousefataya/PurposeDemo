from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields

from flask_jwt_extended import get_jwt_identity

from .services import get_user_by_id, update_user
from api.core import validate_json_body

bp = Blueprint('user', __name__, url_prefix='/users')

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.
class UserTokenObject:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what custom claims
# should be added to the access token.
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what the identity
# of the access token should be.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


@app.route('/token-create', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'admin':
        return jsonify({"msg": "Bad username or password"}), 401

    # Create an example UserObject
    user = UserTokenObject(username='admin', roles=['foo', 'bar'])

    # We can now pass this complex object directly to the
    # create_access_token method. This will allow us to access
    # the properties of this object in the user_claims_loader
    # function, and get the identity of this object from the
    # user_identity_loader function.
    access_token = create_access_token(identity=user)
    ret = {'access_token': access_token}
    return jsonify(ret), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    ret = {
        'current_identity': get_jwt_identity(),  # test
        'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
    }
    return jsonify(ret), 200

@bp.route('/current-logged', methods=['GET'])
def get_current_user():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    return jsonify(__serialize_user(user))


class AddressSchema(Schema):
    street = fields.String(required=True, allow_none=True)
    city = fields.String(required=True, allow_none=True)
    zipCode = fields.String(required=True, allow_none=True)


class UpdateUserSchema(Schema):
    email = fields.Email(required=True)
    firstName = fields.String(required=True, allow_none=True)
    lastName = fields.String(required=True, allow_none=True)
    userName = fields.String(required=True, allow_none=True)
    age = fields.Number(required=True, allow_none=True)
    address = fields.Nested(AddressSchema())


@bp.route('/current', methods=['PUT'])
@validate_json_body(UpdateUserSchema)
def update_current_user():
    user_id = get_jwt_identity()
    data = request.get_json()

    user = get_user_by_id(user_id)

    user.email = data['email']
    user.first_name = data['firstName']
    user.last_name = data['lastName']
    user.login = data['userName']
    user.age = data['age']
    user.street = data['address']['street']
    user.city = data['address']['city']
    user.zip = data['address']['zipCode']

    update_user(user)

    return jsonify(__serialize_user(user))


def __serialize_user(user):
    return {
        'id': user.id,
        'email': user.email,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'userName': user.login,
        'age': user.age,
        'address': {
            'street': user.street,
            'city': user.city,
            'zipCode': user.zip,
        }
    }
