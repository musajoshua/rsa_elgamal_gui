submit = async () => {
	// get public keys
	// let public_keys = document.getElementById("public_key").value;
	let private_keys = [198131, 120013];
	// get file for encryption
	let file = document.getElementById("encrypted_file").files[0];
	if (!file) {
		alert("A File must have been selected !");
		return;
	}

	// console.log(file);

	let reader = new FileReader();
	reader.onload = async () => {
		let dataURL = await reader.result;
		// console.log(dataURL);
		eel.rsa_decrypt(
			private_keys,
			dataURL
		)((data) => {
			console.log(data);
			let cipher_string = data[0];
			let time_taken = data[1];
			var blob = new Blob([cipher_string], {
				type: "text/plain;charset=utf-8",
			});
			saveAs(blob, "enc.jpg");
			document.getElementById("time_taken_to_decrypt").value = time_taken;
			// document.getElementById("encrypted_file").value = cipher_string;
		});
	};
	reader.readAsDataURL(file);
	// let dd = await reader.result;
	// console.log(dd);

	// let fileURL = URL.createObjectURL(file);
	// console.log(file);

	// eel.rsa_encrypt(
	// 	public_keys,
	// 	file
	// )((data) => {
	// 	// alert(data);
	// 	console.log(data);
	// });
};

download = () => {
	let cipher_string = document.getElementById("encrypted_file").value;
	if (!cipher_string) {
		alert("No file to download");
		return;
	}

	var blob = new Blob([cipher_string], { type: "text/plain;charset=utf-8" });
	saveAs(blob, "enc.enc");
};
