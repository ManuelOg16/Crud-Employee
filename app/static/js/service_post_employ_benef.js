$(document).ready(function() {
    $('#formulario_employee').submit(function(e) {
        e.preventDefault();
        let datos = {
            Nombre: $('#Nombre').val(),
            Apellidos:$('#Apellidos').val(),
            Fecha_Nacimiento:$('#Fecha_Nacimiento').val(),
            Numero_Empleado:parseInt($('#Numero_Empleado').val(),10),
            Curp:$('#Curp').val(),
            Ssn:parseInt($('#Ssn').val(),10),
            Telefono:parseInt($('#Telefono').val(),10),
            Nacionalidad:$('#Nacionalidad').val()
            }
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Employees',
            type: "POST",
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
    $('#formulario_beneficiary').submit(function(e) {
        e.preventDefault();
        let datos = {
            Nombre: $('#Nombre').val(),
            Apellidos:$('#Apellidos').val(),
            Fecha_Nacimiento:$('#Fecha_Nacimiento').val(),
            Curp:$('#Curp').val(),
            Ssn:parseInt($('#Ssn').val(),10),
            Telefono:parseInt($('#Telefono').val(),10),
            Nacionalidad:$('#Nacionalidad').val(),
            Porcentaje_Participacion:parseInt($('#Porcentaje_Participacion').val(),10),
            Idempleados:parseInt($('#Idempleados').val(),10),
            }
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Beneficiaries',
            type: "POST",
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
