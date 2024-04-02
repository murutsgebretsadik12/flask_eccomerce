let menu = document.querySelector('#menu_icon');
console.log(menu);

let navlist = document.querySelector('.navlist');
console.log(navlist)

menu.onclick = () => {
	console.log("Menu clicked");
	menu.classList.toggle('bx-x');
	navlist.classList.toggle('open');
}

    window.onscroll = () => {
	menu.classList.remove('bx-x');
	navlist.classList.remove('open');
}


document.getElementById("newsletterForm").onsubmit = function() {
	var username = document.getElementsByName("username")[0].value;
	var password = document.getElementsByName("password")[0].value;

	// Username validation
	if (username.length < 3 || username.length > 20) {
		document.getElementById("usernameError").innerHTML = "Username must be between 3 and 20 characters";
		return false; // Prevent form submission
	} else {
		document.getElementById("usernameError").innerHTML = "";
	}

	// Password validation
	if (password.length < 6) {
		document.getElementById("passwordError").innerHTML = "Password must be at least 6 characters long";
		return false; // Prevent form submission
	} else {
		document.getElementById("passwordError").innerHTML = "";
	}

	return true; // Allow form submission
};
