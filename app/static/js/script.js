
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
    icon.classList.add("fa-eye");
    icon.classList.remove("fa-eye-slash");
  } else {
    passwordBox.type = "password";
    icon.classList.remove("fa-eye");
    icon.classList.add("fa-eye-slash");;
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