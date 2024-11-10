 
var userTableBody = document.getElementById('user_table_body');
var searchInputUser = document.getElementById('search_text_user');
searchInputUser.addEventListener('input', function() {
  var searchText = searchInputUser.value;

  var xhr_3 = new XMLHttpRequest();
  xhr_3.open('GET', '/search_user?search_text=' + encodeURIComponent(searchText), true);
  xhr_3.onload = function() {
    if (xhr_3.status === 200) {
      var users = JSON.parse(xhr_3.responseText);
      userTableBody.innerHTML = '';

      users.forEach(function(user, index) {
        var row = document.createElement('tr');

        var cellIndex = document.createElement('td');
        cellIndex.textContent = index + 1;
        row.appendChild(cellIndex);

        var cellUserId = document.createElement('td');
        cellUserId.textContent = user[0];
        row.appendChild(cellUserId);

        var cellType = document.createElement('td');
        if (user[1]==1){
          cellType.textContent = "Admin";
        }else if(user[1]==0){
          cellType.textContent = "Officer";
        }else{
          cellType.textContent = "Error"
        }
        row.appendChild(cellType);

        var cellAddedBy = document.createElement('td');
        cellAddedBy.textContent = user[2];
        row.appendChild(cellAddedBy);

        var cellTime = document.createElement('td');
        cellTime.textContent = user[3];
        row.appendChild(cellTime);

        userTableBody.appendChild(row);
      });
    }
  }
  xhr_3.send();
})