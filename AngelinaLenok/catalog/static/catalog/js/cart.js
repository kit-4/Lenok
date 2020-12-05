var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var pictureId = this.dataset.id
    var action = this.dataset.action
    console.log('pictureId:', pictureId, 'action', action)
    console.log('USER:', user)
    updateUserOrder(pictureId, action)
    }
  )}

function updateUserOrder(pictureId, action){
	httpRequest = new XMLHttpRequest();
	httpRequest.open("POST", "/update_item", true)
	httpRequest.send(JSON.stringify({"pictureId": pictureId, "action":action}))

	httpRequest.onreadystatechange = function(){
		if(httpRequest.readyState == 4 && httpRequest.status == 200) {
			json = JSON.parse(httpRequest.response)
			number = json.number
			id = json.id
			total = json.total
			action = json.action
			document.getElementById("cart").innerHTML = ' ' +  + number  
			//in case we are on the cart page:
			if (location.href == "http://127.0.0.1:8000/cart" && action == 'remove'){
				document.getElementById(id).remove()
				document.getElementById("total").innerHTML = 'Total ' + total + ' RUB'
			}
    }
	};
}

