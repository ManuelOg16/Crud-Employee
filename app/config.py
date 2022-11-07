import urllib.parse 
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

class Config:
    load_dotenv()
    ENV= os.getenv("ENVIRONMENT") 
    SERVER = os.getenv("SERVER")
    DATABASE = os.getenv("DATABASE")
    UID=os.getenv("UID")
    PWD=os.getenv("PWD")
    params = urllib.parse.quote_plus("DRIVER={SQL Server}"+";"+"SERVER="+SERVER+";"+"DATABASE="+DATABASE+";"+"UID="+UID+";"+"PWD="+PWD)
    SQLALCHEMY_DATABASE_URI =  "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params) 
