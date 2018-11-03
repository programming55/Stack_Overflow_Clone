function validate() {
	uid = document.getElementById('userID');
	pwd = document.getElementById("loginPassword");
	cpwd = document.getElementById("loginPassword2");
	if (cpwd.value != pwd.value) {
		alert("Both Passwords must match!");
	}
}
