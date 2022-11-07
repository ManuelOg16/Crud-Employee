$(document).ready(function() {
    $('#formulario_employee_update').submit(function(e) {
        e.preventDefault();
        let datos = {
            id: $('#id').val()
            }
        if ($('#Nombre_up').val().length == 0){
             //pass
        } else {
            let nombre =$('#Nombre_up').val();
            datos.Nombre = nombre;
        }
        if ($('#Apellidos_up').val().length == 0){
            //pass
        } else {
            let apellidos =$('#Apellidos_up').val();
            datos.Apellidos=apellidos
        }
        if ($('#Fecha_Nacimiento_up').val().length == 0){
                //pass
        } else {
            let fecha_nacimiento =$('#Fecha_Nacimiento_up').val();
            datos.Fecha_Nacimiento = fecha_nacimiento ;
        }
        if ($('#Numero_Empleado_up').val().length == 0){
            //pass
        } else {
            let numero_empleado =$('#Numero_Empleado_up').val();
            datos.Numero_Empleado=numero_empleado
        }
        if ($('#Curp_up').val().length == 0){
            //pass
        } else {
            let curp =$('#Curp_up').val();
            datos.Curp = curp;
        }
        if ($('#Ssn_up').val().length == 0){
            //pass
        } else {
            let ssn =$('#Ssn_up').val();
            datos.Ssn=ssn
        }
        if ($('#Telefono_up').val().length == 0){
            //pass
        } else {
            let telefono =$('#Telefono_up').val();
            datos.Telefono = telefono;
        }
        if ($('#Nacionalidad_up').val().length == 0){
            //pass
        } else {
            let nacionalidad =$('#Nacionalidad_up').val();
            datos.Nacionalidad=nacionalidad
        }
        console.log(datos)
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Employees',
            type: "PATCH",
            ContentypeType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(datos),
            success: function(response)
            {
                // document.getElementById('submitForm').disabled = false;
                $('#responseValue').html(response.message);
                setInterval("location.reload()",1000);
            },
            error:function( jqXHR, textStatus, errorThrown ) {
                $('#responseValue').html(jqXHR.responseJSON.message);
            }
        });
        });
});

$(document).ready(function() {
    $('#formulario_beneficiary_update').submit(function(e) {
        e.preventDefault();
            let datos = {
                id: $('#id').val()
                }
            if ($('#Nombre_up').val().length == 0){
                 //pass
            } else {
                let nombre =$('#Nombre_up').val();
                datos.Nombre = nombre;
            }
            if ($('#Apellidos_up').val().length == 0){
                //pass
            } else {
                let apellidos =$('#Apellidos_up').val();
                datos.Apellidos=apellidos
            }
            if ($('#Fecha_Nacimiento_up').val().length == 0){
                    //pass
            } else {
                let fecha_nacimiento =$('#Fecha_Nacimiento_up').val();
                datos.Fecha_Nacimiento = fecha_nacimiento ;
            }
            if ($('#Curp_up').val().length == 0){
                //pass
            } else {
                let curp =$('#Curp_up').val();
                datos.Curp = curp;
            }
            if ($('#Ssn_up').val().length == 0){
                //pass
            } else {
                let ssn =$('#Ssn_up').val();
                datos.Ssn=ssn
            }
            if ($('#Telefono_up').val().length == 0){
                //pass
            } else {
                let telefono =$('#Telefono_up').val();
                datos.Telefono = telefono;
            }
            if ($('#Nacionalidad_up').val().length == 0){
                //pass
            } else {
                let nacionalidad =$('#Nacionalidad_up').val();
                datos.Nacionalidad=nacionalidad
            }
            if ($('#Porcentaje_Participacion_up').val().length == 0){
                //pass
            } else {
                let porcentaje_participacion =$('#Porcentaje_Participacion_up').val();
                datos.Porcentaje_Participacion=porcentaje_participacion
            }
            if ($('#Idempleados_up').val().length == 0){
                //pass
            } else {
                let id_empleados =$('#Idempleados_up').val();
                datos.Idempleados=id_empleados
            }
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Beneficiaries',
            type: "PATCH",
            ContentypeType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(datos),
            success: function(response)
            {
                // document.getElementById('submitForm').disabled = false;
                $('#responseValue').html(response.message);
                setInterval("location.reload()",1000);
            },
            error:function( jqXHR, textStatus, errorThrown ) {
                $('#responseValue').html(jqXHR.responseJSON.message);
            }
        });
        });
});