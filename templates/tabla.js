const elemento = document.getElementById("datos");
    cadena = "";
    const url = 'http://localhost:5000';
    fetch(url)
        .then(response => response.json())
        .then(data => {
            llenar_tabla(data);
        })

function eliminar_obj(boton){
    fetch('http://localhost:5000'+'/eliminar/'+ boton.id)
    .then(response => response.json())
    .then(data => {
            llenar_tabla(data);
    })
}

function llenar_tabla(data){
    console.log(data);
    cadena = "<table>";
    cadena += "<tr>";
    cadena += "<th> Id </th><th> Nombre </th><th> Cantidad </th><th> Valor </th><th> Opciones </th>";
    cadena += "</tr>";
    for (x in data){
        cadena += "<tr>";
        cadena += "<td>" + data[x].id + "</td><td> " + data[x].nombre + "</td><td>" + data[x].cantidad + "</td><td>" +  + data[x].valor + "</td>";
        cadena += "<td>" + "<input name = 'Eliminar' type = 'button' value = 'Eliminar' id="+ data[x].id + " onclick='eliminar_obj(this)'>"+ "</th>"
        cadena += "</tr>";
    }
    cadena += "</table>";
    elemento.innerHTML = cadena; 
}