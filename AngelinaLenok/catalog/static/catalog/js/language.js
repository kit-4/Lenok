  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


var updateBtns = document.getElementsByClassName('change_language')

for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var language = this.dataset.language
    console.log('language', language)
    updateLanguage(language, getCookie("csrftoken"))
    }
  )}


////function updateLanguage(language, CSRF_token){
////	httpRequest = new XMLHttpRequest();
	//httpRequest.open("POST", "/i18n/setlang/", true)
	//httpRequest.send("csrfmiddlewaretoken="+CSRF_token+"&next=&language="+language)

	//httpRequest.onreadystatechange = function(){
	//	if(httpRequest.readyState == 4 && httpRequest.status == 200) {
   //   location.reload();
    //}
	//};
//}

function updateLanguage(language){
const request = new Request(
    "/i18n/setlang/",
    {headers: {'X-CSRFToken': get_cookie('csrftoken')}}
);

fetch(request, {
    method: 'POST',
    mode: 'same-origin'  // Do not send CSRF token to another domain.
}, 
  body: ("next=&language="+language).then(function(response) {
    location.reload();
}));}
