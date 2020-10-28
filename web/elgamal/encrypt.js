let fileData;
let extn;

$(document).ready(function () {
	$("#plain_file").on("change", async function () {
		var imgPath = $(this)[0].value;
		extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
		var file_holder = $("#file-holder");
		file_holder.empty();
		if (typeof FileReader != "undefined") {
			fileData = await readFile($(this)[0].files[0]);
			if (
				extn == "gif" ||
				extn == "png" ||
				extn == "jpg" ||
				extn == "jpeg"
			) {
				$("<img />", {
					src: fileData,
					width: "100%",
					height: "100%",
				}).appendTo(file_holder);
				file_holder.show();
			} else if (extn == "mp3" || extn == "flac") {
				const source = $("<source />", {
					src: fileData,
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
					src: fileData,
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
		} else {
			alert("This Application does not support FileReader.");
		}
	});
});

submit = async () => {
	// get public keys
	let public_keys = document.getElementById("public_key").value;
	if (!public_keys) {
		alert("Please Enter Your Public Key");
		return;
	}
	const [n, e] = public_keys.split(",");

	public_keys = [parseInt(n), parseInt(e)];
	// get file for encryption
	let file = document.getElementById("plain_file").files[0];
	if (!file) {
		alert("A File must have been selected !");
		return;
	}

	eel.elgamal_encrypt(
		public_keys,
		fileData
	)((data) => {
		console.log(data);
		const cipher_string1 = data[0];
		const cipher_string2 = data[1];
		const time_taken = data[2];

		document.getElementById("time_taken_to_encrypt").value = time_taken;
		document.getElementById("encrypted_file1").value = cipher_string1;
		document.getElementById("encrypted_file2").value = cipher_string2;
	});
};

const getBlob = (dataURI) => {
	let byteString = atob(dataURI.split(",")[1]);

	// separate out the mime component
	let mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0];

	// write the bytes of the string to an ArrayBuffer
	let ab = new ArrayBuffer(byteString.length);
	let ia = new Uint8Array(ab);
	for (let i = 0; i < byteString.length; i++) {
		ia[i] = byteString.charCodeAt(i);
	}
	let blob = new Blob([ab], { type: mimeString });
	return [blob, mimeString.split("/")[1]];
};

download = () => {
	const dataURI1 = document.getElementById("encrypted_file1").value;
	const dataURI2 = document.getElementById("encrypted_file2").value;
	if (!dataURI1 || !dataURI2) {
		alert("No file to download");
		return;
	}

	const [blob1, extn1] = getBlob(dataURI1);
	const [blob2, extn2] = getBlob(dataURI2);

	saveAs(blob1, `enc1.${extn1}`);
	saveAs(blob2, `enc2.${extn2}`);
};
