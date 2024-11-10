
  (() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const login_form = document.querySelectorAll('.needs-validation-login')
    const forms = document.querySelectorAll('.needs-validation')
    const forms_password = document.querySelectorAll('.needs-validation-password')


    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }else{
          event.preventDefault()
          event.stopPropagation()
          Swal.fire({
            title: "Are you sure?",
            icon: "warning",
            iconColor : "#545454",
            showCancelButton: true,
            confirmButtonText: "Yes"
          }).then((result) => {
            if (result.isConfirmed) {
              event.target.submit();
            }
          });
        }

        form.classList.add('was-validated')
      }, false)
      
    })

    Array.from(forms_password).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity() || !passwordsMatch()) {
          event.preventDefault()
          event.stopPropagation()
        }else{
          event.preventDefault()
          event.stopPropagation()
          Swal.fire({
            title: "Are you sure?",
            icon: "warning",
            iconColor : "#545454",
            showCancelButton: true,
            confirmButtonText: "Yes"
          }).then((result) => {
            if (result.isConfirmed) {
              event.target.submit();
            }
          });
        }

        form.classList.add('was-validated')
      }, false)

      // Add input event listeners to confirm password to clear custom validity on input
      const confirmPasswordInput = form.querySelector('#confirm_password');
      confirmPasswordInput.addEventListener('input', () => {
        passwordsMatch();
      });
    })

    Array.from(login_form).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
      
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

function toggleCurrentPassword(passwordBox, icon){
  var passwordBox = document.getElementById("current_password");
  var icon = document.getElementById("show_hide_current_password");

  togglePass(passwordBox, icon)
  
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

/*
function toggleNavPanel() {
  const floatingNavLinks = document.getElementById("floatingNavLinks");
  const btnToggleNavPanel = document.getElementById("btnToggleNavPanel");

  if (floatingNavLinks.classList.contains("hidden")) {
    floatingNavLinks.classList.remove("hidden");
    btnToggleNavPanel.classList.replace("fa-chevron-right", "fa-chevron-left");
  } else {
    floatingNavLinks.classList.add("hidden");
    btnToggleNavPanel.classList.replace("fa-chevron-left", "fa-chevron-right");
  }
}
*/
// Function to apply saved state on page load
function applyNavPanelState() {
  const floatingNavLinks = document.getElementById("floatingNavLinks");
  const btnToggleNavPanel = document.getElementById("btnToggleNavPanel");
  const savedState = localStorage.getItem("navPanelState");

  // Apply the saved state immediately on page load
  if (savedState === "closed") {
    floatingNavLinks.classList.add("hidden");
    btnToggleNavPanel.classList.replace("fa-chevron-left", "fa-chevron-right");
  } else {
    floatingNavLinks.classList.add("visible");
    btnToggleNavPanel.classList.replace("fa-chevron-right", "fa-chevron-left");
  }
}

// Toggle function with localStorage
function toggleNavPanel() {
  const floatingNavLinks = document.getElementById("floatingNavLinks");
  const btnToggleNavPanel = document.getElementById("btnToggleNavPanel");

  if (floatingNavLinks.classList.contains("hidden")) {
    floatingNavLinks.classList.remove("hidden");
    floatingNavLinks.classList.add("visible");
    btnToggleNavPanel.classList.replace("fa-chevron-right", "fa-chevron-left");
    localStorage.setItem("navPanelState", "open");
  } else {
    floatingNavLinks.classList.remove("visible");
    floatingNavLinks.classList.add("hidden");
    btnToggleNavPanel.classList.replace("fa-chevron-left", "fa-chevron-right");
    localStorage.setItem("navPanelState", "closed");
  }
}

// Call the function right away to apply state as early as possible
applyNavPanelState();


function confirmAction(event){

  var url = event.target.getAttribute('data-url');

  Swal.fire({
    title: "Are you sure?",
    icon: "warning",
    iconColor : "#545454",
    showCancelButton: true,
    confirmButtonText: "Yes"
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = url;
    }
  });
}