const filters_toggles = document.getElementsByClassName("filters-toggle");
const filters = document.getElementsByClassName("filters");

Array.prototype.forEach.call(filters_toggles, e => {
	e.onclick = () => {
		e.classList.toggle("active");
		Array.prototype.forEach.call(filters, f => {
			f.classList.toggle("active");
		});
	};
});

const checkboxes = document.getElementsByClassName("checkbox");

Array.prototype.forEach.call(checkboxes, e => {
	e.onclick = () => {
		e.classList.toggle("active");
	};
});
