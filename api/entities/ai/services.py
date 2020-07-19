from api.core import Mixin
from ...db import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
class Urls(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'url_info_ai'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    urlLink = db.Column (db.String , nullable = False)
    createdDate = db.Column(db.DateTime ,  default=datetime.datetime.utcnow)
    isExpired = db.Column(db.Boolean , nullable = False , default = False)
    Description= db.Column(db.String , nullable = True)
    notes = db.Column(db.String , nullable = True)

