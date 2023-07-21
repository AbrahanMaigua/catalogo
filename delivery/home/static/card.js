document.addEventListener('keydown', function(event) {
	let Auxtext = '';	
	let cal = document.getElementById("1455");
	let cat = document.getElementById('id_catidad');
	let key = event.key
	cat = eval(cat.value)
  
	if (isNaN(key) == false){
		//console.log(parseInt(key) + 9);
		//console.log(parseInt(cat) + 9);
		
		console.log(cal.textContent)
		Auxtext += cat;			
		cal.innerHTML = Auxtext + 'R$';
  
  
	}
  let ary =  Array('Delete','Backspace');
  if (key == 'Backspace'){
	  cal.innerHTML = "";
  
  };
  
	//console.log(isNaN(key))
  });
  
  