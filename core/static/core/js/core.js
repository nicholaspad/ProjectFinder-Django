const initSettingModalSaveButton = () => {
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

    $.post("/update-settings", { email, firstName, lastName })
      .done(() => {
        emailInput.val = email;
        firstNameInput.val = firstName;
        lastNameInput.val = lastName;
        alert("Your settings have been updated!");
        $("#settings-modal").modal("toggle");
        location.reload();
      })
      .fail(() => alert("Failed to update your settings."))
      .always(() => $("#settings-modal-save-btn").removeClass("disabled"));
  });
};

const initEntryModalSaveButton = () => {
  $("#entry-modal-save-btn").click((e) => {
    const skillsInput = $("#entry-modal-skills-input");
    const interestsInput = $("#entry-modal-interests-input");
    const projectNameInput = $("#entry-modal-project-name-input");
    const projectDescriptionInput = $("#entry-modal-project-description-input");

    const skills = String(skillsInput.val());
    const interests = String(interestsInput.val());
    const projectName = String(projectNameInput.val());
    const projectDescription = String(projectDescriptionInput.val());

    if (
      skills.length < 1 ||
      interests.length < 1 ||
      projectName.length < 1 ||
      projectDescription.length < 1
    ) {
      return;
    }

    e.preventDefault();
    $("#entry-modal-save-btn").addClass("disabled");

    $.post("/", { email, firstName, lastName, type: "entry" })
      .done(() => {
        skillsInput.val = skills;
        interestsInput.val = interests;
        projectNameInput.val = projectName;
        projectDescriptionInput.val = projectDescription;
        alert("Your entry has been submitted/updated!");
        $("#entry-modal").modal("toggle");
        location.reload();
      })
      .fail(() => alert("Failed to submit/update your entry."))
      .always(() => $("#entry-modal-save-btn").removeClass("disabled"));
  });
};

const initDataTable = () => {
  $("#entry-table").DataTable({ paging: false });
  $("#entry-table_filter > label > input").addClass("form-control mt-1 mb-2");
  $("#entry-table_filter").css("text-align", "left");
};

$(document).ready(() => {
  initSettingModalSaveButton();
  initDataTable();
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
