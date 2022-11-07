from flask import Flask,json,request
from flask_restx import fields,Resource, Namespace
from marshmallow import ValidationError
from ..models.BeneficiariesModel import BeneficiariesModel,BeneficiariesSchema
from ..models.EmployeesModel import EmployeesModel
from ..shared import returnCodes
import datetime
from dateutil.relativedelta import relativedelta
app = Flask(__name__)

nsBeneficieries= Namespace("Beneficiaries", description="Endpoint operations for Beneficiaries")
beneficiary_schema = BeneficiariesSchema()
beneficiaryPostApi = nsBeneficieries.model(
    "BeneficiariesPostModel",
    {
        "Nombre": fields.String(required=True, description="Nombre"),
        "Apellidos": fields.String(description="Apellidos"),
        "Fecha_Nacimiento": fields.Date(description="Fecha_Nacimiento"),
        "Curp": fields.String(description="Curp"),
        "Ssn": fields.Integer(description="Ssn"),
        "Telefono": fields.Integer(description="Telefono"),
        "Nacionalidad": fields.String(description="Nacionalidad"),
        "Porcentaje_Participacion": fields.Integer(description="Porcentaje_Participacion"),
        "Idempleados": fields.Integer(required=True,description="Idempleados")
    }
)

beneficiaryPatchApi = nsBeneficieries .model(
    "BeneficiariesPatchModel",
    {
        
        "id": fields.Integer(required=True, description="identificador"),
        "Nombre": fields.String(description="Nombre"),
        "Apellidos": fields.String(description="Apellidos"),
        "Fecha_Nacimiento": fields.Date(description="Fecha_Nacimiento"),
        "Curp": fields.String(description="Curp"),
        "Ssn": fields.Integer(description="Ssn"),
        "Telefono": fields.Integer(description="Telefono"),
        "Nacionalidad": fields.String(description="Nacionalidad"),
        "Porcentaje_Participacion": fields.Integer(description="Porcentaje_Participacion"),
        "Idempleados": fields.Integer(required=True,description="Idempleados")
        
    }
)

##################################    
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


@nsBeneficieries.route("")
class BeneficieriesList(Resource):
    ######## GET ALL PRODUCTS
    @nsBeneficieries.doc("Read Beneficiaries")
    def get(self):
        """List all Beneficiaries"""
        beneficiaries_values = BeneficiariesModel.get_all_beneficiaries(self)
        beneficiaries_keys = ('id','Nombre','Apellidos','Fecha_Nacimiento'
                                ,'Curp','Ssn','Telefono','Nacionalidad'
                                ,'Porcentaje_Participacion','Idempleados')
        list_all_beneficiaries=[dict(zip(beneficiaries_keys, row)) for row in beneficiaries_values if len(beneficiaries_keys) == len(row)]
        return returnCodes.custom_response(list_all_beneficiaries, 200, 2001, "EMP-3")
    ##########################

    ######CREATE ALL PRODUCTS
    @nsBeneficieries.doc("Create Beneficiaries")
    @nsBeneficieries.expect(beneficiaryPostApi)
    @nsBeneficieries.response(201, "created")
    def post(self):
        """Create Beneficiaries"""
        req_data = request.get_json(force=True)
        data=None
        if(not req_data):
            return returnCodes.custom_response(None, 400, 4001, "EMP-2")
        try:
            data= beneficiary_schema.load(req_data, partial=True)
        except ValidationError as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-2", str(err))

        current_age = date_birth(req_data)
        if current_age < 18 :
            return returnCodes.custom_response(None, 400, 4001, "EMP-14")

        
        employee_id = EmployeesModel.get_one_employee(self, data.get("Idempleados"))
        if len(employee_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-15")


        participation_percentage=data.get("Porcentaje_Participacion")
        sum_percentage = BeneficiariesModel.get_sum_percentage(self, data.get("Idempleados"))
        print(sum_percentage)
        if len(sum_percentage)>=1:
            total_sum_percentage=sum_percentage[0][1]
            total_percentage= participation_percentage + total_sum_percentage
            print(total_percentage)
            if total_percentage > 100:
                return returnCodes.custom_response(None, 400, 4001, "EMP-7")
        

        fields_data,values_tuple=create_fields_values(req_data)

        try:
            BeneficiariesModel.post_beneficiary(self, fields_data,values_tuple)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-8")
        
        return returnCodes.custom_response(req_data, 201, 2011, "EMP-1")

    ################################
    
    ######### UPDATE ONE PRODUCT#######
    @nsBeneficieries.doc("Update Beneficiary")
    @nsBeneficieries.expect(beneficiaryPatchApi)
    def patch(self):
        """Update one Beneficiary"""
        req_data = request.get_json(force=True)
        data=None
        try:
            data=beneficiary_schema.load(req_data, partial=True)
        except ValidationError as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-2", str(err))

        if "Fecha_Nacimiento" in req_data:
            current_age = date_birth(req_data)
            if current_age < 18 :
                return returnCodes.custom_response(None, 400, 4001, "EMP-14")

        employee_id = EmployeesModel.get_one_employee(self, data.get("Idempleados"))
        if len(employee_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-15")
        
        if "Porcentaje_Participacion" in req_data:
            participation_percentage=data.get("Porcentaje_Participacion")
            sum_percentage = BeneficiariesModel.get_sum_percentage(self, data.get("Idempleados"))
            print(sum_percentage)
            if len(sum_percentage)>=1:
                total_sum_percentage=sum_percentage[0][1]
                total_percentage= participation_percentage + total_sum_percentage
                print(total_percentage)
                if total_percentage > 100:
                    return returnCodes.custom_response(None, 400, 4001, "EMP-7")

        beneficiary_id = BeneficiariesModel.get_one_beneficiary(self, data.get("id"))

        if len(beneficiary_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-9")
        field_idempleados = data.get("Idempleados")
        print(field_idempleados)
        if field_idempleados != None:
            employee_id = EmployeesModel.get_one_employee(self, data.get("Idempleados"))
            if len(employee_id)==0:
                return returnCodes.custom_response(None, 404, 4041, "EMP-10")

        fields_data,values_tuple=create_fields_values(req_data)
        try:
            BeneficiariesModel.update_beneficiary(self, fields_data,values_tuple)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-11")
        
        return returnCodes.custom_response(req_data, 200, 2012, "EMP-6")

    ##########################################

##############DELETE ONE PRODUCT
@nsBeneficieries.route("/<id>")
@nsBeneficieries.param("id", "The id identifier")
@nsBeneficieries.response(404, "registro no encontrado")
class OneBeneficiary(Resource):
    @nsBeneficieries.doc("delete Beneficiary")
    def delete(self, id):
        """Delete one Beneficiary"""
        beneficiary_id = BeneficiariesModel.get_one_beneficiary(self, id)
        if len(beneficiary_id)==0:
            return returnCodes.custom_response(None, 404, 4041, "EMP-9")
        try:
            BeneficiariesModel.delete_one_beneficiary(self, id)
        except Exception as err:
            return returnCodes.custom_response(None, 400, 4001, "EMP-12")

        return returnCodes.custom_response(None, 200, 2012, "EMP-13")
###############################
