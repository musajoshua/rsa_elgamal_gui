var reader = new FileReader();

function readText(that) {
	if (that.files && that.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
			var output = e.target.result;

			document.getElementById("textarea1").innerHTML = output;
		};
		reader.readAsText(that.files[0]);
	}
}
