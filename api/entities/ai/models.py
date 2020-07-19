from api.core import Mixin
from ...db import db  

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from ...db import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
Base = declarative_base()
class ArticalInfo(Mixin , Base):
    """description of class"""


    __tablename__ = 'atifical_ai'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= Column(String , nullable=False)
    writtenDate= Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column(Boolean , nullable = False , default = False)
    autherCode = Column(String , nullable = False , unique=True)
    autherName = Column(String , nullable = False)
    articalCode= Column(String , nullable = False , unique=True)
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    publishDate = Column (DateTime, nullable = False)
    publishingHouse = Column (String , nullable = False)




