from api.core import Mixin
from ..db import db  

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Mixin, Base):
    """User Table."""

    __tablename__ = "user_info"

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
import uuid
class ArticalInfo(Mixin , Base):
    """description of class"""
    __tablename__ = 'images_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= Column(String , nullable=False)
    writtenDate= Column(DateTime , nullable = False)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column(Boolean , nullable = False , default = False)
    autherCode = Column(String , nullable = False )
    autherName = Column(String , nullable = False)
    articalCode= Column(String , nullable = False )
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    publishDate = Column (DateTime, nullable = False)
    publishingHouse = Column (String , nullable = False)

from api.core import Mixin
from sqlalchemy_utils import UUIDType
class Urls(Mixin , Base):
    """description of class"""
    __tablename__ = 'url_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    urlLink = Column (String , nullable = False)
    createdDate = Column(DateTime ,  nullable = False)
    isExpired = Column(Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
class CronJob(Mixin , Base):
    """description of class"""
    __tablename__ = 'cron_job_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jobName= Column(String , nullable = False)
    JobCode = Column (String , nullable = False )
    startDate = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False)
    cronExpression=Column ( String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class JobLookup(Mixin , Base):
    """description of class"""
    __tablename__ = 'cron_job_lookup'
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
class FetchNewsEntity(Mixin , Base):
    """description of class"""
    __tablename__ = 'fetch_api_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    newsName= Column(String , nullable = False)
    newsTitle = Column (String , nullable = False )
    newsText = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType

class NewsLookupEntity(Mixin , Base):
    """description of class"""
    __tablename__ = 'asl_lookup'
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

class ArticalHistoryInfo(Mixin , Base):
    """description of class"""
    __tablename__ = 'transaction_history_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= Column(String , nullable=False)
    writtenDate= Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    autherCode = Column(String , nullable = False)
    autherName = Column(String , nullable = False)
    articalCode = Column(String , nullable = False )
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    publishDate = Column (DateTime, nullable = False)
    publishingHouse = Column (String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
#Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class HistoryLookupEntity(Mixin , Base):
    """description of class"""
    __tablename__ = 'history_lookup'
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
class HistoryNewsInfo(Mixin ,Base):
    """description of class"""
    __tablename__ = 'history_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    newsName= Column(String , nullable = False)
    newsTitle = Column (String , nullable = False )
    newsText = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
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
class ImageEntity(Mixin , Base):
    """description of class"""
    __tablename__ = 'image_history'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    imageName= Column(String , nullable = False)
    imageTitle = Column (String , nullable = False )
    status= Column(db.Boolean , nullable = False , default = False)
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
class TopicInfo(Mixin , Base):
    """description of class"""
    __tablename__ = 'text_to_asl_lookup'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
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
class EntityKeywordsInfo(Mixin , Base):
    """description of class"""
    __tablename__ = 'keyword_lookup'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
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
class SubjectInfo(Mixin , Base):
    """description of class"""
    __tablename__ = 'subject_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)