// click the next button
var url = document.location.hostname;

if(url.includes("mail.google")) {
	let button = document.querySelector('[aria-label=Starsze]');
	button.click();
} else {
	alert('None action for this page');
}



