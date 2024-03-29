// Makes "filter-toggle"s change the class of "filters" when clicked
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

// Makes "checkbox"es toggleable (change their own class only)
const checkboxes = document.getElementsByClassName("checkbox");
Array.prototype.forEach.call(checkboxes, e => {
	e.onclick = () => {
		e.classList.toggle("active");
	};
});

// Add "required" class to "form-input"s
const form_inputs = document.getElementsByClassName("form-input");
Array.prototype.forEach.call(form_inputs, e => {
	if (e.querySelector('[required]'))
		e.classList.add('required');
});

const matching_results = document.getElementById("matching-results");
const matching_loading = document.createElement("div");
matching_loading.classList.add("loading-icon", "fa", "fa-spinner", "fa-spin");
matching_results.after(matching_loading);
matching_results.classList.add("hide");
setTimeout(() => {
	matching_loading.remove();
	matching_results.classList.remove("hide");
}, 2500);
