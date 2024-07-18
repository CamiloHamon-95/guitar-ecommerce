var checkbox = document.querySelectorAll('input[type=checkbox]');
let cb_all = document.getElementById('select-all');
let div_cb_all = document.getElementById('div-all-filter');
let btn_fav = document.getElementsByClassName('btn-fav');
let title_filter = document.getElementById('title-filter');
let cb_nav_responsive = document.getElementById('cb-nav-responsive');
let nav_responsive = document.getElementById('nav-responsive');
let menu_responsive = document.getElementById('menu-responsive');
let ul_opt_brands = document.getElementById('ul_opt_brands');
var cb_brands = document.getElementsByClassName('cb-brand');
var cb_models = document.getElementsByClassName('cb-model');
var guitar = document.getElementsByClassName('container-unique-guitar');
var list_models = document.getElementsByClassName('options_models');
/* --------------------------------> the function start here! <-------------------------------- */
/* --------------------------------> the function End here! <-------------------------------- */

    function hidde_models(flag, id_brand){
        for (let i = 0; i < list_models.length; i++) {
            if (list_models[i].getAttribute('data-brand')==id_brand) {
                if (flag) {
                    list_models[i].classList.remove("hidden")   
                }else{
                    list_models[i].classList.add("hidden")
                }
            }  
        }
    }

    function choose_model(flag, id_brand){
        for (let i = 0; i < cb_models.length; i++) {
            if (id_brand == cb_models[i].getAttribute('data-brand')) {
                if (flag) {
                    cb_models[i].checked = true;
                }else{
                    cb_models[i].checked = false;
                }
            }
        }
    }

    function choose_brand(flag){
        for (let i = 0; i < cb_brands.length; i++) {

            if (flag != cb_brands[i].checked) {
                cb_brands[i].click();
                choose_model(cb_brands[i].checked,cb_brands[i].id);
            }else{

            }
            
        }
    }

    function event_brands(){
        for (let i = 0; i < cb_brands.length; i++) {
            cb_brands[i].addEventListener('click', ()=>{
                hidde_models(cb_brands[i].checked,cb_brands[i].id);
                choose_model(cb_brands[i].checked,cb_brands[i].id);
                
                for (let j = 0; j < guitar.length; j++) {
                    if (cb_brands[i].id==guitar[j].getAttribute('data-brand')) {
                        if (!cb_brands[i].checked) {
                            guitar[j].classList.add("hidden")
                        }else{
                            guitar[j].classList.remove("hidden")
                        }
                    }
                }
                
            })
        }
    }

    function event_models(){
        for (let i = 0; i < cb_models.length; i++) {
            cb_models[i].addEventListener('click', ()=>{
                
                for (let j = 0; j < guitar.length; j++) {
                    if (cb_models[i].id==guitar[j].getAttribute('data-model')) {
                        if (!cb_models[i].checked) {
                            guitar[j].classList.add("hidden")
                        }else{
                            guitar[j].classList.remove("hidden")
                        }
                    }
                }

            })
        }
    }

    nav_responsive.addEventListener('click', ()=>{
        if(cb_nav_responsive.checked){
            cb_nav_responsive.checked = false;
            menu_responsive.classList.add("hidden");
        }else{
            cb_nav_responsive.checked = true;
            menu_responsive.classList.remove("hidden");
        }
    })

    if(cb_all!=null){
        cb_all.addEventListener('click', ()=>{
            choose_brand(cb_all.checked);
        })
    }

    if(title_filter!=null){
        title_filter.addEventListener('click', ()=>{
            if (title_filter.checked) {
                ul_opt_brands.classList.remove('hidden')
                div_cb_all.classList.remove('hidden')
            }else{
                ul_opt_brands.classList.add('hidden')
                div_cb_all.classList.add('hidden')
            }
        })
    }

    event_brands()
    event_models()