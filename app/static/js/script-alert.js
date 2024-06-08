var searchInputAlert = document.getElementById('search_text_alert');
var alertTableBody = document.getElementById('alert_table_body');

searchInputAlert.addEventListener('input', function() {
  var searchText = searchInputAlert.value;

  var xhr_2 = new XMLHttpRequest();
  xhr_2.open('GET', '/search_alert?search_text=' + encodeURIComponent(searchText), true);
  xhr_2.onload = function() {
    if (xhr_2.status === 200) {
      var alert = JSON.parse(xhr_2.responseText);
      alertTableBody.innerHTML = '';

      alert.forEach(function(alert, index) {
        var row = document.createElement('tr');
        row.classList.add('clickable-row');
        row.setAttribute('data-href', '/alert/' + alert[0]);

        var cellIndex = document.createElement('td');
        cellIndex.textContent = index + 1;
        row.appendChild(cellIndex);

        var cellAlertId = document.createElement('td');
        cellAlertId.textContent = alert[0];
        row.appendChild(cellAlertId);
        
        var cellType= document.createElement('td');
        cellType.textContent = alert[1];
        row.appendChild(cellType);

        var cellDescription = document.createElement('td');
        cellDescription.textContent = alert[2];
        row.appendChild(cellDescription);

        var cellTime = document.createElement('td');
        cellTime.textContent = alert[3];
        row.appendChild(cellTime);

        var cellBranchId = document.createElement('td');
        cellBranchId.textContent = alert[4];
        row.appendChild(cellBranchId);
        
        var cellGeneratedBy = document.createElement('td');
        cellGeneratedBy.textContent = alert[5];
        row.appendChild(cellGeneratedBy);


        row.addEventListener('click', function() {
          window.location = this.getAttribute('data-href');
        });

        alertTableBody.appendChild(row);
      });
    }
  };
  xhr_2.send();
})