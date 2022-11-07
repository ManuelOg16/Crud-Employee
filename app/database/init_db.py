import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID=os.getenv("UID")
PWD=os.getenv("PWD")

connection=pyodbc.connect("DRIVER={SQL Server}"+";"+"SERVER="+SERVER+";"+"DATABASE="+DATABASE+";"+"UID="+UID+";"+"PWD="+PWD)
cursor = connection.cursor()

try:
    with open('sp_insert_beneficiario.sql') as ib,open('sp_select_beneficiarios.sql') as rb, open('sp_update_beneficiario.sql') as ub, open('sp_delete_beneficiario.sql') as dlb,open('sp_select_id_beneficiario.sql') as idb :
    
        connection.execute(ib.read())
        connection.execute(rb.read())
        connection.execute(ub.read())
        connection.execute(dlb.read())
        connection.execute(idb.read())

    with open('sp_insert_empleado.sql') as iem,open('sp_select_empleados.sql') as rem, open('sp_update_empleado.sql') as uem, open('sp_delete_empleado.sql') as dlem, open('sp_select_id_empleado.sql') as idem, open('sp_sum_id_empleados.sql') as sme :
        
        connection.execute(iem.read())
        connection.execute(rem.read())
        connection.execute(uem.read())
        connection.execute(dlem.read())
        connection.execute(idem.read())
        connection.execute(sme.read())
    print("conexion exitosa")
    cursor.commit()
except Exception as e:
    print("Ocurrio un error al conectar a sql server", e)

connection.close() 


