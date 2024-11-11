window.addEventListener("load", ()=>{
    let button_search_date = document.getElementById("search_date");
    let date_turn = document.getElementById("date_turn");
    let url_actual = window.location.href
    let url_final = ""

    button_search_date.addEventListener("click", ()=>{
        if (url_actual.endsWith("date/")) {
            url_final = url_actual + date_turn.value + "/"
        } else {
            let nueva_url = url_actual.substring(0,url_actual.lastIndexOf("date/") + 5);
            url_final = nueva_url + date_turn.value + "/"
        }
        window.location.assign(url_final);
    })
})