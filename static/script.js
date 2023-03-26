// Get the form element and add an event listener for when the form is submitted
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();  // Prevent the default form submission behavior
    const data = new FormData(form);  // Create a new FormData object from the form data
    fetch('/results', {  // Send a POST request to the /results route with the form data
        method: 'POST',
        body: data
    })
    .then(response => response.text())
    .then(html => {
        const resultsContainer = document.querySelector('#results-container');  // Get the results container element
        resultsContainer.innerHTML = html;  // Set the results container's inner HTML to the response from the server
    });
});
