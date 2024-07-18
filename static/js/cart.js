var updateBtns = document.getElementsByClassName('update-cart')
var favBtns = document.getElementsByClassName('btn-fav')
var logout = document.getElementById('li-logout')
var signup = document.getElementById('li-signup')
var login = document.getElementById('li-login')

function noCookies(productId, action){
	var url = '/payments/update_item/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken': csrftoken,
		}, 
		body:JSON.stringify({'productId':productId, 'action':action})
	})
	.then((response) => {
		return response.json();
	})
	.then(() => {
		location.reload(true);
	});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated... ')

	if (action == 'add'){
		if (cart[productId] == undefined){
			cart[productId] = {'quantity':1};
		}else{
			cart[productId]['quantity'] += 1;
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	/* console.log('CART:', cart) */
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/";
	
	location.reload();
}

function addFavorites(productId, action){

	if (action == 'false'){
		fav[productId] = true;
	}else{
		fav[productId] = false;
	}

	/* console.log('FAVS:', fav) */
	document.cookie ='fav=' + JSON.stringify(fav) + ";domain=;path=/";
}

/* Se agrega evento a botones de "Add to cart" en el index */
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		if (user == 'AnonymousUser'){
			addCookieItem(productId, action);
		}else{
			noCookies(productId, action)
		}
	})
}

/* Se agrega evento a botones de "Favorites" en el index */
for (i = 0; i < favBtns.length; i++) {
	favBtns[i].addEventListener('click', function(){
		if (user == 'AnonymousUser'){
			alert("Debes loguearte para gestionar favoritos")
		}else{
			var productId = this.dataset.product;
			addFavorites(productId, this.dataset.value );
			if (this.dataset.value == 'false'){
				this.dataset.value = true;
			}else{
				this.dataset.value = false;
			}
		}
	})
}

/* Se crea un evento para el boton de Logout con el fin de vaciar la lista de favoritos */
if(logout!=null){
	logout.addEventListener('click', ()=>{
		fav = {};
		cart = {};
		document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
		document.cookie = 'fav=' + JSON.stringify(fav) + ";domain=;path=/";
	})
}

if(login!=null){
	login.addEventListener('click', ()=>{
		fav = {};
		cart = {};
		document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
		document.cookie = 'fav=' + JSON.stringify(fav) + ";domain=;path=/";
	})
}