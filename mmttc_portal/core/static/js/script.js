console.log("script.js loaded");

const photoInput = document.getElementById("photograph");
const photoPreview = document.getElementById("photo-preview");
const photoUploaded = document.getElementById("photo-uploaded");

if (photoInput && photoPreview && photoUploaded) {

    photoInput.addEventListener("change", function () {

        const file = this.files[0];

        photoPreview.style.display = "none";
        photoUploaded.checked = false;

        if (!file) {
            return;
        }

        const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
        const maxSize = 50 * 1024;

        if (!allowedTypes.includes(file.type)) {
            alert("Only JPG, PNG, or GIF files are allowed.");
            photoInput.value = "";
            return;
        }

        if (file.size > maxSize) {
            alert("Photograph size must be 50KB or less.");
            photoInput.value = "";
            return;
        }

        const reader = new FileReader();

        reader.onload = function (event) {

            const image = new Image();

            image.onload = function () {

                if (image.width !== image.height) {
                    alert("Photograph must have 1:1 aspect ratio.");
                    photoInput.value = "";
                    photoPreview.style.display = "none";
                    photoUploaded.checked = false;
                    return;
                }

                photoPreview.src = event.target.result;
                photoPreview.style.display = "block";
                photoUploaded.checked = true;
            };

            image.src = event.target.result;
        };

        reader.readAsDataURL(file);
    });
}

const applicationForm = document.querySelector(".official-application-form");

let formChanged = false;

if (applicationForm) {

    applicationForm.addEventListener("input", function () {
        formChanged = true;
    });

    applicationForm.addEventListener("submit", function () {
        formChanged = false;
    });

    window.addEventListener("beforeunload", function (event) {

        if (formChanged) {
            event.preventDefault();
            event.returnValue = "";
        }

    });

}

const instructionCheck = document.getElementById("instruction_check");
const continueButton = document.getElementById("continue_button");

if (instructionCheck && continueButton) {

    instructionCheck.addEventListener("change", function () {

        continueButton.disabled = !this.checked;

    });

}