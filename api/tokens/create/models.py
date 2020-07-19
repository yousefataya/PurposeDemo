from api.core import Mixin
from ...db import db  
from sqlalchemy_utils import UUIDType

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapper
Base = declarative_base()

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
metadata = MetaData()

userToken = Table('user_tokens_auths', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('email', String(255)),
            Column('password', String(255)),
            Column('first_name', String(255)),
            Column('last_name', String(255)),
            Column('login', String(128)),
            
            Column('age', Integer),
            Column('street', String(255)),
            Column('city', String(255)),
            Column('zip', String(255))
            )

class UserToken(Mixin, Base):
    """User Table."""

    __tablename__ = "user_tokens_auths"

    id = Column(Integer, unique=True, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    first_name = Column(String, nullable=False, default='')
    last_name = Column(String, nullable=False, default='')
    login = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    street = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip = Column(String, nullable=True)

    def __init__(self, email, password, name):
        if name:
            res = name.split(' ')
            self.first_name = '' if len(res) == 1 else res[0]
            self.last_name = res[0] if len(res) == 1 else ' '.join(res[1:])
        self.last_name = None
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"



import uuid
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy_utils import UUIDType
import datetime
import uuid


opsBaseRole = Table('operations_based_role', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('operationName', String(255)),
            Column('createDate', DateTime),
            Column('description', String(255)),
            Column('isExpired', Boolean),
            Column('userCode', String(128)),
            Column('operationCode', String(255)),
            Column('isResereved', Boolean),
            Column('reserevedBy', String(255)),
            Column('isAllow', Boolean),
            Column('isPermit', Boolean)
            )


class OperationJwtAllowed(Mixin , Base):
    """description of class"""
    __tablename__ = 'operations_based_role'

    id =  Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    operationName=  Column( String , nullable=False)
    createDate=  Column( DateTime , nullable = False , default=datetime.datetime.utcnow)
    description =  Column( String , nullable = True)
    notes =  Column ( String , nullable = True)
    isExpired =  Column( Boolean , nullable = False , default = False)
    userCode =  Column( String , nullable = False )
    userName =  Column( String , nullable = False)
    operationCode=  Column( String , nullable = False )
    isResereved =  Column ( String , nullable = False , default = False )
    reserevedBy =  Column ( String , nullable = False)
    isAllow =  Column ( Boolean, nullable = False)
    isPermit =  Column ( Boolean , nullable = False)



from api.core import Mixin
from sqlalchemy_utils import UUIDType
import datetime
urlsPatterns = Table('url_patterns_auth', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('urlLink', String(255)),
            Column('createDate', DateTime),
            Column('Description', String(255)),
            Column('isExpired', Boolean),
            Column('controller', String(128)),
            Column('method', String(255)),
            Column('notes', Boolean)
            )
class UrlsPatterns(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'url_patterns_auth'

    id =  Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    urlLink =  Column ( String , nullable = False)
    createdDate =  Column( DateTime ,  nullable = False , default=datetime.datetime.utcnow)
    isExpired =  Column( Boolean , nullable = False , default = False)
    controller=  Column ( String , nullable = False)
    method=  Column ( String , nullable = False)
    Description=  Column( String , nullable = True)
    notes =  Column( String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
jwtTokenCronJob = Table('token_jwt_cron_jobs', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('jobName', String(255)),
            Column('JobCode', DateTime),
            Column('startDate', DateTime),
            Column('status', Boolean),
            Column('createdDate', DateTime),
            Column('cronExpression', String(128))
            )
class JwtTokenCronJob(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'token_jwt_cron_jobs'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jobName= Column(String , nullable = False)
    JobCode = Column (String , nullable = False )
    startDate = Column( DateTime , nullable = False)
    status= Column( Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False)
    cronExpression=Column ( String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
jwtTokenLookup = Table('token_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('lookupKey', String(128)),
            Column('lookupValue', String(128))
            )
class JwtTokenLookup(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'token_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
import datetime
jwtUserHistory = Table('jwt_user_history', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('jwtName', String(255)),
            Column('jwtCode', DateTime),
            Column('jwtKey', DateTime),
            Column('status', Boolean),
            Column('createdDate', DateTime),
            Column('Description', String(255)),
            Column('Notes', String(255))
             )
class JwtUserHistory(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'jwt_user_history'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtName= Column(String , nullable = False)
    jwtCode = Column (String , nullable = False )
    jwtKey = Column( DateTime , nullable = False)
    status= Column( Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
jwtTransactionLookup = Table('transaction_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('lookupKey', String(128)),
            Column('lookupValue', String(128))
            )
class JwtTransactionLookup(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'transaction_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import uuid
import datetime
from sqlalchemy.ext.automap import automap_base
jwtHistoryToken = Table('transaction_history_token', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('jwtCode', String(255)),
            Column('jwtDate', DateTime),
            Column('description', String(255)),
            Column('notes', String(255)),
            Column('isExpired', Boolean),
            Column('jwtName', String(255)),
            Column('jwtKey', String(255)),
            Column('jwtOperationName', String(255)),
            Column('isResereved', Boolean),
            Column('operationCode', String(128)),
            Column('operationGuid', String(128))
             )
class JwtHistoryToken(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'transaction_history_token'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtCode= Column(String , nullable=False)
    jwtDate= Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column( Boolean , nullable = False , default = False)
    jwtName = Column(String , nullable = False )
    jwtKey = Column(String , nullable = False)
    jwtOperationName= Column(String , nullable = False)
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    operationCode = Column (DateTime, nullable = False)
    operationGuid = Column (String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
jwtTokenSignatureLookup = Table('jwt_token_signature_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('lookupKey', String(128)),
            Column('lookupValue', String(128))
            )
class JwtTokenSignatureLookup(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'jwt_token_signature_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import datetime
import uuid
jwtTokenSignature = Table('jwt_token_signature', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('signatureName', String(255)),
            Column('signCode', String(255)),
            Column('signKey', String(255)),
            Column('status', Boolean),
            Column('createdDate', DateTime),
            Column('Description', String(255)),
            Column('Notes', String(255))
             )
class JwtTokenSignature(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'jwt_token_signature'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    signatureName= Column(String , nullable = False)
    signCode = Column (String , nullable = False )
    signKey = Column( String , nullable = False)
    status= Column( Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.automap import automap_base
from sqlalchemy_utils import UUIDType
import datetime
import uuid
jwtTokenTransactions = Table('jwt_token_transaction', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('tansactionCode', String(255)),
            Column('tansactionKey', String(255)),
            Column('createdDate', DateTime),
            Column('Description', String(255)),
            Column('Notes', String(255))
             )
class JwtTokenTransactions(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'jwt_token_transaction'
    def __init__(self, tag_text):
       """description of class"""
       
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    tansactionCode= Column(String , nullable = False)
    tansactionKey = Column (String , nullable = False )
    status= Column( Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import datetime
import uuid
from sqlalchemy.ext.automap import automap_base
jwtTokenExpire = Table('token_jwt_expire', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('jwtCode', String(255)),
            Column('createdDate', DateTime),
            Column('isExpired', Boolean),
            Column('Description', String(255)),
            Column('Notes', String(255))
             )
class JwtTokenExpire(Mixin ,  Base):
    
    def __init__(self, tag_text):
       """description of class"""
      
    __tablename__ = 'token_jwt_expire'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtCode = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column( Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)
from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import datetime
import uuid
from sqlalchemy.ext.automap import automap_base
jwtTokenExpireLookup = Table('token_jwt_expire_lookup', metadata,
            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('keywork', String(255)),
            Column('createdDate', DateTime),
            Column('isExpired', Boolean),
            Column('Description', String(255)),
            Column('Notes', String(255))
             )
class JwtTokenExpireLookup(Mixin ,  Base):
    """description of class"""
    __tablename__ = 'token_jwt_expire_lookup'
    def __init__(self, tag_text):
       """description of class"""
       


    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column( Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
import uuid
from sqlalchemy_utils import UUIDType
import datetime
from sqlalchemy.ext.automap import automap_base
class JwtTokenPermit(Mixin ,  Base):
    """description of class"""
     
    def __init__(self, tag_text):
       """description of class"""
      
    __tablename__ = 'jwt_token_permit'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    permitCode = Column (String , nullable = False)
    permitName = Column (String , nullable = False)
    permitKey = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column( Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)


Table('sawa_ps_bok_table', metadata,

            Column('id', UUIDType(binary=False) , primary_key=True),
            Column('permitCode', String(255)),
            Column('createdDate', DateTime),
            Column('isExpired', Boolean),
            Column('Description', String(255)),
            Column('notes', String(255)),
            Column('name', String(255)),
            Column('nickName', String(255)),
            Column('roles', String(255)),
            Column('age', Integer),
            Column('gender', String(255)),
            Column('state', String(255)),
            Column('desiredPlace', String(255)),
            Column('placeCompany', String(255)),
            Column('publicReputation', String(255)),
            Column('caseType', String(255)),
            Column('currentCareer', String(255)),

            Column('socialSituations', String(255)),
            Column('economySitutation', String(255)),
            Column('healthSituation', String(255)),
            Column('nationality', String(255)),
            Column('personLanguage', String(255)),
            Column('ageViolance', Integer),
            Column('fullName', String(255)),
            Column('idNumber', Integer),
            Column('association', String(255)),
            Column('medicalConsultation', Boolean),
            Column('inquiriesDiseases', Boolean),
            Column('hospitalAdmission', Boolean),
            Column('healthCare', Boolean),
            Column('selfHarming', Boolean),
            Column('secretsDisclosure', Boolean),
            Column('depression', Boolean),
            Column('suicide', Boolean),
            Column('obsessive', Boolean),
            Column('stealing', Boolean),
            Column('nervousness', Boolean),
            Column('schizophrenia', Boolean),
            Column('fear', Boolean),
            Column('lying', Boolean),
            Column('adolescence', Boolean),
            Column('psychologicalDischarge', Boolean),
            Column('boredom', Boolean),
            Column('lifeEnd', Boolean),
            Column('peeReflex', Boolean),
            Column('LowSelfEsteem', Boolean),
            Column('threat', Boolean),
            Column('deathThreat', Boolean),
            Column('control', Boolean),
            Column('economicDeprivation', Boolean),
            Column('nailBiting', Boolean),
            Column('nightmares', Boolean),
            Column('speechProblems', Boolean),
            Column('helpThanks', Boolean),
            Column('line', Boolean),
            Column('volunteer', Boolean),
            Column('helpChildern', Boolean),
            Column('professional', Boolean),
        )


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
import uuid
from sqlalchemy_utils import UUIDType
import datetime
from sqlalchemy.ext.automap import automap_base
from api.entities.sawa.models import CallerInfo
class BaseSawaBooks(Mixin , Base):
    """description of class"""
    __tablename__ = 'sawa_ps_bok_table'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    permitCode = Column (String , nullable = True)
    permitName = Column (String , nullable = True)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column( Boolean , nullable = True , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)
    name= Column(String , nullable = True);
    nickName = Column(String , nullable = True);
    roles = Column(String , nullable = True);
    age = Column( Integer , nullable = True);
    gender = Column(String , nullable = True);
    location = Column(String , nullable = True);
    state = Column(String , nullable = True);
    desiredPlace = Column(String , nullable = True);
    placeCompany = Column(String , nullable = True);
    publicReputation = Column(String , nullable = True);
    caseType = Column(String , nullable = True);
    currentCareer = Column(String , nullable = True);
    socialSituations = Column(String , nullable = True);
    economySitutation = Column(String , nullable = True);
    healthSituation = Column(String , nullable = True);
    nationality = Column(String , nullable = True);
    personLanguage = Column(String , nullable = True);
    ageViolance = Column( Integer , nullable = True);
    fullName = Column(String , nullable = True);
    idNumber = Column(String , nullable = True);
    association = Column(String , nullable = True);
    adolescence = Column( Boolean , nullable = True , default = False)
    
    subCatogries = Column( String , nullable = True , default = False)
    types = relationship('CallerInfo', back_populates="parent", lazy='dynamic' )
    calls = relationship('RecCallerInfo', back_populates="parent", lazy='dynamic' )
    casess = relationship('CaseChildsInfo', back_populates="parent", lazy='dynamic' )
    voliances = relationship('CaseVolianceInfo', back_populates="parent", lazy='dynamic' )
    polices = relationship('CasePoliceInfo', back_populates="parent", lazy='dynamic' )
    notes = relationship('MainFormNotes', back_populates="parent", lazy='dynamic' )

#    medicalConsultation = Column( Boolean , nullable = True , default = False)
#    inquiriesDiseases = Column( Boolean , nullable = True , default = False)
#    hospitalAdmission = Column( Boolean , nullable = True , default = False)
#    healthCare = Column( Boolean , nullable = True , default = False)
#    selfHarming = Column( Boolean , nullable = True , default = False)
#    secretsDisclosure = Column( Boolean , nullable = True , default = False)
#    depression = Column( Boolean , nullable = True , default = False)
#    suicide = Column( Boolean , nullable = True , default = False)
#    obsessive = Column( Boolean , nullable = True , default = False)
#    stealing = Column( Boolean , nullable = True , default = False)
#    nervousness = Column( Boolean , nullable = True , default = False)
#    schizophrenia = Column( Boolean , nullable = True , default = False)
#    fear = Column( Boolean , nullable = True , default = False)
#    lying = Column( Boolean , nullable = True , default = False)
#    adolescence = Column( Boolean , nullable = True , default = False)
#    psychologicalDischarge = Column( Boolean , nullable = True , default = False)
#    boredom = Column( Boolean , nullable = True , default = False)
#    lifeEnd = Column( Boolean , nullable = True , default = False)
#    peeReflex = Column( Boolean , nullable = True , default = False)
#    LowSelfEsteem = Column( Boolean , nullable = True , default = False)
#    threat = Column( Boolean , nullable = True , default = False)
#    deathThreat = Column( Boolean , nullable = True , default = False)
#    economicDeprivation = Column( Boolean , nullable = True , default = False)
#    control = Column( Boolean , nullable = True , default = False)
#    nailBiting = Column( Boolean , nullable = True , default = False)
#    nightmares = Column( Boolean , nullable = True , default = False)
#    speechProblems = Column( Boolean , nullable = True , default = False)
#    helpThanks  = Column( Boolean , nullable = True , default = False)
#    line  = Column( Boolean , nullable = True , default = False)
#    volunteer = Column(Boolean , nullable = True , default = False);
#    helpChildern = Column(Boolean , nullable = True , default = False );
#    professional = Column(Boolean , nullable = True , default = False);

#mapper(BaseSawaBooks, sawaTableBook)
#mapper(UrlsPatterns , urlsPatterns)
#mapper(JwtTokenCronJob , jwtTokenCronJob)
#mapper(JwtTokenLookup , jwtTokenLookup)
#mapper(JwtUserHistory , jwtUserHistory)
#mapper(JwtTransactionLookup , jwtTransactionLookup)
#mapper(JwtHistoryToken , jwtHistoryToken)
#mapper(JwtTokenSignatureLookup , jwtTokenSignatureLookup)
#mapper(JwtTokenSignature , jwtTokenSignature)
#mapper(JwtTokenTransactions , jwtTokenTransactions)
#mapper(JwtTokenExpire , jwtTokenExpire)
#mapper(JwtTokenExpireLookup , jwtTokenExpireLookup)
#mapper(UserToken , userToken)
#mapper(OperationJwtAllowed,opsBaseRole)

class MainFormNotes(Mixin, Base):
      """User Table."""

      __tablename__ = "sawa_main_form_notes_info"

      id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
      componentName = Column(String, nullable=False)
      valueTxT = Column(String, nullable=False)
      txtNotes = Column(String, nullable=False)
      createBy = Column(String, nullable=False)
      createdDate = Column(DateTime , nullable = False , default=datetime.datetime.utcnow)
      updateDate = Column(DateTime, nullable=True , default=datetime.datetime.utcnow)
      updateBy = Column(String, nullable=True)
      description = Column(String, nullable=True)
      notes = Column(String, nullable=True)
      type_id = Column(UUIDType(binary=False), ForeignKey("sawa_ps_bok_table.id"))
      parent = relationship('BaseSawaBooks'  , back_populates="notes" , primaryjoin = "BaseSawaBooks.id == MainFormNotes.type_id")