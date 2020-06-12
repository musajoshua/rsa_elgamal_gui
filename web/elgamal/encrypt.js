$(document).ready(function () {
	$("#fileUpload").on("change", function () {
		var imgPath = $(this)[0].value;
		var extn = imgPath
			.substring(imgPath.lastIndexOf(".") + 1)
			.toLowerCase();
		var file_holder = $("#file-holder");
		file_holder.empty();
		if (typeof FileReader != "undefined") {
			if (
				extn == "gif" ||
				extn == "png" ||
				extn == "jpg" ||
				extn == "jpeg"
			) {
				var reader = new FileReader();
				reader.onload = function (e) {
					$("<img />", {
						src: e.target.result,
						width: "100%",
						height: "100%",
					}).appendTo(file_holder);
				};
				file_holder.show();
				reader.readAsDataURL($(this)[0].files[0]);
			} else {
				alert("Pls select only images");
			}
		} else {
			alert("This Application does not support FileReader.");
		}
	});
});
