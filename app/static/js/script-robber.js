 
var searchInputRobber = document.getElementById('search_text_robber');
var robberTableBody = document.getElementById('robber_table_body');

searchInputRobber.addEventListener('input', function() {
  var searchText = searchInputRobber.value;

  var xhr_2 = new XMLHttpRequest();
  xhr_2.open('GET', '/search_robber?search_text=' + encodeURIComponent(searchText), true);
  xhr_2.onload = function() {
    if (xhr_2.status === 200) {
      var robber = JSON.parse(xhr_2.responseText);
      robberTableBody.innerHTML = '';

      robber.forEach(function(robber, index) {
        var row = document.createElement('tr');
        row.classList.add('clickable-row');
        row.setAttribute('data-href', '/robber/' + robber[0]);

        var cellIndex = document.createElement('td');
        cellIndex.textContent = index + 1;
        row.appendChild(cellIndex);

        var cellRobberId = document.createElement('td');
        cellRobberId.textContent = robber[0];
        row.appendChild(cellRobberId);
        
        var cellName = document.createElement('td');
        cellName.textContent = robber[1];
        row.appendChild(cellName);

        var cellDescription = document.createElement('td');
        cellDescription.textContent = robber[2];
        row.appendChild(cellDescription);

        var cellAddedBy = document.createElement('td');
        cellAddedBy.textContent = robber[3];
        row.appendChild(cellAddedBy);

        var cellTime = document.createElement('td');
        cellTime.textContent = robber[4];
        row.appendChild(cellTime);

        row.addEventListener('click', function() {
          window.location = this.getAttribute('data-href');
        });

        robberTableBody.appendChild(row);
      });
    }
  };
  xhr_2.send();
})