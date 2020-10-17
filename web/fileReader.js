let readFile = (file) => {
	return new Promise((resolve, reject) => {
		var fr = new FileReader();
		fr.onload = () => {
			resolve(fr.result.toString());
		};
		fr.readAsDataURL(file);
	});
};
