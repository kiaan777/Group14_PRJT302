(() => {
  const form = document.getElementById("expenseForm");
  if (!form) return;
  form.addEventListener("submit", () => {
    const btn = form.querySelector(".predict-btn");
    btn.querySelector("span").textContent = "Running both models...";
    btn.disabled = true;
  });
})();
