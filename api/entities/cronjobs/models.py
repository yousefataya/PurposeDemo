from api.core import Mixin
from ...db import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
class CronJob(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'cron_job_ai'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jobName= db.Column(db.String , nullable = False)
    JobCode = db.Column (db.String , nullable = False , unique = True)
    startDate = db.Column(db.DateTime , nullable = False)
    status= db.Column(db.Boolean , nullable = False , default = False)
    createdDate = db.Column (db.DateTime , nullable = False , default=datetime.datetime.utcnow)
    cronExpression= db.Column (db.String , nullable = False)

