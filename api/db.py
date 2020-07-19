from flask_sqlalchemy import SQLAlchemy

# instantiate database object
db = SQLAlchemy()

from sqlalchemy import create_engine
import cx_Oracle

#host='localhost'
#port=1521
#sid='ORCL'
#user='purpose'
#password='opc@2020'
#sid = cx_Oracle.makedsn(host, port, sid=sid)

#cstr = 'oracle+cx_oracle://{user}:{password}@{sid}'.format(
#    user=user,
#    password=password,
#    sid=sid
#)
import pyodbc



engine = create_engine("mssql+pyodbc://sa:opc@2020@192.168.1.103/PurposeDB?driver=SQL+Server",isolation_level="REPEATABLE READ")
