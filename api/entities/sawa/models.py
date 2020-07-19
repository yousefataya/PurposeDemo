from api.core import Mixin
from ...db import db  
from sqlalchemy_utils import UUIDType

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType
import uuid
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
import datetime
from sqlalchemy.orm import relationship
#from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(JsonSerializableBase)
from sqlalchemy.orm import mapper

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
metadata = MetaData()

from api.logger import create_app
from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute
app = create_app()
from django.contrib import admin
db = SQLAlchemy(app)

from api.tokens.create.models import *

accidentPlace = Table('sawa_accident_place', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True , default=uuid.uuid4()),
            Column('accName', String(255)),
            Column('accType', String(255)),
            Column('createDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', DateTime),
            Column('description', String(255)),
            Column('notes', String(255)),
            Column('isExpired', Boolean),
            Column('lastViewed', DateTime),
            Column('type_id', UUIDType(binary=False) , ForeignKey('sawa_accident_lookup.id'))
            
            )

class AccidentPlace(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_accident_place"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    accName = Column(String, nullable=False)
    accType = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    isExpired = Column(Boolean, nullable=False)
    lastViewed = Column(DateTime, nullable=False)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_accident_lookup.id"))
    parent = relationship('AccidentTypeLookup'  , back_populates="types" , primaryjoin = "AccidentTypeLookup.id == AccidentPlace.type_id ")
#   Employee  create by 
#   Employee  Update by     

accidentTypeLookup = Table('sawa_accident_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True , default=uuid.uuid4()),
            Column('keyName', String(255)),
            Column('valueType', String(255)),
            Column('createDate', DateTime),
            Column('createBy', String(128)),
            Column('updateBy', String(128)),
            Column('updateDate', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class AccidentTypeLookup(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_accident_lookup"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    keyName = Column(String, nullable=False)
    valueType = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    types = relationship('AccidentPlace', back_populates="parent", lazy='dynamic' )
#   Employee  create by 
#   Employee  Update by 




ageRange = Table('sawa_age_range', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('FriendlyName', String(255)),
            Column('FromAge', String(255)),
            Column('createDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('NeedMoreDetail', String(255)),
            Column('notes', String(255)),
            Column('lastViewed', DateTime),
            Column('isExpired', Boolean),
            Column('Comments', String(255))
            
            )



class AgeRange(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_age_range"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    FriendlyName = Column(String, nullable=False)
    FromAge = Column(Integer, nullable=False)
    ToAge = Column(Integer , nullable = False)
    createBy = Column(String, nullable=False)
    createDate =  Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime , nullable = True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    NeedMoreDetail = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    isExpired = Column(Boolean, nullable=False)
    lastViewed = Column(DateTime, nullable=False)
    Comments = Column(String , nullable=True)
#   Employee  create by 
#   Employee  Update by 

appContactMethod=Table('sawa_app_contact_method', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('addDate', DateTime),
            Column('contactTypeDetails', String(255)),
            Column('createDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('contactName', String(255)),
            Column('notes', String(255)),
            Column('lastViewed', DateTime),
            Column('isExpired', Boolean),
            Column('Comments', String(255)),
#            Column('contact_type_lookup',UUIDType(binary=False), ForeignKey('contactTypeLookup.id'))
            )

class AppContactMethod(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_app_contact_method"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    addDate = Column(DateTime, nullable=False , default=datetime.datetime.utcnow )
    contactTypeDetails = Column(String, nullable=False)
    contactName = Column(Integer , nullable = False)
    createBy = Column(String, nullable=False)
    createDate =  Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime , nullable = True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    isExpired = Column(Boolean, nullable=False)
    lastViewed = Column(DateTime, nullable=False)
    Comments = Column(String , nullable=True)
#    contact_type_lookup =  Column('contact_type_lookup',UUIDType(binary=False), ForeignKey('contactTypeLookup.id'))
#   Employee  create by 
#   Employee  Update by 


Table('sawa_contact_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('keyName', String(255)),
            Column('valueType', String(255)),
            Column('createDate', DateTime , default=datetime.datetime.utcnow),
            Column('createBy', String(128)),
            Column('updateBy', String(128)),
            Column('updateDate', DateTime , default=datetime.datetime.utcnow),
            Column('description', String(255)),
            Column('notes', String(255)),
            Column('isExpired', Boolean),
#            relationship("AppContactMethod",backref="ContactTypeLookup", order_by="appContactMethod.id")
#            Column('lastViewed', DateTime),
#            Column('types', UUIDType(binary=False) , ForeignKey('accidentTypeLookup.id'))
            )

class ContactTypeLookup(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_contact_lookup"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keyName = Column(String, nullable=False)
    valueType = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
#    contacts = relationship("AppContactMethod",backref="contactTypeLookup", order_by="sawa_app_contact_method.id")
#   Employee  create by 
#   Employee  Update by     

applicatnTable = Table('sawa_application_base', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('firstName', String(255)),
            Column('lastName', String(255)),
            Column('createDate', DateTime),
            Column('caseName', String(255)),
            Column('createBy', String(128)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255)),
            Column('aggressingAge', Integer),
            Column('currentAge', Integer),
            Column('employeeFollowName', String(255)),
            Column('lastViewed', DateTime),
            Column('isExpired', Boolean)
            
#            Column('contact_type_lookup',UUIDType(binary=False), ForeignKey('contactTypeLookup.id'))
            )

class Application(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_application_base"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    caseName = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
#    contacts = relationship("AppContactMethod",backref="contactTypeLookup", order_by="appContactMethod.id")
    aggressingAge = Column(Integer, nullable=False)
    currentAge = Column(Integer, nullable=False)
    employeeFollowName = Column(String, nullable=False )
    lastViewed =  Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    isExpired = Column(Boolean, nullable=False )
#   Employee  create by 
#   Employee  Update by 

applicantCall = Table('sawa_application_call_base', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('callDate', String(255)),
            Column('callEndDate', String(255)),
            Column('callName', DateTime),
            Column('createDate', String(255)),
            Column('createBy', String(128)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255)),
            Column('isViolance', Integer),
            Column('isComplaintToPolice', Integer),
            Column('employeeFollowName', String(255)),
            Column('lastViewed', DateTime),
            Column('isExpired', Boolean),
            Column('isAttorneyGeneral', String(255)),
            Column('isSamePerson', String(255)),
            Column('personName', String(255)),
            Column('callerComments', Integer),
            Column('contactMethodDetail', Integer),
            Column('policeStationName', String(255)),
            Column('investigatorName', DateTime),
            Column('policeStationTel', Boolean),
            Column('policeComplaintNo', String(255)),
            Column('policeComplaintDate', String(255)),
            Column('attorneyGeneralName', String(255)),
            Column('educationalStatusDetail', Integer),
            Column('attorneyGeneralTel', Integer),
            Column('attorneyGeneralCompDate', String(255)),
            Column('educationalStatusDetail', DateTime),
            Column('policeStationTel', Boolean),
            Column('livingStatusDetail', Integer),
            Column('descriptionOfTrend', String(255)),
            Column('followUpDescription', DateTime),
            Column('isMarkedToDelet', Boolean),
            Column('satisfactionRate', Boolean)
#            Column('contact_type_lookup',UUIDType(binary=False), ForeignKey('contactTypeLookup.id'))
            )


class ApplicantCall(Mixin, Base):
    """User Table."""
    __tablename__ = "sawa_application_call_base"
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    callDate = Column(DateTime, nullable=False , default=datetime.datetime.utcnow)
    callEndDate = Column(DateTime, nullable=False)
    callName = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
#    contacts = relationship("AppContactMethod",backref="contactTypeLookup", order_by="appContactMethod.id")
    isViolance = Column(Boolean, nullable=True)
    isComplaintToPolice = Column(Boolean, nullable=True)
    employeeFollowName = Column(String, nullable=False )
    lastViewed =  Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    isExpired = Column(Boolean, nullable=False )
    isAttorneyGeneral = Column(Boolean, nullable=True )
    isSamePerson = Column(Boolean, nullable=True )
    personName = Column(String, nullable=False)
    callerComments = Column(String, nullable=True)
#    callerComments = Column(String, nullable=True)
    contactMethodDetail = Column(String, nullable=True)
    policeStationName = Column(String, nullable=True)
    investigatorName = Column(String, nullable=True)
    policeStationTel = Column(String, nullable=True)
    policeComplaintNo = Column(String, nullable=True)
    aggressorName = Column(String, nullable=True)
    policeComplaintDate = Column(String, nullable=True)
    attorneyGeneralName = Column(String, nullable=True)
    attorneyGeneralTel = Column(String, nullable=True)
    attorneyGeneralCompDate = Column(String, nullable=True)
    educationalStatusDetail = Column(String, nullable=True)
    livingStatusDetail = Column(String, nullable=True)
    descriptionOfTrend = Column(String, nullable=True)
    followUpDescription = Column(String, nullable=True)
    isMarkedToDelet = Column(String, nullable=True)
    satisfactionRate =   Column(String, nullable=True)
#   Employee  create by 
#   Employee  Update by 


applicantCallViolence = Table('sawa_applicant_call_violence', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('keyName', String(255)),
            Column('valueType', String(255)),
            Column('createDate', DateTime),
            Column('createBy', String(255)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class ApplicantCallViolence(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_applicant_call_violence"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keyName = Column(String, nullable=False)
    valueType = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

#   User Id
#   Applicant Id
#   Employee  create by 
#   Employee  Update by 

#   call id reference key 
#   ViolenceId reference key     

applicantComments = Table('sawa_applicant_comments', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('commentName', String(255)),
            Column('commentValue', String(255)),
            Column('commentDate', DateTime),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ApplicantComments(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_applicant_comments"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    commentName = Column(String, nullable=False)
    commentValue = Column(String, nullable=False)
    commentDate = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

#   User Id
#   Applicant Id
#   Employee  create by 
#   Employee  Update by 


applicantComments = Table('sawa_applicant_contact_method', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('contactMethod', String(255)),
            Column('contactValue', String(255)),
            Column('contactKey', DateTime),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class ApplicantContactMethod(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_applicant_contact_method"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    contactMethod = Column(String, nullable=False)
    contactValue = Column(String, nullable=False)
    contactKey = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

applicantFollowUp = Table('sawa_applicant_follow_up', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('employeeId', String(255)),
            Column('fromDate', String(255)),
            Column('toDate', DateTime),
            Column('isCurrent', DateTime),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ApplicantFollowUp(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_applicant_follow_up"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    employeeId = Column(String, nullable=False)
    fromDate = Column(String, nullable=False)
    toDate = Column(String, nullable=False)
    isCurrent = Column(Boolean, nullable=False) 
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

applicantStatus = Table('sawa_applicant_status', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('statusName', String(255)),
            Column('statusKey', String(255)),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ApplicantStatus(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_applicant_status"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    statusName = Column(String, nullable=False)
    statusKey = Column(String, nullable=False)
    createDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

area = Table('area_table_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('areaNam', String(255)),
            Column('enName', String(255)),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Area(Mixin, Base):
    """User Table."""

    __tablename__ = "area_table_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    areaName = Column(String, nullable=False)
    enName = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

article = Table('article_table_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('article', String(255)),
            Column('body', String(255)),
            Column('createDate', String(255)),
            Column('createBy', String(255)),
            Column('updateDate', String(255)),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Article(Mixin, Base):
    """User Table."""

    __tablename__ = "article_table_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    article = Column(String, nullable=False)
    body = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)




from sqlalchemy.dialects.mssql import IMAGE

articleAttachments = Table('sawa_article_attachments_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('articleSerial', String(255)),
            Column('subject', String(255)),
            Column('attachedFile', IMAGE),
            Column('fileName', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(255)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class ArticleAttachments(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_article_attachments_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articleSerial = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    attachedFile = Column(IMAGE, nullable=False)
    fileName = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


attendance = Table('sawa_attendance_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('typeId', String(255)),
            Column('inDate', DateTime),
            Column('outDate', DateTime),
            Column('employeeId', String(255)),
            Column('numberOfHours', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(255)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Attendance(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_attendance_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    typeId = Column(String, nullable=False)
    inDate = Column(DateTime, nullable=False)
    outDate = Column(DateTime, nullable=False)
    employeeId = Column(String, nullable=False)
    numberOfHours = Column(Integer, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

attendance = Table('sawa_blackList_phones', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('callDateTime', DateTime),
            Column('phoneNumber', String(64)),
            Column('comments', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(255)),
            Column('updateDate', DateTime),
            Column('updateBy', String(255)),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class BlackListPhones(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_blackList_phones"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    callDateTime = Column(DateTime, nullable=False)
    phoneNumber = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

# phobe Id reference key 
# CallDeleteRequest

callsLog = Table('sawa_call_logs_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('applicantId', String(255)),
            Column('keyCode', DateTime),
            Column('receipientId', DateTime),
            Column('startTime', DateTime),
            Column('endTime', DateTime),
            Column('isClosed', DateTime),
            Column('isBlackList', String(255)),
            Column('comments', String(255)),
            Column('createdBy', String(255)),

            Column('createdDate', DateTime),
            Column('lastModBy', String(255)),
            Column('isNoAnswer', String(255)),
            Column('isDisconnected', String(255))
            )

class CallsLog(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_call_logs_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    applicantId = Column(String, nullable=False)
    keyCode = Column(String, nullable=False)
    receipientId = Column(Boolean, nullable=True)
    startTime = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    endTime = Column(String, nullable=False)
    isClosed = Column(Integer, nullable=True , default=datetime.datetime.utcnow)
    isBlackList = Column(DateTime, nullable=True)
    comments = Column(String, nullable=True)

    createdBy = Column(String, nullable=True)
    createdDate = Column(DateTime, nullable=True)
    lastModBy = Column(String, nullable=True)

    lastModDate = Column(String, nullable=True)
    isNoAnswer = Column(DateTime, nullable=True)
    isDisconnected = Column(String, nullable=True)

# RuserId reference key 
chiCategories = Table('sawa_chi_categories_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('categoryId', String(255)),
            Column('parentId', UUIDType(binary=False)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))

            )

class CHICategories(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_chi_categories_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    categoryId = Column(String, nullable=False)
    parentId = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


complainantCategory = Table('sawa_complainant_category', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('catName', String(255)),
            Column('needMoreDetail', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))

            )

class ComplainantCategory(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_complainant_category"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    catName = Column(String, nullable=False)
    needMoreDetail = Column(String, nullable=False)
    categoryId = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

complaintType = Table('sawa_complaint_type', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))

            )

class ComplaintType(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_complaint_type"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

consultationObjective = Table('sawa_consultation_objective', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('prentId', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ConsultationObjective(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_consultation_objective"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    prentId = Column(UUIDType(binary=False), nullable = True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


contactInfo = Table('sawa_contact_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('fullName', String(255)),
            Column('displayName', String(255)),
            Column('email', String(128)),
            Column('mobile', String(64)),
            Column('mobile2', String(64)),
            Column('telePhone', String(64)),
            Column('telePhone1', String(64)),
            Column('telePhone2', String(64)),
            Column('fax', String(64)),
            Column('address', String(64)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ContactInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_contact_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    fullName = Column(String, nullable=True )
    displayName = Column(String, nullable=False)
    email = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    mobile = Column(String, nullable=True)
    mobile2 = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    telePhone = Column(String, nullable=True)
    telePhone1 = Column(String, nullable=True)
    telePhone2 = Column(String, nullable=True)
    extension = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    address = Column(String, nullable=True)
    extension = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    address = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

contactGroup = Table('sawa_contact_group', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('jobTitle', String(255)),
            Column('email', String(255)),
            Column('mobile', String(128)),
            Column('telePhone', String(64)),
            Column('extension', String(64)),
            Column('fax', String(64)),
            Column('comments', String(64)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ContactGroup(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_contact_group"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jobTitle = Column(String, nullable=True )
    email = Column(String, nullable=False)
    mobile = Column(String , nullable = False )
    telePhone = Column(String, nullable=True  )
    extension = Column(String, nullable=True  )
    fax = Column(String, nullable=True)
    comments = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


contactGroup = Table('sawa_contact_list', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ContactList(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_contact_list"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

contactGroup = Table('sawa_contact_method', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ContactMethod(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_contact_method"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

contactGroup = Table('sawa_conversion_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('applicantId', UUIDType(binary=False)),
            Column('contactId', UUIDType(binary=False)),
            Column('conversionDate', DateTime),
            Column('employeeId', UUIDType(binary=False)),
            Column('commentts', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Conversion(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_conversion_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    applicantId = Column(UUIDType(binary=False), nullable=True )
    contactId = Column(UUIDType(binary=False), nullable=True )
    conversionDate = Column(DateTime, nullable=True )
    employeeId = Column(UUIDType(binary=False), nullable=True )
    commentts = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

applicantCall = Table('sawa_cpwg_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('organization', String(255)),
            Column('acronym', String(255)),
            Column('typeO', String(255)),
            Column('implementingPartner', String(255)),
            Column('financing', String(128)),
            Column('needs', String(255)),
            Column('activity', String(255)),
            Column('descriptionO', String(255)),
            Column('governorate', String(255)),
            Column('municipality', String(255)),
            Column('typeoflocation', String(255)),
            Column('statusO', String(255)),
            Column('startDate', DateTime),
            Column('endDate', DateTime),
            Column('girlBeneficiaries', String(255)),
            Column('womanBeneficiaries', String(255)),
            Column('manBeneficiaries', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))


            )
class CPWG(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_cpwg_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    organization = Column(String, nullable=True )
    acronym = Column(String, nullable=True )
    typeO = Column(String, nullable=True )
    implementingPartner = Column(String, nullable=True )
    financing = Column(String, nullable=True )
    needs = Column(String, nullable=True )
    activity = Column(String, nullable=True )
    descriptionO = Column(String, nullable=True )
    governorate = Column(String, nullable=True )
    municipality = Column(String, nullable=True )
    typeoflocation = Column(String, nullable=True )
    statusO = Column(String, nullable=True )
    startDate = Column(DateTime, nullable=True )
    endDate = Column(DateTime, nullable=True )
    girlBeneficiaries = Column(String, nullable=True )
    boyBenefeciaries = Column(String, nullable=True )
    womanBeneficiaries = Column(String, nullable=False)
    manBeneficiaries = Column(String , nullable = False , default=datetime.datetime.utcnow)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

criminalSituation = Table('sawa_criminal_situation', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class CriminalSituation(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_criminal_situation"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

criminalSituation = Table('sawa_economic_situation', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class EconomicSituation(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_economic_situation"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


criminalSituation = Table('sawa_education_level', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createdDate', DateTime),
            Column('createBy', String(128)),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class EducationLevel(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_education_level"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

employee = Table('sawa_employee', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('employeeName', String(255)),
            Column('gender', DateTime),
            Column('maritalStatus', DateTime),
            Column('idCard', String(255)),
            Column('birthDate', DateTime),
            Column('mobileNo', String(255)),
            Column('telephoneNo', String(255)),

            Column('email', String(255)),
            Column('specialization', DateTime),
            Column('areaId', DateTime),
            Column('governerateId', String(255)),
            Column('locationId', DateTime),
            Column('comments', String(255)),
            Column('address', String(255)),

            Column('nikName', DateTime),
            Column('employeeNo', String(255)),
            Column('employeeNo', String(255)),

            )

class Employee(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_employee"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    employeeName = Column(String, nullable=True )
    gender = Column(String, nullable=False)
    maritalStatus = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    idCard = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    birthDate = Column(String, nullable=True)
    mobileNo = Column(String, nullable=True)
    telephoneNo = Column(String, nullable=True)
    email = Column(String, nullable=True )
    specialization = Column(String, nullable=False)
    areaId = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    governerateId = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    locationId = Column(String, nullable=True)
    comments = Column(String, nullable=True)
    address = Column(String, nullable=True)
    nikName = Column(String, nullable=True)
    employeeNo = Column(String, nullable=True)


governerate = Table('sawa_governerate', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            
            Column('enName', String(255)),
            Column('telCode', String(255)),

            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Governerate(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_governerate"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    enName = Column(String, nullable=False)
    telCode = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


group = Table('sawa_group', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('comments', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Group(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_group"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    comments = Column(String, nullable=False)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)



healthStatus = Table('sawa_health_status', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class HealthStatus(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_health_status"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

job = Table('sawa_job_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('title', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Job(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_job_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

keyCodeSequence = Table('sawa_code_sequence', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('currentSequence', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class KeyCodeSequence(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_code_sequence"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    currentSequence = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


language = Table('sawa_language_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('language', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class Language(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_language_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    language = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

livingConditions = Table('sawa_living_conditions', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('livingCondition', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class LivingConditions(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_living_conditions"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    livingCondition = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

location = Table('sawa_location_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('governerateId', String(255)),

            Column('placeType', String(255)),
            Column('telCode', String(255)),

            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Location(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_location_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    governerateId = Column(String, nullable=True )
    placeType = Column(String, nullable=True )
    telCode = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

location = Table('sawa_login_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('userId', String(64)),

            Column('loginDate', DateTime),
            Column('logoutDate', DateTime),
            
            Column('ipAddress', String(128)),
            Column('hostName', String(128)),

            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class LoginInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_login_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    userId = Column(String, nullable=True )
    loginDate = Column(String, nullable=True )
    logoutDate = Column(String, nullable=True )
    ipAddress = Column(String, nullable=True )
    hostName = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


maritalStatus = Table('sawa_marital_status', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('status', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class MaritalStatus(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_marital_status"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    status = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

messageReceipent = Table('sawa_message_receipent', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('category', String(255)),
            Column('isRemoved', Boolean),
            Column('isRead', Boolean),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class MessageReceipent(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_message_receipent"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    category = Column(String, nullable=True )
    isRemoved = Column(Boolean, nullable=True )
    isRead = Column(Boolean, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

from sqlalchemy.dialects.mssql import TEXT

msg = Table('sawa_message_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('messageDate', String(255)),
            Column('messageTitle', String(255)),
            Column('messageBody', TEXT),
            Column('fromUser', String(128)),
            Column('toUserString', String(128)),
            Column('ccString', TEXT),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class Msg(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_message_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    messageDate = Column(String, nullable=False )
    messageTitle = Column(String, nullable=False )
    messageBody = Column(String, nullable=False )
    fromUser = Column(String, nullable=False )
    toUserString = Column(String, nullable=False )
    ccString = Column(String, nullable=False )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


nationality = Table('sawa_nationality_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('status', String(255)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Nationality(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_nationality_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

newLocation = Table('sawa_new_location_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('codeLocation', String(128)),   
            Column('goveCode', String(128)),
            Column('ABCCat', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class NewLocation(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_new_location_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    codeLocation = Column(String, nullable=True )
    goveCode = Column(String, nullable=True )
    ABCCat = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

periodAccComp = Table('sawa_period_acc_comp', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('exactDate', DateTime),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class PeriodAccComp(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_period_acc_comp"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    exactDate = Column(DateTime, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

permssion = Table('sawa_permssion_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('permissionName', String(64)),
            Column('internalId', DateTime),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Permssion(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_permssion_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    permissionName = Column(String, nullable=True )
    internalId = Column(String , nullable = False )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

physicalViolance = Table('sawa_physical_violance', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class PhysicalViolance(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_physical_violance"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


place = Table('sawa_place_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Place(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_place_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

placeLiving = Table('sawa_place_living', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class PlaceLiving(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_place_living"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    
psychologicalViolence = Table('sawa_psychological_violence', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class PsychologicalViolence(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_psychological_violence"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

refferedOrganization = Table('sawa_reffered_organization', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('orgName', String(64)),
            Column('orgType', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )


class RefferedOrganization(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_reffered_organization"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    orgName = Column(String, nullable=True )
    orgType = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)



refferedOrganizationType = Table('sawa_reffered_organization_type', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('orgName', String(64)),
            Column('needOrgDetail', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class RefferedOrganizationType(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_reffered_organization_type"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    orgName = Column(String, nullable=True )
    needOrgDetail = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

relationViolent = Table('sawa_relation_violent', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class RelationViolent(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_relation_violent"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


sexualViolence = Table('sawa_sexual_violence', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class SexualViolence(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_sexual_violence"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

socialSituation = Table('sawa_social_situation', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class SocialSituation(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_social_situation"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

specialization = Table('sawa_specialization_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('title', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Specialization(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_specialization_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

topic = Table('sawa_topic_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('topicName', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Topic(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_topic_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    topicName = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


trainingCourse = Table('sawa_training_course', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('trainingRefNo', String(255)),
            Column('trainingTitle', String(255)),
            Column('mainPlace', String(255)),
            Column('startDate', DateTime),
            Column('endDate', DateTime),
            Column('isEnded', Boolean),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class TrainingCourse(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_training_course"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    trainingRefNo = Column(String, nullable=False )
    trainingTitle = Column(String, nullable=False )
    mainPlace = Column(String, nullable=False )
    startDate = Column(DateTime, nullable=False )
    endDate = Column(DateTime, nullable=False )
    isEnded = Column(Boolean, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    
trainingType = Table('sawa_training_type', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('courseType', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class TrainingType(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_training_type"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    courseType = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

trainingCourse = Table('sawa_training_session', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('sessionRefNo', String(255)),
            Column('sessionTitle', String(255)),
            Column('mainPlace', String(255)),
            Column('startDate', DateTime),
            Column('endDate', DateTime),
            Column('isEnded', Boolean),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class TrainingSession(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_training_session"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    sessionRefNo = Column(String, nullable=False )
    sessionTitle = Column(String, nullable=False )
    mainPlace = Column(String, nullable=False )
    startDate = Column(DateTime, nullable=False )
    endDate = Column(DateTime, nullable=False )
    isEnded = Column(Boolean, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

userInfo = Table('sawa_user_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('userName', String(64)),
            Column('fullName', String(255)),
            Column('englishName', String(255)),
            Column('password', String(255)),
            Column('isActive', Boolean),
            Column('isCurrentlyLogon', Boolean),
            Column('lastLoginDate', DateTime),
            Column('lastLogoutDate', DateTime),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class UserInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_user_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    userName = Column(String, nullable=False )
    fullName = Column(String, nullable=False )
    englishName = Column(String, nullable=False )
    password = Column(String, nullable=False )
    isActive = Column(Boolean, nullable=False )
    isCurrentlyLogon = Column(Boolean, nullable=True )
    lastLoginDate = Column(DateTime, nullable=True )
    lastLogoutDate = Column(Boolean, nullable=True )
    employeeId = Column(UUIDType(binary=False), nullable=True )
    employeeNo = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

violence = Table('sawa_violence_info', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(255)),
            Column('englishName', String(255)),
            Column('parentId', UUIDType(binary=False)),
            Column('isMainCategory', Boolean),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class Violence(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_violence_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False )
    englishName = Column(String, nullable=False )
    parentId = Column(UUIDType(binary=False), nullable=True )
    isMainCategory = Column(DateTime, nullable=False )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)




violenceTools = Table('sawa_violence_tools', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('name', String(64)),
            Column('createBy', String(128)),
            Column('createDate', DateTime),
            Column('updateDate', String(255)),
            Column('updateBy', DateTime),
            Column('description', String(255)),
            Column('notes', String(255))
            )

class ViolenceTools(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_violence_tools"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


voipSettings = Table('sawa_voip_settings', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('sipPort', Integer),
             Column('rtpPort', Integer),
             Column('audioCodecs', String(255)),
             Column('useNATAddr', Boolean),
             Column('displayName', String(64)),
             Column('userName', String(64)),
             Column('domain', String(64)),
             Column('proxy', String(64)),
             Column('password', String(64)),
             Column('dnd', String(64)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )

class VOIPSettings(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_voip_settings"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    sipPort = Column(Integer, nullable=True )
    rtpPort = Column(Integer, nullable=True )
    audioCodecs = Column(String, nullable=True )
    useNATAddr = Column(Boolean, nullable=True )
    displayName = Column(String, nullable=True )
    userName = Column(String, nullable=True )
    domain = Column(Boolean, nullable=True )
    displayName = Column(Integer, nullable=True )
    proxy = Column(String, nullable=True )
    password = Column(String, nullable=True )
    dnd = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

volunteer = Table('sawa_volunteer_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('volunteerCode', String(255)),
             Column('name', String(255)),
             Column('idCard', String(128)),
             Column('birthDate', DateTime),
             Column('mobileNo', String(64)),
             Column('telephoneNo', String(64)),
             Column('email', String(64)),
             Column('specialization', String(255)),
             Column('comments', String(255)),
             Column('address', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )

class Volunteer(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_volunteer_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    volunteerCode = Column(String, nullable=True )
    name = Column(String, nullable=True )
    idCard = Column(String, nullable=True )
    birthDate = Column(DateTime, nullable=True )
    mobileNo = Column(String, nullable=True )
    telephoneNo = Column(String, nullable=True )
    email = Column(String, nullable=True )
    specialization = Column(String, nullable=True )
    comments = Column(String, nullable=True )
    address = Column(String, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)




volunteerHours = Table('sawa_volunteer_hours', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('attendanceDate', DateTime),
             Column('startTime', DateTime),
             Column('endDate', DateTime),
             Column('comments', DateTime),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )

class VolunteerHours(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_volunteer_hours"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    attendanceDate = Column(DateTime, nullable=True )
    startTime = Column(DateTime, nullable=True )
    endDate = Column(DateTime, nullable=True )
    comments = Column(DateTime, nullable=True )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)


mainLokupTools = Table('sawa_main_lookup_tools', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('parentVal', String(128)),
             Column('catVal', String(128)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )






import json


class MainLokupTools(Mixin,Base):
    """User Table."""

    __tablename__ = "sawa_main_lookup_tools"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    parentVal = Column(String, nullable=True )
    catVal = Column(String, nullable=False )
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow())
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow())
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    def to_json(self):
        return json.dumps(self.__dict__)


class LookupDto(object):
    

    id =''
    parentVal =''
    catVal =''
    createBy =''
    createdDate =''
    updateDate =''
    updateBy =''
    description =''
    notes =''

    def __init__(self , id , parentVal , catVal , createBy , createdDate , updateDate , updateBy , description , notes):
        self.id = id
        self.parentVal = parentVal
        self.catVal = catVal
        self.createBy = createBy
        self.createdDate = createdDate
        self.updateDate = updateDate
        self.updateBy = updateBy
        self.description = description
        self.notes = notes

class FinalDto(object):
    

    id =''
    catVal =''

    def __init__(self , id , catVal):
        self.id = id
        self.catVal = catVal
        
class LookupDtos(object):
   

    dtos = []
    
    def __init__(self, dtos ):
        self.dtos = dtos

callerInfo = Table('sawa_caller_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('idNumber', String(255)),
             Column('fullName', String(255)),
             Column('realationShip', String(255)),
             Column('communicateType', String(255)),
             Column('descriptionInfo', String(255)),
             Column('nextStep', String(255)),
             Column('description1', String(255)),
             Column('description2', String(255)),
             Column('description3', String(255)),

             Column('lastStep', String(255)),
             Column('description', String(255)),
             Column('notes', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )

class CallerInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_caller_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    idNumber = Column(String, nullable=False)
    fullName = Column(String, nullable=False)
    realationShip = Column(String, nullable=False)
    communicateType = Column(String, nullable=False)
    nextStep = Column(String, nullable=True)
    sameCaller = Column(String, nullable=True)
    lastStep = Column(String, nullable=True)
    descriptionInfo = Column(String, nullable=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    description3 = Column(String, nullable=True)
    personName = Column(String, nullable=True)
    notesInfo = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
    parent = relationship('BaseSawaBooks'  , back_populates="types" , primaryjoin = "BaseSawaBooks.id == CallerInfo.type_id ")



recCallerInfo = Table('sawa_rec_caller_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('firstPerson', String(255)),
             Column('secondPersonName', String(255)),
             Column('basedDate', String(255)),
             Column('startTime', String(255)),
             Column('endTime', String(255)),
             Column('lastStep', String(255)),
             Column('description', String(255)),
             Column('notes', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )


class RecCallerInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_rec_caller_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    firstPerson = Column(String, nullable=False)
    secondPersonName = Column(String, nullable=False)
    basedDate = Column(String, nullable=False)
    startTime = Column(String, nullable=False)
    endTime = Column(String, nullable=True)
    descriptionInfo = Column(String, nullable=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    description3 = Column(String, nullable=True)
    personName = Column(String, nullable=True)
    notesInfo = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
    parent = relationship('BaseSawaBooks'  , back_populates="calls" , primaryjoin = "BaseSawaBooks.id == RecCallerInfo.type_id ")



caseChildsInfo = Table('sawa_child_case_situation_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('situationSelected', String(255)),
             Column('livesWith', String(255)),
             Column('textDescription', String(255)),
             Column('description1', String(255)),
             Column('description2', String(255)),
             Column('description3', String(255)),
             Column('description', String(255)),
             Column('notes', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )


class CaseChildsInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_child_case_situation_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    situationSelected = Column(String, nullable=False)
    livesWith = Column(String, nullable=False)
    textDescription = Column(String, nullable=False)
    descriptionInfo = Column(String, nullable=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    description3 = Column(String, nullable=True)
    notesInfo = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
    parent = relationship('BaseSawaBooks'  , back_populates="casess" , primaryjoin = "BaseSawaBooks.id == CaseChildsInfo.type_id ")


caseVolianceInfo = Table('sawa_voliance_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('volianceRelated', String(255)),
             Column('caseType', String(255)),
             Column('socialSituation', String(255)),
             Column('econmySituation', String(255)),
             Column('voliancePlace', String(255)),
             Column('period', String(255)),
             Column('description1', String(255)),
             Column('description2', String(255)),
             Column('description3', String(255)),
             Column('description', String(255)),
             Column('notes', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )

class CaseVolianceInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_voliance_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    volianceRelated = Column(String, nullable=False)
    caseType = Column(String, nullable=False)
    socialSituation = Column(String, nullable=False)
    econmySituation = Column(String, nullable=True)
    voliancePlace = Column(String, nullable=True)
    period = Column(String, nullable=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    description3 = Column(String, nullable=True)
    notesInfo = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
    parent = relationship('BaseSawaBooks'  , back_populates="voliances" , primaryjoin = "BaseSawaBooks.id == CaseVolianceInfo.type_id ")



casePoliceInfo = Table('sawa_police_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('callPolice', String(255)),
             Column('policecenter', String(255)),
             Column('policenumber', String(255)),
             Column('fileNumber', String(255)),
             Column('volPerson', String(255)),
             Column('callPoliceDate', String(255)),
             Column('description1', String(255)),
             Column('description2', String(255)),
             Column('description3', String(255)),
             Column('description', String(255)),
             Column('notes', String(255)),
             Column('createBy', String(128)),
             Column('createDate', DateTime),
             Column('updateDate', String(255)),
             Column('updateBy', DateTime),
             Column('description', String(255)),
             Column('notes', String(255))
            )


class CasePoliceInfo(Mixin, Base):
    """User Table."""

    __tablename__ = "sawa_police_info"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    callPolice = Column(String, nullable=False)
    policecenter = Column(String, nullable=False)
    policenumber = Column(String, nullable=False)
    fileNumber = Column(String, nullable=True)
    volPerson = Column(String, nullable=True)
    callPoliceDate = Column(String, nullable=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    description3 = Column(String, nullable=True)
    notesInfo = Column(String, nullable=True)
    createBy = Column(String, nullable=False)
    createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
    updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
    updateBy = Column(String, nullable=True)
    description = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
    parent = relationship('BaseSawaBooks'  , back_populates="polices" , primaryjoin = "BaseSawaBooks.id == CasePoliceInfo.type_id")



caseCatogriesKeywords = Table('sawa_cat_keywords_info', metadata,
             Column('id', UUIDType(binary=False) , primary_key=True),
             Column('parent', String(255)),
             Column('options', String(255)),
             Column('policenumber', String(255))
            )

class CaseCatogriesKeywords(Mixin, Base):
      """User Table."""

      __tablename__ = "sawa_cat_keywords_info"

      id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
      parent = Column(String, nullable=False)
      options = Column(String, nullable=False)
      keywords = Column(String, nullable=False)
      createBy = Column(String, nullable=False)
      createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
      updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
      updateBy = Column(String, nullable=True)

class BaseBookDto(object):

    idCard =''
    fullName =''
    socialName =''
    economySitutation =''
    healthSituation =''
    ageViolance = ''

    def __init__(self , idCard , fullName , socialName , economySitutation , healthSituation , ageViolance):

        self.idCard = idCard
        self.fullName = fullName
        self.socialName = socialName
        self.economySitutation = economySitutation
        self.healthSituation = healthSituation
        self.ageViolance = ageViolance