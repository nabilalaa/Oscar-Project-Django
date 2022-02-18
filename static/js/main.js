// side menu
let obtn = document.querySelector(".sidemenu__btn");
let menu = document.querySelector(".side__menu");
let cbtn = document.querySelector(".closemenu__btn");

obtn.onclick = function () {
	if (window.matchMedia("(max-width: 576px)").matches) {
		menu.style.width = `${window.innerWidth}px`;
		menu.style.right = "0";
	} else {
		menu.style.right = "0";
	}
};
cbtn.onclick = function () {
	if (window.matchMedia("(max-width: 576px)").matches) {
		menu.style.right = `-${window.innerWidth}px`;
	} else {
		menu.style.right = "-350px";
	}
};

/* drop menu */

let menubtn = document.querySelector(".btnmenu");
let dropMenu = document.querySelector(".drop__menu");

menubtn.onmouseover = function () {
	dropMenu.style.display = "block";
};

menubtn.onmouseout = function () {
	dropMenu.style.display = "none";
};

let sideMenuBtn = document.querySelector(".btnsidemenu");
let dropSideMenu = document.querySelector(".dropSide__menu");

sideMenuBtn.onclick = function () {
	if (dropSideMenu.style.display == "block") {
		dropSideMenu.style.display = "none";
	} else {
		dropSideMenu.style.display = "block";
	}
};
