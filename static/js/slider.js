// slider

let nextBtn = document.querySelector(".next");
let previousBtn = document.querySelector(".previous");
let slide = document.querySelectorAll(".slide");
let pagination = document.querySelectorAll(".pagination li");

let num = 5;
pagination[4].style.backgroundColor = "#fca311";
let pag = 4;
function plus() {
	if (num > 1) {
		slide[--num].classList.add("hidden");
		pagination.forEach((e) => {
			e.style.backgroundColor = "#0000003a";
		});
		pagination[--pag].style.backgroundColor = "#fca311";
	}
}

function prev() {
	if (num <= 4) {
		slide[num++].classList.remove("hidden");
		pagination.forEach((e) => {
			e.style.backgroundColor = "#0000003a";
		});
		pagination[++pag].style.backgroundColor = "#fca311";
	}
}

nextBtn.addEventListener("click", plus);
previousBtn.addEventListener("click", prev);

if (window.matchMedia("(max-width: 576px)").matches) {
	// console.log(document.querySelector(".pagination").lastElementChild);
	document.querySelector(".pagination").lastElementChild.style.backgroundColor =
		"#0000003a";

	pagination.forEach((ele) => {
		// document.querySelectorAll(".pagination li").style.backgroundColor =
		// 	"#0000003a";
		// console.log(();
		ele.onclick = function () {
			console.log(document.querySelector(ele.dataset.pag));
			pagination.forEach((i) => {
				i.style.backgroundColor = "#0000003a";
			});
			ele.style.backgroundColor = "#fca311";
			slide.forEach((ele) => {
				ele.classList.remove("show");
			});
			document.querySelector(ele.dataset.pag).classList.add("show");
		};
	});
}
