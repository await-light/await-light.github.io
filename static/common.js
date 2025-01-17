function get_custacc() {
	var a = window.location.href.split("/");
	return a[a.length-1].split(".")[0];
}

function get_platform() {
	var a = window.location.href.split("/");
	return a[a.length-2];
}

window.onload = (event) => {
	document.getElementsByTagName("iframe")[0].src = `https://ynetwork.site/cust/${get_platform()}?custacc=${get_custacc()}`;
};