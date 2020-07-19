import django
django.setup()

from api.entities.sawa.models import * 


from django.contrib import admin
from api.tokens.create.models import MainFormNotes


from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.utils.crypto import get_random_string
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.logger import create_app
from api.db import db
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields 
from flask_jwt_extended import get_jwt_identity
from api.tokens.create.models import BaseSawaBooks
from api.entities.services import get_user_by_id, update_user
from api.core import validate_json_body
import json
from json import JSONEncoder
bp = Blueprint('user', __name__, url_prefix='/users')
from api.entities.sawa.models import  LookupDto
from api.entities.sawa.models import  LookupDtos
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
# sets up the app
from flask_cors import CORS, cross_origin
from http.server import HTTPServer, SimpleHTTPRequestHandler

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:opc@2020@192.168.1.103/PurposeDB?driver=SQL+Server'

from flask_sqlalchemy import SQLAlchemy
from flask_jsontools import jsonapi
manager = Manager(app)
migrate = Migrate(app, db)
db = SQLAlchemy(app)

# adds the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)
from api.entities.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=create_engine)

from os import environ
db_uri = 'mssql+pyodbc://sa:opc@2020@192.168.1.103/PurposeDB?driver=SQL+Server'
engine = create_engine(db_uri, echo=True)

# Create All Tables
Base.metadata.create_all(engine)

from api.tokens.create.models import Base
Base.metadata.create_all(engine)

from api.entities.sawa.models import Base
Base.metadata.create_all(engine)
from sqlalchemy.sql import and_, or_, not_
#@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=3001)


#@manager.command
#def runworker():
#    app.run(debug=False)


#@manager.command
#def recreate_db():
  
#    db.drop_all()
#    db.create_all()
#    db.session.commit()

from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:opc@2020@192.168.1.103/PurposeDB?driver=SQL+Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
db.init_app(app)
#cors = CORS(app , resources={r"/*": {"origins": "*"}})
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',)

ns = api.namespace('todos', description='TODO operations')
ns_____________ = api.namespace('tokens', description='Tokens operations')
todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})
def to_dict(obj):

       obj_dict = {
       "__class__": obj.__class__.__name__,
       "__module__": obj.__module__
                  }
  
  
       obj_dict.update(obj.__dict__)
  
       return obj_dict
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
from sqlalchemy.sql import select
from  api.entities.sawa.models import  MainLokupTools
from django.http import JsonResponse
#from api.entities.sawa.models import MainLokupToolsEncoder
import  xlrd
from django.core import serializers
book = xlrd.open_workbook('initdb.xlsx', encoding_override="utf_8")
import uuid
sheet = book.sheet_by_name('Lookups')
r = sheet.nrows 
#c = sheet.ncols
import jsonlib
pageNumber = 1
parentVal = ''
isParent = False
from api.entities.sawa.models import CallerInfo
import datetime
for i in range(1, r):

              valueCol_______0 = str(sheet.cell(i, 0).value)
              valueCol_______1 = str(sheet.cell(i, 1).value)

              if('Part' not in str(sheet.cell(i, 0).value) and valueCol_______0 != ''):

                   lookups = MainLokupTools()
                   lookups.id = uuid.uuid4()
                   lookups.catVal = valueCol_______1
                   lookups.parentVal = sheet.cell(i, 0).value
                   lookups.createBy = "Administrator"
                   lookups.createdDate = datetime.datetime.utcnow()
                   lookups.description = "Lookups Value"
                   lookups.notes = "Lookups Value"
                   lookups.updateBy = "Administrator"
                   lookups.updateDate = datetime.datetime.utcnow()
#                   db.session.add(lookups)
#                   db.session.commit()


import requests 
    
#location = "delhi technological university"
   
#PARAMS = {'address':location} 
  
#r = requests.get(url = URL, params = PARAMS) 
  
#data = r.json() 
#
books = xlrd.open_workbook('catogries.xlsx', encoding_override="utf_8")
sheet = books.sheet_by_name('Lookups')
r = sheet.nrows 
for i in range(1, r):

              valueCol_______0 = str(sheet.cell(i, 0).value)
              valueCol_______1 = str(sheet.cell(i, 1).value)
              valueCol_______2 = str(sheet.cell(i, 2).value)


              lookups = CaseCatogriesKeywords()
              lookups.id = uuid.uuid4()
              lookups.keywords = valueCol_______1
              lookups.options = valueCol_______0
              lookups.parent = valueCol_______2

              lookups.createBy = "Administrator"
              lookups.updateBy = "Administrator"

              lookups.description = "Keywords"
              lookups.notes = "Keywords"


#              db.session.add(lookups)
#              db.session.commit()

#                print(sheet.cell(row=i, column=j).value)
def row2dict(row):
    return {
        c.name: str(getattr(row, c.name))
        for c in row.__table__.columns
    }

class HandleAppClass():
     list = []
     dtosL = []
     def __init__(self , obj):
           self.default(obj)

     def default(self , obj):
             
             for object in obj.dtos:
                        print(object.description)
                        self.dtosL.append(object.catVal)
                        #self.ccc = object
                        #print(object.id)
                        #self.dtosL.append(self.ccc.catVal)
                        #print(self.ccc.description)
             return self.dtosL

def default(o):
    return o._asdict()

class HomeBookEncoder(JSONEncoder):
        def default(self, o):
            return o._asdict()

class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})
import json
import uuid  

@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    @app.route('/list-todo')
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @app.route('/create-todo')
    @ns.marshal_with(todo, code=201)
    def post_todo(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201

@ns_____________.route('/api')
@ns_____________.response(404, 'Todo not found')
@ns_____________.param('id', 'The task identifier')
class Tokens(Resource):


    @ns_____________.doc('/create-token')
    @app.route('/create-token')
    def delete(self):
        '''Delete a task given its identifier'''
        DAO.delete(1)
        return '', 204

    @ns_____________.doc('put-files')
    def put(self):
        '''Update a task given its identifier'''
        return DAO.update(1, api.payload)

    @jwt.user_claims_loader
    def add_claims_to_access_token(user):
        return {'roles': user.roles}

    @jwt.user_identity_loader
    def user_identity_lookup(user):
           return user.username

    @ns_____________.doc('login-processor')
    @app.route('/login-processor' , methods = ['POST'])
    @cross_origin("*")
    def post():
             username = request.json.get('username')
             print(username)
             password = request.json.get('password')
             print(username)
             if (username != 'admin' or password != 'admin') and (username != 'manager' or password != '121@password') and (username != 'administrator' or password != 'opc@2020') and (username != 'support' or password != 'opc@2020') and (username != 'asterisk' or password != 'opc@2020'):
                return jsonify({"msg": "Bad username or password"}), 401

             user = UserTokenObject(username='admin', roles=['foo', 'bar'])

             access_token = create_access_token(identity=user)
             ret = {'access_token': access_token}
             print('access_token' + str(access_token))
             return jsonify(ret), 200

    @ns_____________.doc('keywords-processor')
    @app.route('/keywords-processor' , methods = ['GET'])
    @cross_origin("*")
    def optionsKeywordsLookup():
             parentCat = request.args.get('parent')
             options = request.args.get('options')
#             print(parentCat)
             selctedOption = str(parentCat)
             keywords = db.session.query(CaseCatogriesKeywords).filter(CaseCatogriesKeywords.options == options).all()
#             keywords = select([(CaseCatogriesKeywords.keywords + ", " + CaseCatogriesKeywords.id)].where( and_ (CaseCatogriesKeywords.parents == parentCat , CaseCatogriesKeywords.options == options ) ))
             
             dtos________ = FinalDto
             dtos = []
             listdtos = []
             for row in keywords:

                  id = str(row.id)
                  keywords = str(row.keywords)
                  dtos = FinalDto(id , keywords)
                  listdtos.append(dtos.__dict__)
                  
             
             data = json.dumps(listdtos , ensure_ascii=False).encode('utf8')

             dict = { "data": data.decode('UTF-8')}

#             do = json.JSONDecoder().decode(dict)
#             do = do.encode('UTF-8')
             print('*********************** : ' + data.decode('UTF-8'))
             return jsonify(dict), 200

    @ns_____________.doc('main-form-processor-all')
    @app.route('/main-form-processor-all' , methods = ['GET'])
    @cross_origin("*")
    def optionsSearch():

#             parentCat = request.args.get('parent')
#             print(parentCat)
#             selctedOption = str(parentCat)

             query = db.session.query(BaseSawaBooks).all()
             
             dtos________ = BaseBookDto

             dtos = []

             listdtos = []

             for row in query:

                  idCard = str(row.idNumber)
                  fullName = str(row.fullName)
                  socialName = str(row.socialSituations)
                  economySitutation = str(row.economySitutation)
                  healthSituation = str(row.healthSituation)
                  ageViolance = str(row.ageViolance)
                  
                  dtos = BaseBookDto(idCard , fullName , socialName , economySitutation , healthSituation , ageViolance)
                  print(dtos.fullName)
                  listdtos.append(dtos.__dict__)

#                 dto = LookupDto(row.id , row.parentVal , row.catVal ,
#                 row.createBy , row.createdDate , row.updateDate ,
#                 row.updateBy , row.description , row.notes)
#                 print(row.description)
#                 dto.id = row.id
#                 dto.catVal = row.catVal
#                 dto.parentVal = row.parentVal
#                 dto.createdDate = row.createdDate
#                 dtos.append(dto)

             #dtos________ = FinalDto(dtos)


             #for object in dtos________.dtos :
             #            listdtos.append(object.catVal)
             #            print(object.catVal)
               
             #data = default(listdtos)
             data = json.dumps(listdtos , ensure_ascii=False).encode('utf8')

             dict = { "data": data.decode('UTF-8')}

#             do = json.JSONDecoder().decode(dict)
#             do = do.encode('UTF-8')
             print('*********************** : ' + data.decode('UTF-8'))
             return jsonify(dict), 200

    @ns_____________.doc('lookups-processor')
    @app.route('/lookups-processor' , methods = ['GET'])
    @cross_origin("*")
    def optionsLookup():
             parentCat = request.args.get('parent')
#             print(parentCat)
             selctedOption = str(parentCat)
             query = db.session.query(MainLokupTools).filter(MainLokupTools.parentVal.startswith(selctedOption)).all()
             
             dtos________ = FinalDto
             dtos = []
             listdtos = []
             for row in query:

                  id = str(row.id)
                  catVal = str(row.catVal)
                  dtos = FinalDto(id , catVal)
                  listdtos.append(dtos.__dict__)

#                 dto = LookupDto(row.id , row.parentVal , row.catVal ,
#                 row.createBy , row.createdDate , row.updateDate ,
#                 row.updateBy , row.description , row.notes)
#                 print(row.description)
#                 dto.id = row.id
#                 dto.catVal = row.catVal
#                 dto.parentVal = row.parentVal
#                 dto.createdDate = row.createdDate
#                 dtos.append(dto)

             #dtos________ = FinalDto(dtos)


             #for object in dtos________.dtos :
             #            listdtos.append(object.catVal)
             #            print(object.catVal)
               
             #data = default(listdtos)
             data = json.dumps(listdtos , ensure_ascii=False).encode('utf8')

             dict = { "data": data.decode('UTF-8')}

#             do = json.JSONDecoder().decode(dict)
#             do = do.encode('UTF-8')
             print('*********************** : ' + data.decode('UTF-8'))
             return jsonify(dict), 200


    @ns_____________.doc('save-case-processor')
    @app.route('/save-case-processor' , methods = ['POST'])
    @cross_origin("*")
    def postCasesCallerInfo():

        situationSelected = request.json.get('situationSelected')
        livesWith = request.json.get('livesWith')
        textDescription = request.json.get('textDescription')
        

#        lastStep = request.json.get('lastStep')
#        description = request.json.get('description')
#        person = request.json.get('personName')
#        notes = request.json.get('notes')
#        sameCaller = request.json.get('sameCaller')

        description1 = request.json.get('description1')
        description2 = request.json.get('description2')
        description3 = request.json.get('description3')

        base_______object = CaseChildsInfo()
        base_______object.situationSelected = situationSelected
        base_______object.livesWith = livesWith
        base_______object.textDescription = textDescription
#        base_______object.endTime = endTime
#        base_______object.startTime = startTime

#        base_______object = CallerInfo()
#        base_______object.communicateType = communicateType
#        base_______object.idNumber = idNumber
#        base_______object.fullName = fullName
#        base_______object.realationShip = realationShip
#        base_______object.nextStep = nextStep
#        base_______object.lastStep = lastStep
        base_______object.description = description1
        base_______object.notes = description1
#        base_______object.sameCaller = sameCaller
        base_______object.createBy = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.notesInfo = "Administrator"
#        base_______object.personName = firstPerson


        base_______object.description1 = description1
        base_______object.description2 = description2
        base_______object.description3 = description3

        base_______object.descriptionInfo = "Administrator"
        base_______object.updateBy = "Administrator"

        db.session.add(base_______object)
        db.session.commit()

        return jsonify("sucess"), 200


    @ns_____________.doc('save-formnotes-processor')
    @app.route('/save-formnotes-processor' , methods = ['POST'])
    @cross_origin("*")
    def postMainNotesInfo():
         componentName = request.json.get('componentName')
         valueTxT = request.json.get('valueTxT')
         txtNotes = request.json.get('txtNotes')
        

#        lastStep = request.json.get('lastStep')
#        description = request.json.get('description')
#        person = request.json.get('personName')
#        notes = request.json.get('notes')
#        sameCaller = request.json.get('sameCaller')

         

         base_______object = MainFormNotes()
         base_______object.componentName = componentName
         base_______object.valueTxT = valueTxT
         base_______object.txtNotes = txtNotes
#        base_______object.endTime = endTime
#        base_______object.startTime = startTime

#        base_______object = CallerInfo()
#        base_______object.communicateType = communicateType
#        base_______object.idNumber = idNumber
#        base_______object.fullName = fullName
#        base_______object.realationShip = realationShip
#        base_______object.nextStep = nextStep
#        base_______object.lastStep = lastStep
         base_______object.description = txtNotes
         base_______object.notes = txtNotes
#        base_______object.sameCaller = sameCaller
         base_______object.createBy = "Administrator"
        
#        base_______object.personName = firstPerson


         #base_______object.description1 = description1
         #base_______object.description2 = description2
         #base_______object.description3 = description3

        
         base_______object.updateBy = "Administrator"

         db.session.add(base_______object)
         db.session.commit()

         return jsonify("sucess"), 200


    @ns_____________.doc('save-police-processor')
    @app.route('/save-police-processor' , methods = ['POST'])
    @cross_origin("*")
    def postCasesPoliceInfo():

        callPolice = request.json.get('callPolice')
        policecenter = request.json.get('policecenter')
        policenumber = request.json.get('policenumber')
        
        fileNumber = request.json.get('fileNumber')
        volPerson = request.json.get('volPerson')
        callPoliceDate = request.json.get('callPoliceDate')

#        lastStep = request.json.get('lastStep')
#        description = request.json.get('description')
#        person = request.json.get('personName')
#        notes = request.json.get('notes')
#        sameCaller = request.json.get('sameCaller')

        description1 = request.json.get('description1')
        description2 = request.json.get('description2')
        description3 = request.json.get('description3')

        base_______object = CasePoliceInfo()


        base_______object.callPolice = callPolice
        base_______object.policecenter = policecenter
        base_______object.policenumber = policenumber

        base_______object.fileNumber = fileNumber
        base_______object.volPerson = volPerson
        base_______object.callPoliceDate = callPoliceDate


#        base_______object.endTime = endTime
#        base_______object.startTime = startTime

#        base_______object = CallerInfo()
#        base_______object.communicateType = communicateType
#        base_______object.idNumber = idNumber
#        base_______object.fullName = fullName
#        base_______object.realationShip = realationShip
#        base_______object.nextStep = nextStep
#        base_______object.lastStep = lastStep
        base_______object.description = description1
        base_______object.notes = description1
#        base_______object.sameCaller = sameCaller
        base_______object.createBy = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.notesInfo = "Administrator"
#        base_______object.personName = firstPerson


        base_______object.description1 = description1
        base_______object.description2 = description2
        base_______object.description3 = description3

        base_______object.descriptionInfo = "Administrator"
        base_______object.updateBy = "Administrator"

        db.session.add(base_______object)
        db.session.commit()

        return jsonify("sucess"), 200

    @ns_____________.doc('save-voilance-processor')
    @app.route('/save-voilance-processor' , methods = ['POST'])
    @cross_origin("*")
    def postCasesVoilanceInfo():

        volianceRelated = request.json.get('volianceRelated')
        caseType = request.json.get('caseType')
        socialSituation = request.json.get('socialSituation')
        
        econmySituation = request.json.get('econmySituation')
        voliancePlace = request.json.get('voliancePlace')
        period = request.json.get('period')

#        lastStep = request.json.get('lastStep')
#        description = request.json.get('description')
#        person = request.json.get('personName')
#        notes = request.json.get('notes')
#        sameCaller = request.json.get('sameCaller')

        description1 = request.json.get('description1')
        description2 = request.json.get('description2')
        description3 = request.json.get('description3')

        base_______object = CaseVolianceInfo()


        base_______object.volianceRelated = volianceRelated
        base_______object.caseType = caseType
        base_______object.socialSituation = socialSituation

        base_______object.econmySituation = econmySituation
        base_______object.voliancePlace = voliancePlace
        base_______object.period = period


#        base_______object.endTime = endTime
#        base_______object.startTime = startTime

#        base_______object = CallerInfo()
#        base_______object.communicateType = communicateType
#        base_______object.idNumber = idNumber
#        base_______object.fullName = fullName
#        base_______object.realationShip = realationShip
#        base_______object.nextStep = nextStep
#        base_______object.lastStep = lastStep
        base_______object.description = description1
        base_______object.notes = description1
#        base_______object.sameCaller = sameCaller
        base_______object.createBy = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.notesInfo = "Administrator"
#        base_______object.personName = firstPerson


        base_______object.description1 = description1
        base_______object.description2 = description2
        base_______object.description3 = description3

        base_______object.descriptionInfo = "Administrator"
        base_______object.updateBy = "Administrator"

        db.session.add(base_______object)
        db.session.commit()

        return jsonify("sucess"), 200

    @ns_____________.doc('rec-caller-processor')
    @app.route('/rec-caller-processor' , methods = ['POST'])
    @cross_origin("*")
    def postRecCallerInfo():

        firstPerson = request.json.get('firstPerson')
        secondPersonName = request.json.get('secondPersonName')
        basedDate = request.json.get('basedDate')
        startTime = request.json.get('startTime')
        endTime = request.json.get('endTime')

#        lastStep = request.json.get('lastStep')
#        description = request.json.get('description')
#        person = request.json.get('personName')
#        notes = request.json.get('notes')
#        sameCaller = request.json.get('sameCaller')

        description1 = request.json.get('description1')
        description2 = request.json.get('description2')
        description3 = request.json.get('description3')

        base_______object = RecCallerInfo()
        base_______object.basedDate = basedDate
        base_______object.firstPerson = firstPerson
        base_______object.secondPersonName = secondPersonName
        base_______object.endTime = endTime
        base_______object.startTime = startTime

#        base_______object = CallerInfo()
#        base_______object.communicateType = communicateType
#        base_______object.idNumber = idNumber
#        base_______object.fullName = fullName
#        base_______object.realationShip = realationShip
#        base_______object.nextStep = nextStep
#        base_______object.lastStep = lastStep
        base_______object.description = description1
        base_______object.notes = description1
#        base_______object.sameCaller = sameCaller
        base_______object.createBy = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.personName = firstPerson


        base_______object.description1 = description1
        base_______object.description2 = description2
        base_______object.description3 = description3

        base_______object.descriptionInfo = "Administrator"
        base_______object.updateBy = "Administrator"

        db.session.add(base_______object)
        db.session.commit()

        return jsonify("sucess"), 200


    @ns_____________.doc('caller-processor')
    @app.route('/caller-processor' , methods = ['POST'])
    @cross_origin("*")
    def postCallerInfo():

        idNumber = request.json.get('idNumber')
        fullName = request.json.get('fullName')
        realationShip = request.json.get('realationShip')
        communicateType = request.json.get('communicateType')
        nextStep = request.json.get('nextStep')
        lastStep = request.json.get('lastStep')
        description = request.json.get('description')
        person = request.json.get('personName')
        notes = request.json.get('notes')
        sameCaller = request.json.get('sameCaller')

        description1 = request.json.get('description1')
        description2 = request.json.get('description2')
        description3 = request.json.get('description3')

        base_______object = CallerInfo()
        base_______object.communicateType = communicateType
        base_______object.idNumber = idNumber
        base_______object.fullName = fullName
        base_______object.realationShip = realationShip
        base_______object.nextStep = nextStep
        base_______object.lastStep = lastStep
        base_______object.description = description
        base_______object.notes = notes
        base_______object.sameCaller = sameCaller
        base_______object.createBy = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.notesInfo = "Administrator"
        base_______object.personName = person


        base_______object.description1 = description1
        base_______object.description2 = description2
        base_______object.description3 = description3

        base_______object.descriptionInfo = "Administrator"
        base_______object.updateBy = "Administrator"

        db.session.add(base_______object)
        db.session.commit()

        return jsonify("sucess"), 200

    @ns_____________.doc('save-processor')
    @app.route('/save-processor' , methods = ['POST'])
    @cross_origin("*")
    def postHome():

             #name = request.json.get('name')
             nickName = request.json.get('nickName')
#             print(nickName)

             roles = request.json.get('roles')
#             print(roles)
#
             age = request.json.get('age')
#             print(age)
             
             gender = request.json.get('gender')
#             print(gender)

             location = request.json.get('location')
#             print(location)


             state = request.json.get('state')
#             print(state)


             desiredPlace = request.json.get('desiredPlace')
#             print(desiredPlace)

             placeCompany = request.json.get('placeCompany')
#             print(placeCompany)

             publicReputation = request.json.get('publicReputation')
#             print(publicReputation)

             caseType = request.json.get('caseType')
#             print(caseType)


             currentCareer = request.json.get('currentCareer')
#             print(currentCareer)
             
             
             socialSituations = request.json.get('socialSituations')
#             print(socialSituations)
             
             
             economySitutation = request.json.get('economySitutation')
#             print(economySitutation)


             healthSituation = request.json.get('healthSituation')
#             print(healthSituation)

             nationality = request.json.get('nationality')
#             print(nationality)


             personLanguage = request.json.get('personLanguage')
#             print(personLanguage)

             ageViolance = request.json.get('ageViolance')
#             print(ageViolance)

             fullName = request.json.get('fullName')
#             print(fullName)

             idNumber = request.json.get('idNumber')
#             print(idNumber)

             association = request.json.get('association') 
#             print(association)

             medicalConsultation = request.json.get('medicalConsultation')
#             print(medicalConsultation)

             inquiriesDiseases = request.json.get('inquiriesDiseases')
#             print(inquiriesDiseases)

             hospitalAdmission = request.json.get('hospitalAdmission')
#             print(hospitalAdmission)


             healthCare = request.json.get('healthCare')
#             print(healthCare)


             selfHarming = request.json.get('selfHarming')
#             print(selfHarming)

             secretsDisclosure = request.json.get('secretsDisclosure')
#            print(secretsDisclosure)


             depression = request.json.get('depression')
#             print(depression)


             suicide = request.json.get('suicide')
#             print(suicide)


             obsessive = request.json.get('obsessive')
#             print(obsessive)


             stealing = request.json.get('stealing')
#             print(stealing)


             nervousness = request.json.get('nervousness')
#             print(nervousness)


             schizophrenia = request.json.get('schizophrenia')
#             print(schizophrenia)


             fear = request.json.get('fear')
#             print(fear)



             lying = request.json.get('lying')
#             print(lying)


             adolescence = request.json.get('adolescence')
#             print(adolescence)


             psychologicalDischarge = request.json.get('psychologicalDischarge')
#             print(psychologicalDischarge)


             boredom = request.json.get('boredom')
#             print(boredom)


             lifeEnd = request.json.get('lifeEnd')
#             print(lifeEnd)


             peeReflex = request.json.get('peeReflex')
#             print(peeReflex)


             LowSelfEsteem = request.json.get('LowSelfEsteem')
#             print(LowSelfEsteem)


             threat = request.json.get('threat')
#             print(threat)


             deathThreat = request.json.get('deathThreat')
#             print(deathThreat)


             economicDeprivation = request.json.get('economicDeprivation')
 #            print(economicDeprivation)

             control = request.json.get('control')
 #            print(control)


             nailBiting = request.json.get('nailBiting')
 #            print(nailBiting)


             nightmares = request.json.get('nightmares')
#             print(nightmares)


             speechProblems = request.json.get('speechProblems')
#             print(speechProblems)

             helpThanks = request.json.get('helpThanks')
#             print(helpThanks)


             line = request.json.get('line')
#             print(line)
             volunteer = request.json.get('volunteer')
#            print(volunteer)
             helpChildern = request.json.get('helpChildern')
#             print(helpChildern)
             professional = request.json.get('professional')
#             print(association)
             

             print("......................................")

             print(uuid.uuid4())

             base_______object = BaseSawaBooks()
             base_______object.id = uuid.uuid4()
             base_______object.permitCode = "PurposeRGU"
             base_______object.permitName = "OPSW"
             base_______object.roles = roles
             base_______object.nickName = nickName
             base_______object.adolescence = adolescence
             base_______object.age = age
             base_______object.ageViolance = ageViolance
             base_______object.association = association
             base_______object.boredom = boredom
             base_______object.caseType = caseType
             base_______object.control = control
             base_______object.currentCareer = currentCareer
             base_______object.deathThreat = deathThreat
             base_______object.depression = depression
             base_______object.Description = "Add Process Workflow"
             base_______object.desiredPlace = desiredPlace
             base_______object.placeCompany = placeCompany
             base_______object.notes = "Add Process Workflow"
             base_______object.publicReputation = publicReputation
             base_______object.socialSituations = socialSituations
             base_______object.economySitutation = economySitutation
             base_______object.healthSituation = healthSituation
             base_______object.nationality = nationality
             base_______object.personLanguage = personLanguage
             base_______object.ageViolance = ageViolance
             base_______object.fullName = fullName
             base_______object.idNumber = idNumber
             base_______object.association = association
             base_______object.state = state
             base_______object.medicalConsultation = medicalConsultation
             base_______object.inquiriesDiseases = inquiriesDiseases
             base_______object.hospitalAdmission = hospitalAdmission
             base_______object.healthCare = healthCare
             base_______object.selfHarming = selfHarming
             base_______object.secretsDisclosure = secretsDisclosure
             base_______object.depression = depression
             base_______object.suicide = suicide
             base_______object.obsessive = obsessive
             base_______object.stealing = stealing
             base_______object.nervousness = nervousness
             base_______object.schizophrenia = schizophrenia
             base_______object.fear = fear
             base_______object.lying = lying
             base_______object.psychologicalDischarge = psychologicalDischarge
             base_______object.lifeEnd = lifeEnd
             base_______object.peeReflex = peeReflex
             base_______object.LowSelfEsteem = LowSelfEsteem
             base_______object.threat = threat
             base_______object.deathThreat = deathThreat
             base_______object.economicDeprivation = economicDeprivation
             base_______object.control = control
             base_______object.nailBiting = nailBiting
             base_______object.nailBiting = nailBiting
             base_______object.nightmares = nightmares
             base_______object.speechProblems = nightmares
             base_______object.helpThanks = helpThanks
             base_______object.line = helpThanks
             base_______object.volunteer = helpThanks
             base_______object.helpChildern = helpChildern
             base_______object.professional = professional


             db.session.add(base_______object)
             db.session.commit()


#             homeJson = json.dumps(base_______object, cls=HomeBookEncoder)
#             renderJson = json.loads(homeJson)

             
             return jsonify("sucess"), 200

    @ns_____________.doc('token-gets')
    @app.route('/token-gets')
    @ns_____________.response(204, 'get token featuers')
    @jwt_required
    def create():
       ret = {
        'current_identity': get_jwt_identity(),  # test
        'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
             }
       return jsonify(ret), 200

    @ns_____________.doc('current-user')
    @app.route('/current-user')
    @ns_____________.response(204, 'get_current_user featuers')
    def getloggedin():
         user_id = get_jwt_identity()
         user = get_user_by_id(user_id)
         return jsonify(__serialize_user(user))

    @ns_____________.doc('update-user')
    @app.route('/UpdateUser')
    @ns_____________.response(204, 'update_current_user featuers')
    def update():
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
# app = Flask(__name__)
class UserTokenObject(Resource):
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles
import os

#from django.core.wsgi import get_wsgi_application
#from django.conf import settings
#from django.core.management import setup_environ
app.register_blueprint(bp)
#httpd = HTTPServer(('localhost', 8003), CORSRequestHandler)
#httpd.serve_forever()
import os
import sys


#setup_environ(settings)
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development')
#os.environ["SECRET_KEY"] =
#"ftov1!91yf@7f7&g2%*@0_e^)ac&f&9jeloc@#v76#^b1dhbl#"
#import django
#settings.configure()
if __name__ == "__main__":
#    django.setup()
    runserver()
    