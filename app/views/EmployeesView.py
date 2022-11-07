from flask import Flask,request,json,render_template
from flask_restx import fields,Resource, Namespace
from ..models.EmployeesModel import EmployeesModel,EmployeesSchema
from ..shared import returnCodes
from ..models import db
from marshmallow import ValidationError
import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

nsEmployees= Namespace("Employees", description="Endpoint operations for Employees")
employee_schema = EmployeesSchema()
EmployeePostApi = nsEmployees.model(
    "EmployeesModel",
    {
        "Nombre": fields.String(required=True, description="Nombre"),
        "Apellidos": fields.String(description="Apellidos"),
        "Fecha_Nacimiento": fields.Date(description="Fecha_Nacimiento"),
        "Numero_Empleado": fields.Integer(description="Numero_Empleado"),
        "Curp": fields.String(description="Curp"),
        "Ssn": fields.Integer(description="Ssn"),
        "Telefono": fields.Integer(description="Telefono"),
        "Nacionalidad": fields.String(description="Nacionalidad"),
    }
)

EmployeePatchApi = nsEmployees.model(
    "EmployeePatchModel",
    {
        
        "id": fields.Integer(required=True, description="identificador"),
        "Nombre": fields.String(required=True, description="Nombre"),
        "Apellidos": fields.String(description="Apellidos"),
        "Fecha_Nacimiento": fields.Date(description="Fecha_Nacimiento"),
        "Numero_Empleado": fields.Integer(description="Numero_Empleado"),
        "Curp": fields.String(description="Curp"),
        "Ssn": fields.Integer(description="Ssn"),
        "Telefono": fields.Integer(description="Telefono"),
        "Nacionalidad": fields.String(description="Nacionalidad"),
        
    }
)
def create_fields_values(req_data):
    list_keys_data,list_values_data= ['@'+row+'=?' for row in req_data],[req_data[row ] for row in req_data]
    fields_data= ", ".join(list_keys_data)
    values_tuple = tuple(list_values_data)
    return fields_data,values_tuple

def date_birth(req_data):
        date_updated=str((datetime.datetime.now().strftime('%Y-%m-%d')))
        format_date = '%Y-%m-%d'
        end= datetime.datetime.strptime(date_updated,format_date).date()
        start=datetime.datetime.strptime(req_data["Fecha_Nacimiento"],format_date).date()
        current_age = relativedelta(end, start).years
        return current_age 

@nsEmployees.route("")
class EmployeesList(Resource):
    ######## GET ALL PRODUCTS
    @nsEmployees.doc("Read Employees")
    def get(self):
        """List all Employees"""
        employees_values = EmployeesModel.get_all_employees(self)
        employees_keys = ('id','Nombre','Apellidos','Fecha_Nacimiento'
                                ,'Numero_Empleado','Curp','Ssn','Telefono','Nacionalidad')
        list_all_employees=[dict(zip(employees_keys, row)) for row in employees_values if len(employees_keys) == len(row)]
        return returnCodes.custom_response(list_all_employees, 200, 2001, "EMP-3")
    ##########################

    ######CREATE ALL PRODUCTS
    @nsEmployees.doc("Create Employees")
    @nsEmployees.expect(EmployeePostApi)
    @nsEmployees.response(201, "created")
    def post(self):
        """Create Employees"""
        req_data = request.get_json(force=True)
        print(req_data)
        data=None
        if(not req_data):
            return returnCodes.custom_response(None, 400, 4001, "EMP-2")
        try:
            data= employee_schema .load(req_data, partial=True)
        except ValidationError as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-2", str(err))

        current_age = date_birth(req_data)
        if current_age < 18 :
            return returnCodes.custom_response(None, 400, 4001, "EMP-14")

        fields_data,values_tuple=create_fields_values(req_data)
        print(fields_data,values_tuple)
        try:
            EmployeesModel.post_employee(self, fields_data,values_tuple)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-8")
        
        return returnCodes.custom_response(req_data, 201, 2011, "EMP-1")

    ################################
    
    ######### UPDATE ONE PRODUCT#######
    @nsEmployees.doc("Update Employee")
    @nsEmployees.expect(EmployeePatchApi)
    def patch(self):
        """Update one Employee"""
        req_data = request.get_json(force=True)
        data=None
        try:
            data=employee_schema .load(req_data, partial=True)
        except ValidationError as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-2", str(err))

        if "Fecha_Nacimiento" in req_data:
            current_age = date_birth(req_data)
            if current_age < 18 :
                return returnCodes.custom_response(None, 400, 4001, "EMP-14")

        employee_id = EmployeesModel.get_one_employee(self, data.get("id"))

        if len(employee_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-10")

        fields_data,values_tuple=create_fields_values(req_data)
        try:
            EmployeesModel.update_employee(self, fields_data,values_tuple)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-11")
        
        return returnCodes.custom_response(req_data, 200, 2012, "EMP-6")

    ##########################################

##############DELETE ONE PRODUCT
@nsEmployees.route("/<id>")
@nsEmployees.expect(EmployeePatchApi)
@nsEmployees.response(404, "Not found")
class OneEmployee(Resource):
    @nsEmployees.doc("Delete Employee")
    def delete(self, id):
        """Delete one Employee"""
        employee_id = EmployeesModel.get_one_employee(self, id)
        if len(employee_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-10")
        try:
            EmployeesModel.delete_one_employee(self, id)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-12")

        return returnCodes.custom_response(None, 200, 2012, "EMP-13")
###############################

