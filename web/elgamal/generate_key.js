submit = () => {
	eel.elgamal_key_gen()((data) => {
		const [pub_key, pri_key] = data;

		// Display key
		document.getElementById("public_key").innerHTML = pub_key;
		document.getElementById("private_key").innerHTML = pri_key;
	});
};
