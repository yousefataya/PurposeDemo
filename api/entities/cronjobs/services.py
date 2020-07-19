from api.core import Mixin
from ...db import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
from sqlalchemy.ext.automap import automap_base
class JobLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'cron_job_lookup_ai'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= db.Column(db.String , nullable = False)
    lookupValue = db.Column(db.String , nullable = False)



