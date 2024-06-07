  /*------------------------------------- */

  (() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    const forms_password = document.querySelectorAll('.needs-validation-password')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })

    Array.from(forms_password).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity() || !passwordsMatch()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)

      // Add input event listeners to confirm password to clear custom validity on input
      const confirmPasswordInput = form.querySelector('#confirm_password');
      confirmPasswordInput.addEventListener('input', () => {
        passwordsMatch();
      });
    })

    const passwordsMatch = () => {
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirm_password').value;

      if (password !== confirmPassword) {
        document.getElementById('confirm_password').setCustomValidity('Passwords do not match');
        document.getElementById('confirm_password').nextElementSibling.nextElementSibling.innerText = 'Passwords do not match.';
        return false;
      } else {
        document.getElementById('confirm_password').setCustomValidity('');
        return true;
      }
    }
  })();
 
  /*
  (() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity() || !passwordsMatch()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)

      // Add input event listeners to confirm password to clear custom validity on input
      const confirmPasswordInput = form.querySelector('#confirm_password');
      confirmPasswordInput.addEventListener('input', () => {
        passwordsMatch();
      });
    })

    const passwordsMatch = () => {
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirm_password').value;

      if (password !== confirmPassword) {
        document.getElementById('confirm_password').setCustomValidity('Passwords do not match');
        document.getElementById('confirm_password').nextElementSibling.nextElementSibling.innerText = 'Passwords do not match.';
        return false;
      } else {
        document.getElementById('confirm_password').setCustomValidity('');
        return true;
      }
    }
  })();
*/
  /*----------------------------------- */

function togglePassword(){
    var passwordBox = document.getElementById("password");
    var icon = document.getElementById("show_hide_password");

    togglePass(passwordBox, icon)
    
}

function toggleConfirmPassword(){
  var passwordBox = document.getElementById("confirm_password");
  var icon = document.getElementById("show_hide_confirm_password");

  togglePass(passwordBox, icon)
  
}

function togglePass(passwordBox, icon){
  if (passwordBox.type === "password") {
    passwordBox.type = "text";
    icon.classList.add("fa-eye-slash");
    icon.classList.remove("fa-eye");
  } else {
    passwordBox.type = "password";
    icon.classList.remove("fa-eye-slash");
    icon.classList.add("fa-eye");;
}
}

$(document).ready(function(){
  $('.toast').toast('show');
});

var rows = document.querySelectorAll(".clickable-row");
rows.forEach(function(row) {
  row.addEventListener("click", function() {
    window.location = this.dataset.href;
  });
});

//------------------------------------------------------------
var searchInputBlacklisted = document.getElementById('search_text_blacklisted');
var searchInputRobber = document.getElementById('search_text_robber');

var customerTableBody = document.getElementById('customer_table_body');
var robberTableBody = document.getElementById('robber_table_body');

searchInputBlacklisted.addEventListener('input', function() {
  var searchText = searchInputBlacklisted.value;

  // Make an AJAX request to the search endpoint
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



searchInputRobber.addEventListener('input', function() {
  var searchText = searchInputRobber.value;

  // Make an AJAX request to the search endpoint
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

//------------------------------------------------------------


/*
document.addEventListener("DOMContentLoaded", function() {

  var searchInputBlacklisted = document.getElementById('search_text_blacklisted');
  var searchInputRobber = document.getElementById('search_text_robber');

  var customerTableBody = document.getElementById('customer_table_body');
  var robberTableBody = document.getElementById('robber_table_body');

  searchInputBlacklisted.addEventListener('input', function() {
    var searchText = searchInputBlacklisted.value;

    // Make an AJAX request to the search endpoint
    var xhr_1 = new XMLHttpRequest();
    xhr_1.open('GET', '/search-blacklisted?search_text=' + encodeURIComponent(searchText), true);
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

          row.addEventListener('click', function() {
            window.location = this.getAttribute('data-href');
          });

          customerTableBody.appendChild(row);
        });
      }
    };
    xhr_1.send();
  });

  searchInputRobber.addEventListener('input', function() {
    var searchText = searchInputRobber.value;

    // Make an AJAX request to the search endpoint
    var xhr_2 = new XMLHttpRequest();
    xhr_2.open('GET', '/search-robber?search_text=' + encodeURIComponent(searchText), true);
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

          row.addEventListener('click', function() {
            window.location = this.getAttribute('data-href');
          });

          robberTableBody.appendChild(row);
        });
      }
    };
    xhr_2.send();
  });

  // Initial click handler for existing rows
  var rows = document.querySelectorAll(".clickable-row");
  rows.forEach(function(row) {
    row.addEventListener("click", function() {
      window.location = this.dataset.href;
    });
  });
});
*/
