 
var customerTableBody = document.getElementById('customer_table_body');
var searchInputBlacklisted = document.getElementById('search_text_blacklisted');
searchInputBlacklisted.addEventListener('input', function() {
  var searchText = searchInputBlacklisted.value;

  var xhr_1 = new XMLHttpRequest();
  xhr_1.open('GET', '/search_blacklisted?search_text=' + encodeURIComponent(searchText), true);
  xhr_1.onload = function() {
    if (xhr_1.status === 200) {
      var customers = JSON.parse(xhr_1.responseText);
      customerTableBody.innerHTML = '';

      customers.forEach(function(customer, index) {
        var row = document.createElement('tr');
        row.classList.add('clickable-row');
        row.setAttribute('data-href', '/blacklisted_customer/' + customer[0]);

        var cellIndex = document.createElement('td');
        cellIndex.textContent = index + 1;
        row.appendChild(cellIndex);

        var cellCifNo = document.createElement('td');
        cellCifNo.textContent = customer[0];
        row.appendChild(cellCifNo);

        var cellDescription = document.createElement('td');
        cellDescription.textContent = customer[1];
        row.appendChild(cellDescription);

        var cellAddedBy = document.createElement('td');
        cellAddedBy.textContent = customer[2];
        row.appendChild(cellAddedBy);

        var cellTime = document.createElement('td');
        cellTime.textContent = customer[3];
        row.appendChild(cellTime);

        row.addEventListener('click', function() {
          window.location = this.getAttribute('data-href');
        });

        customerTableBody.appendChild(row);
      });
    }
  }
  xhr_1.send();
})