let fileData;
let extn;

$(document).ready(function () {
	$("#encrypted_file").on("change", async function () {
		var imgPath = $(this)[0].value;
		extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
		var file_holder = $("#textarea1");
		file_holder.empty();
		if (typeof FileReader != "undefined") {
			fileData = await readFile($(this)[0].files[0]);

			document.getElementById("encrypted_file_view").value = fileData;
		} else {
			alert("This Application does not support FileReader.");
		}
	});
});

submit = async () => {
	// get private keys
	// let private_keys = document.getElementById("private_key").value;
	// if (!private_keys) {
	// 	alert("Please Enter Your Public Key");
	// 	return;
	// }
	// const [n, e] = private_keys.split(",");

	// private_keys = [parseInt(n), parseInt(e)];
	let private_keys = [20, 7];
	// get file for encryption
	let file = document.getElementById("encrypted_file").files[0];
	if (!file) {
		alert("A File must have been selected !");
		return;
	}

	eel.elgamal_decrypt(
		private_keys,
		fileData
	)((data) => {
		let plain_string = data[0];
		let time_taken = data[1];

		document.getElementById("time_taken_to_decrypt").value = time_taken;

		var file_holder = $("#file-holder");

		if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
			$("<img />", {
				src: plain_string,
				width: "100%",
				height: "100%",
			}).appendTo(file_holder);
			file_holder.show();
		} else if (extn == "mp3" || extn == "flac") {
			const source = $("<source />", {
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
	let dataURI = document.getElementById("file-holder").value;
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
