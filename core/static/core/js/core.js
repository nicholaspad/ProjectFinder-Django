$("#settings-modal-save-btn").click((e) => {
  const validateEmail = (email) => {
    return email.match(/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/);
  };

  const emailInput = $("#settings-modal-email-input");
  const firstNameInput = $("#settings-modal-first-name-input");
  const lastNameInput = $("#settings-modal-last-name-input");

  const email = String(emailInput.val()).toLowerCase();
  const firstName = String(firstNameInput.val());
  const lastName = String(lastNameInput.val());

  if (!validateEmail(email) || firstName.length < 1 || lastName.length < 1) {
    return;
  }

  e.preventDefault();
  $("#settings-modal-save-btn").addClass("disabled");

  $.post("/", { email, firstName, lastName })
    .done(() => {
      emailInput.val = email;
      firstNameInput.val = firstName;
      lastNameInput.val = lastName;
      alert("Your settings have been updated!");
      $("#settings-modal").modal("toggle");
    })
    .fail(() => alert("Failed to update your settings."))
    .always(() => $("#settings-modal-save-btn").removeClass("disabled"));
});

/****************************************************************************/
/****************************************************************************/
/****************************************************************************/

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
