
//DARK MODE
let darkMode = localStorage.getItem("darkMode");
const webmode_container = document.querySelector(".webmode_container");
const webmode_dark = document.querySelector(".webmode_dark");
const webmode_light = document.querySelector(".webmode_light");
const favicon_img = document.querySelector(".favicon_img");
const favicon_img_footer = document.querySelector(".favicon_img_footer");

const enableDarkMode = () => {
    document.body.classList.add("dark");
    localStorage.setItem("darkMode", "enabled");
    favicon_img.classList.add("dark");
    favicon_img_footer.classList.add("dark");
    webmode_dark.classList.remove("hide_dark");
    webmode_light.classList.add("hide_dark");
};

const disableDarkMode = () => {
    document.body.classList.remove("dark");
    localStorage.setItem("darkMode", "disabled");
    favicon_img.classList.remove("dark");
    favicon_img_footer.classList.remove("dark");
    webmode_dark.classList.add("hide_dark");
    webmode_light.classList.remove("hide_dark");
};


if(darkMode === "enabled") {
    enableDarkMode();
} else {
    disableDarkMode();
};

webmode_container.addEventListener("click", function() {
    darkMode = localStorage.getItem("darkMode");
    if(darkMode !== "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});