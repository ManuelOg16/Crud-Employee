from flask import Response, json

# Diccionario de return codes
app_codes = {
    "EMP-1": "Creado exitosamente",
    "EMP-2": "Error en la formación del json de entrada",
    "EMP-3": "Consulta exitosa",
    "EMP-4": "Recurso no encontrado",
    "EMP-5": "El recurso ya existe",
    "EMP-6": "Recurso actualizado correctamente",
    "EMP-7": "El porcentaje de participacion sobrepasa el 100% para el empleado",
    "EMP-8": "Error al crear",
    "EMP-9": "Beneficiario no encontrado",
    "EMP-10": "Empleado no encontrado",
    "EMP-11": "Error al actualizar",
    "EMP-12": "Error al borrar",
    "EMP-13": "Borrado exitoso",
    "EMP-14": "Requisito ser mayor de edad",
    "EMP-15": "Empleado no encontrado",


}


def custom_response(res, status_code, yt_code, app_code, message="", item=""):
    """
    Custom Response Function
    """
    messageSent = ""
    if message == "":
        messageSent = app_codes[app_code]
    else:
        messageSent = message
    if(item!=""):
        messageSent = messageSent + ", " + item
    response = {
        "yt_code": yt_code,
        "app_code": app_code,
        "message": messageSent,
        "data": res,
    }
    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status_code,
    )
