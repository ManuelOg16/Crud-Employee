from marshmallow import fields, Schema, validate
from . import db
from app.config import Config

engine= Config.engine
class BeneficiariesModel(db.Model):
    
    __tablename__ = 'beneficiarios'

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(60))
    Apellidos = db.Column(db.String(60))
    Fecha_Nacimiento= db.Column(db.Date)
    Curp = db.Column(db.String(60))
    Ssn = db.Column(db.Integer) 
    Telefono = db.Column(db.BigInteger)   
    Nacionalidad =db.Column(db.String(60))
    Porcentaje_Participacion = db.Column(db.Integer)   
    Idempleados = db.Column( db.Integer, db.ForeignKey("empleados.id"))


    def __init__(self,data):
        """
        Class constructor
        """
        self.Nombre= data.get('Nombre')
        self.Apellidos= data.get('Apellidos')
        self.Fecha_Nacimiento = data.get('Fecha_Nacimiento') 
        self.Curp = data.get('Curp')
        self.Ssn = data.get('Ssn')
        self.Telefono = data.get('Telefono')
        self.Nacionalidad = data.get('Nacionalidad') 
        self.Porcentaje_Participacion = data.get('Porcentaje_Participacion')
        self.Idempleados = data.get('Idempleados')
    
    def post_beneficiary(self, fields_data, values_tuple):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql=f"""exec pa_INSERT_BENEFICIARIOS {fields_data}"""
        params = values_tuple
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)

    def get_all_beneficiaries(self):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql = "exec pa_SELECT_BENEFICIARIOS"
        cursor.execute(sql)
        register = cursor.fetchall()
        cursor.commit()
        return register

    def update_beneficiary(self, fields_data, values_tuple):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql=f"""exec pa_UPDATE_BENEFICIARIOS {fields_data}"""
        params = values_tuple
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)

    def delete_one_beneficiary(self, id):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="""exec pa_DELETE_BENEFICIARIO  @id=?"""
        params = (id)
        cursor=cursor.execute(sql, params)
        result=cursor
        cursor.commit()
        print(result)


    def get_sum_percentage(self, id):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="""exec pa_SELECT_EMPLEADO_X_ID_SUMA  @Idempleados=?"""
        params = (id)
        cursor=cursor.execute(sql, params)
        result=cursor.fetchall()
        cursor.commit()
        return result

    def get_one_beneficiary(self,id):
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="""exec pa_SELECT_BENEFICIARIO_X_ID  @id=?"""
        params = (id)
        cursor=cursor.execute(sql, params)
        result=cursor.fetchall()
        cursor.commit()
        return result

class BeneficiariesSchema(Schema):
    """
    Beneficiaries Schema
    """
    id = fields.Int()
    Nombre = fields.Str(required=True, validate=[validate.Length(max=60)])
    Apellidos = fields.Str()
    Fecha_Nacimiento = fields.Date('%Y-%m-%d')
    Curp = fields.Str()
    Ssn = fields.Int()
    Telefono = fields.Int(validate=[validate.Range(min=1111111111, max=9999999999)])
    Nacionalidad = fields.Str()
    Porcentaje_Participacion = fields.Int(validate=[validate.Range(min=1, max=100)])
    Idempleados = fields.Int(required=True)

