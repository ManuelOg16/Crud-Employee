$.ajax({
    url: "http://127.0.0.1:5000/api/v1/Employees",
    type: 'GET',
    success: function(res) {
        let datos = res.data;
        var filas = res.data.length;
        console.log(datos);
        for (  indice = 0 ; indice < filas; indice++){ //cuenta la cantidad de registros
			var nuevafila= "<tr><td><ahref>" + 
			res.data[indice].id + "</td><td>"+
            res.data[indice].Nombre+ "</td><td>" +
            res.data[indice].Apellidos+ "</td><td>" +
            res.data[indice].Fecha_Nacimiento+ "</td><td>" +
            res.data[indice].Numero_Empleado+ "</td><td>"+
            res.data[indice].Curp+ "</td><td>"+
            res.data[indice].Ssn+ "</td><td>"+
            res.data[indice].Telefono+ "</td><td>"+
            res.data[indice].Nacionalidad+ "</td><td>"
			$("#tabla_resultados").append(nuevafila)}
    }
});

$.ajax({
    url: "http://127.0.0.1:5000/api/v1/Beneficiaries",
    type: 'GET',
    success: function(res) {
        let datos = res.data;
        var filas = res.data.length;
        console.log(datos);
        for (  indice = 0 ; indice < filas; indice++){ //cuenta la cantidad de registros
			var nuevafila= "<tr><td>" +
			res.data[indice].id + "</td><td>"+
            res.data[indice].Nombre+ "</td><td>" +
            res.data[indice].Apellidos+ "</td><td>" +
            res.data[indice].Fecha_Nacimiento+ "</td><td>" +
            res.data[indice].Curp+ "</td><td>"+
            res.data[indice].Ssn+ "</td><td>"+
            res.data[indice].Telefono+ "</td><td>"+
            res.data[indice].Nacionalidad+ "</td><td>"+
            res.data[indice].Porcentaje_Participacion+ "</td><td>"+
            res.data[indice].Idempleados+ "</td><td>"
			$("#tabla_beneficiarios").append(nuevafila)}
    }
});

// setInterval('index()',1000); 