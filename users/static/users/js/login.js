const   eyeOpenClose = document.querySelectorAll('.icon-eye'),
        field_passwords = document.querySelectorAll('#id_password');


eyeOpenClose.forEach(
    eyeIcon => {
        eyeIcon.addEventListener("click", ()=>{
            field_passwords.forEach(
                field_password =>{
                    if (field_password.type === "password"){
                        field_password.type = "text";

                        eyeIcon.src="/static/users/images/eye-on.png"

                    }else{
                        field_password.type = "password";
                        eyeIcon.src="/static/users/images/eye.png"
                    }
                }
            )
        })
    }
)