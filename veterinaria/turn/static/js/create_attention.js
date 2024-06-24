window.addEventListener("load", ()=>{
    let button_select_create_attention = document.getElementById("select_create_attention");
    let check_select_create_attention = document.getElementsByName("attention_check");
    let url_page = window.location.href
    let url_complete = ""
    let select_attention_id = ""
    let select_validation = false

    button_select_create_attention.addEventListener("click", ()=>{
        for (let i = 0; i < check_select_create_attention.length; i++) {
            if (check_select_create_attention[i].checked == true) {
                select_attention_id = check_select_create_attention[i].value
                select_validation = true;
                break;
            }            
        }
        if (select_validation == false){
            alert("Debe seleccionar un tipo de atención para la mascota");
        } else {
            url_complete = url_page + select_attention_id + "/professional/"
            window.location.assign(url_complete);
        }
    })
})