// $(document).ready(function () {
// 	$("#file").on("change", function () {
// 		var imgPath = $(this)[0].value;
// 		var extn = imgPath
// 			.substring(imgPath.lastIndexOf(".") + 1)
// 			.toLowerCase();
// 		var file_holder = $("#file-holder");
// 		file_holder.empty();
// 		if (typeof FileReader != "undefined") {
// 			if (
// 				extn == "gif" ||
// 				extn == "png" ||
// 				extn == "jpg" ||
// 				extn == "jpeg"
// 			) {
// 				var reader = new FileReader();
// 				reader.onload = function (e) {
// 					$("<img />", {
// 						src: e.target.result,
// 						width: "100%",
// 						height: "100%",
// 					}).appendTo(file_holder);
// 				};
// 				file_holder.show();
// 				reader.readAsDataURL($(this)[0].files[0]);
// 			} else {
// 				alert("Pls select only images");
// 			}
// 		} else {
// 			alert("This Application does not support FileReader.");
// 		}
// 	});
// });

submit = async () => {
	// get public keys
	// let public_keys = document.getElementById("public_key").value;
	let public_keys = [198131, 5197];
	// get file for encryption
	let file = document.getElementById("plain_file").files[0];
	if (!file) {
		alert("A File must have been selected !");
		return;
	}

	let reader = new FileReader();
	reader.onload = async () => {
		let dataURL = await reader.result;
		// console.log(dataURL);
		// let dd = dataURL.substr(dataURL.indexOf(",") + 1);
		// dataURL === dd ? console.log(true) : console.log(false);
		// console.log(dd);
		let fso = CreateObject("Scripting.FileSystemObject");
		let s = fso.CreateTextFile("C:\test.txt", True);
		s.writeline("HI");
		s.writeline("Bye");
		s.writeline("-----------------------------");
		s.Close();
		// let blob = new Blob([dataURL], { type: "application/octet-binary" });

		// saveAs(blob, "plane.png");
		eel.rsa_encrypt(
			public_keys,
			dataURL
		)((data) => {
			let cipher_string = data[0];
			let time_taken = data[1];

			document.getElementById("time_taken_to_encrypt").value = time_taken;
			document.getElementById("encrypted_file").value = cipher_string;
		});
	};
	reader.readAsText(file);
};

download = () => {
	let cipher_string = document.getElementById("encrypted_file").value;
	if (!cipher_string) {
		alert("No file to download");
		return;
	}

	var blob = new Blob([cipher_string], { type: "text/plain;charset=utf-8" });
	saveAs(blob, "enc.txt");
};
