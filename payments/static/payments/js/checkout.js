var form = document.getElementById('checkout-form');

csrftoken = form.getElementsByTagName("input")[0].value;
console.log('New token: ',form.getElementsByTagName("input")[0].value);

document.getElementById("btn-continue").addEventListener('click', function(e){
    e.preventDefault();
    console.log('Data submitted...');
    document.getElementById('btn-continue').classList.add("hidden");
    document.getElementById('payment-info').classList.remove("hidden");
})

document.getElementById('make-payment').addEventListener('click', function(e){
        alert('Transaction completed');
        cart = {};
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
})

/* ---------------- VALIDACION DEL FORMULARIO ---------------- */

const inputs = document.querySelectorAll('#checkout-form input');

const expresiones = {
	user: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	name: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    last_name: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    address: /^[a-zA-Z0-9À-ÿ\s\_\-\#]{1,40}$/, // Letras, numeros, guion y guion_bajo
    city: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    state: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	phone: /^\d{7,14}$/, // 7 a 14 numeros.
    postal_code: /^\d{5,8}$/ // 7 a 14 numeros.
}

const campos = {
	user: false,
	name: false,
    last_name: false,
	password: false,
	email: false,
    address: false,
    city: false,
    state: false,
	phone: false,
    postal_code: false,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "name":
			validarCampo(expresiones.name, e.target, 'name');
		break;
        case "last_name":
			validarCampo(expresiones.last_name, e.target, 'last_name');
		break;
		case "email":
			validarCampo(expresiones.email, e.target, 'email');
		break;
        case "address":
			validarCampo(expresiones.address, e.target, 'address');
		break;
        case "city":
			validarCampo(expresiones.city, e.target, 'city');
		break;
        case "state":
			validarCampo(expresiones.state, e.target, 'state');
		break;
		case "postal_code":
			validarCampo(expresiones.postal_code, e.target, 'postal_code');
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`wrapper-${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`wrapper-${campo}`).classList.add('formulario__grupo-correcto');
		/* document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo'); */
		campos[campo] = true;
	} else {
        console.log('Si entro weon y esta mal')
		document.getElementById(`wrapper-${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`wrapper-${campo}`).classList.remove('formulario__grupo-correcto');
		/* document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo'); */
		campos[campo] = false;
	}
}

const validarPassword2 = () => {
	const inputPassword1 = document.getElementById('password');
	const inputPassword2 = document.getElementById('password2');

	if(inputPassword1.value !== inputPassword2.value){
		document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos['password'] = false;
	} else {
		document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos['password'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

/* form.addEventListener('submit', (e) => {
	e.preventDefault();

	const terminos = document.getElementById('terminos');
	if(campos.user && campos.name && campos.password && campos.email && campos.phone && terminos.checked ){
		form.reset();

		document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
		setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);

		document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
			icono.classList.remove('formulario__grupo-correcto');
		});
	} else {
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
}); */