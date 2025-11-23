
document.querySelectorAll(".submenu-title").forEach(function(title) {
    title.addEventListener("click", function() {

        const allSubmenus = document.querySelectorAll(".submenu");
        const allArrows = document.querySelectorAll(".arrow");

        const submenu = this.nextElementSibling;
        const arrow = this.querySelector(".arrow");

        const isOpen = submenu.style.display === "block";

        allSubmenus.forEach(s => s.style.display = "none");
        allArrows.forEach(a => a.style.transform = "rotate(0deg)");

        if (!isOpen) {
            submenu.style.display = "block";
            arrow.style.transform = "rotate(180deg)";
        }
    });
});

const themeBtn = document.getElementById("themeToggle");


if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    themeBtn.innerHTML = `<i class="fa-solid fa-sun"></i>`;
}

themeBtn.addEventListener("click", () => {

    const darkMode = document.body.classList.toggle("dark");

    themeBtn.innerHTML = darkMode
        ? `<i class="fa-solid fa-sun"></i>`
        : `<i class="fa-solid fa-moon"></i>`;

    localStorage.setItem("theme", darkMode ? "dark" : "light");
});
