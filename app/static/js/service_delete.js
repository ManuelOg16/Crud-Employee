$(document).ready(function() {
    $('#formulario_employee_delete').submit(function(e) {
        e.preventDefault();
        let datos = {
            id: $('#id_empleado').val(),
            Nombre: $('#Nombre_del').val(),
            }
        let valuess=(Object.values(datos));
        id=valuess[0]
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Employees/'+id,
            type: "DELETE",
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
    $('#formulario_beneficiary_delete').submit(function(e) {
        e.preventDefault();
        let datos = {
            id: $('#id_beneficiario').val(),
            Nombre: $('#Nombre_del').val(),
            }
        let valuess=(Object.values(datos));
        id=valuess[0]
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v1/Beneficiaries/'+id,
            type: "DELETE",
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