// ===============================================
// ARMAN PORTFOLIO - main.js
// ===============================================

document.addEventListener("DOMContentLoaded", function () {

    const navbar = document.querySelector(".navbar");
    const navToggle = document.querySelector(".nav-toggle");
    const navMenu = document.getElementById("nav-menu");
    const navLinks = document.querySelectorAll(".nav-links a");
    const sections = document.querySelectorAll("main section[id]");

    // ---------- 1. Mobile menu ----------
    // Your CSS uses ".open" on the menu and ".active" on the button.

    function openMenu() {
        navMenu.classList.add("open");
        navToggle.classList.add("active");
        navToggle.setAttribute("aria-expanded", "true");
        navToggle.setAttribute("aria-label", "Close menu");
    }

    function closeMenu() {
        navMenu.classList.remove("open");
        navToggle.classList.remove("active");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Open menu");
    }

    if (navToggle && navMenu) {

        navToggle.addEventListener("click", function () {
            if (navMenu.classList.contains("open")) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        // Close the menu when a link is tapped
        navLinks.forEach(function (link) {
            link.addEventListener("click", closeMenu);
        });

        // Close with the Escape key
        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") {
                closeMenu();
            }
        });

        // Close when tapping outside the menu
        document.addEventListener("click", function (event) {
            const clickedInside =
                navMenu.contains(event.target) ||
                navToggle.contains(event.target);

            if (!clickedInside) {
                closeMenu();
            }
        });

        // Close if the screen becomes wide (matches your 768px CSS)
        window.addEventListener("resize", function () {
            if (window.innerWidth > 768) {
                closeMenu();
            }
        });
    }

    // ---------- 2. Scroll effects ----------

    function onScroll() {

        // Shrink the navbar after scrolling a little (.navbar.scrolled)
        if (navbar) {
            navbar.classList.toggle("scrolled", window.scrollY > 20);
        }

        // Highlight the link of the section being viewed
        let currentId = "";

        sections.forEach(function (section) {
            if (window.scrollY >= section.offsetTop - 140) {
                currentId = section.getAttribute("id");
            }
        });

        // At the very bottom of the page, highlight the last section
        const atBottom =
            window.innerHeight + window.scrollY >=
            document.body.offsetHeight - 4;

        if (atBottom && sections.length > 0) {
            currentId = sections[sections.length - 1].getAttribute("id");
        }

        navLinks.forEach(function (link) {
            link.classList.toggle(
                "active",
                link.getAttribute("href") === "#" + currentId
            );
        });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
});