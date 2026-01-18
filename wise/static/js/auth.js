import "../sass/auth.scss";

class Authentication {
  init() {
    this.createAccount();
    this.login();
  }

  /* =========================
     CREATE ACCOUNT FLOW
  ========================== */
  createAccount() {
    const self = this;

    // Step navigation
    $(document).on("click", "[data-step]", function () {
      const step = $(this).data("step");
      self.goToStep(step);
    });

    // Finish onboarding
    $(document).on("click", "#finishProcess", function () {
      self.processFinish();
    });
  }

  goToStep(step) {
    $(".pane-step").removeClass("active");
    $("#step" + step).addClass("active");

    for (let i = 1; i <= 4; i++) {
      $("#p" + i).toggleClass("active", i <= step);
    }
  }

  processFinish() {
    this.goToStep(4);

    setTimeout(() => {
      $("#loading-state").hide();
      $("#success-state").show();
    }, 2500);
  }

  /* =========================
     LOGIN FLOW
  ========================== */
  login() {
    $(document).on("submit", "#loginForm", function (e) {
      e.preventDefault();

      // login logic here
      console.log("Login submitted");
    });
  }
}

$(function () {
  new Authentication().init();
});
