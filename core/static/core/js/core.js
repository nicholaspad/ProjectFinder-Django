$("#settings-modal-save-btn").click(() => {
  const emailInput = $("#settings-modal-email-input");
  const nameInput = $("#settings-modal-name-input");

  const email = emailInput.val();
  const name = nameInput.val();

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
