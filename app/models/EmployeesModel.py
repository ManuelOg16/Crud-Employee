from marshmallow import fields, Schema, validate
from . import db
from app.config import Config

engine= Config.engine
class EmployeesModel(db.Model):
    
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(60))
    Apellidos = db.Column(db.String(60))
    Fecha_Nacimiento= db.Column(db.Date)
    Numero_Empleado = db.Column(db.Integer) 
    Curp = db.Column(db.String(60))
    Ssn = db.Column(db.Integer) 
    Telefono = db.Column(db.BigInteger) 
    Nacionalidad = db.Column(db.String(60))
    
    def __init__(self,data):
        """
        Class constructor
        """
        self.Nombre= data.get('Nombre')
        self.Apellidos= data.get('Apellidos')
        self.Fecha_Nacimiento = data.get('Fecha_Nacimiento') 
        self.Numero_Empleado = data.get('Numero_Empleado') 
        self.Curp = data.get('Curp')
        self.Ssn = data.get('Ssn')
        self.Telefono = data.get('Telefono')
        self.Nacionalidad = data.get('Nacionalidad')
        
    # def __repr(self):
    #     return '<id {}>'.format(self.id)

    
    def post_employee(self, fields_data, values_tuple):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql=f"""exec pa_INSERT_EMPELADOS {fields_data}"""
        params = values_tuple
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)

    def get_all_employees(self):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql = "exec pa_SELECT_EMPLEADOS"
        cursor.execute(sql)
        register = cursor.fetchall()
        cursor.commit()
        return register

    def update_employee(self, fields_data, values_tuple):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql=f"""exec pa_UPDATE_EMPLEADOS {fields_data}"""
        params = values_tuple
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)

    def delete_one_employee(self, id):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="""exec pa_DELETE_EMPLEADO  @id=?"""
        params = (id)
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)

    def get_one_employee(self,id):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="""exec pa_SELECT_EMPLEADO_X_ID  @id=?"""
        params = (id)
        cursor=cursor.execute(sql, params)
        result=cursor.fetchall()
        cursor.commit()
        print(result)
        print("connection terminated")
        return result

class EmployeesSchema(Schema):
    """
    Order Employees
    """
    id = fields.Int()
    Nombre = fields.Str(required=True, validate=[validate.Length(max=60)])
    Apellidos = fields.Str()
    Fecha_Nacimiento = fields.Date('%Y-%m-%d')
    Numero_Empleado = fields.Int()
    Curp = fields.Str()
    Ssn = fields.Int()
    Telefono = fields.Int(validate=[validate.Range(min=1111111111, max=9999999999)])
    Nacionalidad = fields.Str()
