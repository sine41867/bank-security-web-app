function fetchData() {
    $.ajax({
        url: '/get-data',
        type: 'GET',
        success: function(response) {
            $('#data-div').text(response.message);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

// Call fetchData every 5 seconds (5000 milliseconds)
setInterval(fetchData, 1000);

// Initial call to populate the div when the page loads
fetchData();