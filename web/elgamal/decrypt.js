let fileData1;
let fileData2;
let extn;

$(document).ready(function () {
	$("#enc_file_1").on("change", async function () {
		var path = $(this)[0].value;
		extn = path.substring(path.lastIndexOf(".") + 1).toLowerCase();
		if (typeof FileReader != "undefined") {
			fileData1 = await readFile($(this)[0].files[0]);

			document.getElementById("encrypted_file1").value = fileData1;
		} else {
			alert("This Application does not support FileReader.");
		}
	});
	$("#enc_file_2").on("change", async function () {
		var path = $(this)[0].value;
		extn = path.substring(path.lastIndexOf(".") + 1).toLowerCase();
		if (typeof FileReader != "undefined") {
			fileData2 = await readFile($(this)[0].files[0]);

			document.getElementById("encrypted_file2").value = fileData2;
		} else {
			alert("This Application does not support FileReader.");
		}
	});
});

submit = async () => {
	// get private keys
	let private_keys = document.getElementById("private_key").value;
	if (!private_keys) {
		alert("Please Enter Your Public Key");
		return;
	}
	const [n, e] = private_keys.split(",");

	private_keys = [parseInt(n), parseInt(e)];
	// get file for encryption
	let cipher_string1 = document.getElementById("enc_file_1").files[0];
	let cipher_string2 = document.getElementById("enc_file_2").files[0];
	if (!cipher_string1 || !cipher_string2) {
		alert("Please Select the two cipher files !");
		return;
	}

	eel.elgamal_decrypt(
		private_keys,
		fileData1,
		fileData2
	)((data) => {
		let plain_string = data[0];
		let time_taken = data[1];

		document.getElementById("time_taken_to_decrypt").value = time_taken;

		var file_holder = $("#file-holder");

		if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
			$("<img />", {
				id: "plainfile",
				src: plain_string,
				width: "100%",
				height: "100%",
			}).appendTo(file_holder);
			file_holder.show();
		} else if (extn == "mp3" || extn == "flac") {
			const source = $("<source />", {
				id: "plainfile",
				src: plain_string,
			});
			const audio = $("<audio controls />", {
				// width: "100%",
				height: "300px",
			});
			source.appendTo(audio);
			audio.appendTo(file_holder);
			file_holder.show();
		} else if (extn == "mp4" || extn == "mov") {
			const source = $("<source />", {
				id: "plainfile",
				src: plain_string,
			});
			const video = $("<video controls />", {
				// width: "100%",
				height: "300px",
			});
			source.appendTo(video);
			video.appendTo(file_holder);
			file_holder.show();
		} else {
			alert("Pls select only images, video and audio");
		}
	});
};

download = () => {
	let dataURI = document.getElementById("plainfile").src;
	if (!dataURI) {
		alert("No file to download");
		return;
	}

	var byteString = atob(dataURI.split(",")[1]);

	// separate out the mime component
	var mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0];

	// write the bytes of the string to an ArrayBuffer
	var ab = new ArrayBuffer(byteString.length);
	var ia = new Uint8Array(ab);
	for (var i = 0; i < byteString.length; i++) {
		ia[i] = byteString.charCodeAt(i);
	}
	let blob = new Blob([ab], { type: mimeString });

	saveAs(blob, `dec.${mimeString.split("/")[1]}`);
};
