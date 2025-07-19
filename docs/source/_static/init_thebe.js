window.addEventListener("load", function () {
  thebe.on("status", function (status) {
    if (status === "ready") {
      document.querySelectorAll(".thebe-init").forEach((el) => {
        el.querySelector("button")?.click();
      });
    }
  });
});
