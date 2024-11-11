window.addEventListener("load", ()=>{
    let button_select_create_professional = document.getElementById("select_create_professional");
    let check_select_create_professional = document.getElementsByName("professional_check");
    let url_page = window.location.href
    let url_complete = ""
    let select_professional_id = ""
    let select_validation = false

    button_select_create_professional.addEventListener("click", ()=>{
        for (let i = 0; i < check_select_create_professional.length; i++) {
            if (check_select_create_professional[i].checked == true) {
                select_professional_id = check_select_create_professional[i].value
                select_validation = true;
                break;
            }            
        }
        if (select_validation == false){
            alert("Debe seleccionar un profesional para atención");
        } else {
            
            let date = new Date() // genera la fecha y hora actual
            
            let hour = date.getHours() // obtiene la hora correspondiente a la fecha de la variable date
            if (hour >= 14) {
                var day = date.getDate() + 1 // obtiene el día correspondiente a la fecha de la variable date
            } else {
                var day = date.getDate()
            }
            let month = date.getMonth() + 1 // obtiene el mes correspondiente a la fecha de la variable date (suma 1 porque los valores comienzan con 0, rango [0:11])
            let year = date.getFullYear() // obtiene el año correspondiente a la fecha de la variable date
            
            if (month <= 9){
                var url_date = year + "-" + "0" + month + "-" + day
            } else {
                var url_date = year + "-" + month + "-" + day
            }
            
            // genera la nueva url para direccionar a la página
            url_complete = url_page + select_professional_id + "/date/" + url_date + "/";
            
            window.location.assign(url_complete);
        }
    })
})