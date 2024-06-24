window.addEventListener("load", ()=>{
    let button_select_create_turn = document.getElementById("select_create_turn");
    let check_select_create_turn = document.getElementsByName("pet_check");
    let url_page = window.location.href
    let url_complete = ""
    let select_pet_id = ""
    let select_validation = false

    button_select_create_turn.addEventListener("click", ()=>{        
        /* if (url_actual.endsWith("date/")) {
            url_final = url_actual + date_turn.value + "/"
        } else {
            let nueva_url = url_actual.substring(0,url_actual.lastIndexOf("date/") + 5);
            url_final = nueva_url + date_turn.value + "/"
        }
        window.location.assign(url_final); */
        for (let i = 0; i < check_select_create_turn.length; i++) {
            if (check_select_create_turn[i].checked == true) {
                select_pet_id = check_select_create_turn[i].value
                select_validation = true;
                break;
            }            
        }
        if (select_validation == false){
            alert("Debe seleccionar una mascota para el turno")
        } else {
            url_complete = url_page + select_pet_id + "/attention/"
            window.location.assign(url_complete);
        }
    })
})