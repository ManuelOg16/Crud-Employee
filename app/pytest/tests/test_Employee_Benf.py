import requests

from app.pytest.helpers import HEADERS

var_id_employee=1
var_id_beneficiary=1
def test_post_employees(endpoint):
    assert len(endpoint) > 0
    url = f"{endpoint}/api/v1/Employees"
    json = {
            "Nombre": "string",
            "Apellidos": "string",
            "Fecha_Nacimiento": "2002-11-06",
            "Numero_Empleado": 0,
            "Curp": "string",
            "Ssn": 0,
            "Telefono": 3008160902,
            "Nacionalidad": "string"
            }
    response = requests.post(url, headers=HEADERS, json=json)
    try:
        response_data = response.json()
    except:
        response_data= {}
    assert response.status_code == 201
    assert response_data["app_code"] == "EMP-1"
    assert response_data["yt_code"] == 2011


def test_post_beneficiary(endpoint):
    assert len(endpoint) > 0
    url = f"{endpoint}/api/v1/Beneficiaries"
    json = {
            "Nombre": "string",
            "Apellidos": "string",
            "Fecha_Nacimiento": "2002-11-06",
            "Curp": "string",
            "Ssn": 0,
            "Telefono": 3008160902,
            "Nacionalidad": "string",
            "Porcentaje_Participacion": 1,
            "Idempleados": var_id_employee
            }
    response = requests.post(url, headers=HEADERS, json=json)
    try:
        response_data = response.json()
    except:
        response_data= {}
    assert response.status_code == 201
    assert response_data["app_code"] == "EMP-1"
    assert response_data["yt_code"] == 2011


########################test beneficiaries
def test_get_beneficiaries(endpoint):
    url = f"{endpoint}/api/v1/Beneficiaries"
    response = requests.get(url, headers=HEADERS)
    try:
        response_data = response.json()
    except:
        response_data = {}
        return
    return response_data["data"][0]

def test_patch_beneficiary(endpoint):
    assert len(endpoint) > 0
    url = f"{endpoint}/api/v1/Beneficiaries"
    json = {
            "id": var_id_beneficiary,
            "Nombre": "update",
            "Idempleados": var_id_employee
            }
    response = requests.patch(url, headers=HEADERS, json=json)
    try:
        response_data = response.json()
    except:
        response_data = {}
    assert response.status_code == 200
    assert response_data["app_code"] == "EMP-6"
    assert response_data["yt_code"] == 2012

def test_delete_beneficiary(endpoint):
    assert len(endpoint) > 0
    id_b=var_id_beneficiary
    url = f"{endpoint}/api/v1/Beneficiaries/{id_b}"
    response = requests.delete(url)
    try:
        response_data = response.json()
    except:
        response_data = {}
    assert response.status_code == 200
    assert response_data["app_code"] == "EMP-13"
    assert response_data["yt_code"] == 2012
###############################################

########################test employees
def test_get_employees(endpoint):
    url = f"{endpoint}/api/v1/Employees"
    response = requests.get(url, headers=HEADERS)
    try:
        response_data = response.json()
    except:
        response_data = {}
        return
    return response_data["data"][0]

def test_patch_employees(endpoint):
    assert len(endpoint) > 0
    url = f"{endpoint}/api/v1/Employees"
    json = {
            "id": var_id_employee,
            "Nombre": "update"
            }
    response = requests.patch(url, headers=HEADERS, json=json)
    try:
        response_data = response.json()
    except:
        response_data = {}
    assert response.status_code == 200
    assert response_data["app_code"] == "EMP-6"
    assert response_data["yt_code"] == 2012

def test_delete_employees(endpoint):
    assert len(endpoint) > 0
    id_e=var_id_employee
    url = f"{endpoint}/api/v1/Employees/{id_e}"
    response = requests.delete(url)
    try:
        response_data = response.json()
    except:
        response_data = {}
    assert response.status_code == 200
    assert response_data["app_code"] == "EMP-13"
    assert response_data["yt_code"] == 2012
#######################