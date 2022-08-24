$("#settings-modal-save-btn").click(() => {
  const validateEmail = (email) => {
    return email.match(/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/);
  };

  const emailInput = $("#settings-modal-email-input");
  const nameInput = $("#settings-modal-name-input");

  const email = String(emailInput.val()).toLowerCase();
  const name = String(nameInput.val());

  if (!validateEmail(email) || name.length < 1) {
    return;
  }

  $.post("/", { email, name }, (res) => {
    console.log(res);
  });
});

// Source: https://getbootstrap.com/docs/5.2/forms/validation/#custom-styles
(() => {
  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();
