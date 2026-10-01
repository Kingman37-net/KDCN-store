/* =========================================================
   KDCN Admin — Application Bootstrap (Phase A)
   Shell only. No backend calls. No secrets.
   ========================================================= */

(function () {
  "use strict";

  const BUILD = "phase-a";
  const PAGES = [
    "dashboard", "services", "customers", "orders", "quotes",
    "payments", "fulfillment", "audit", "settings"
  ];

  // ---------------------------------------------------------
  // PAGE NAVIGATION
  // ---------------------------------------------------------
  function setActivePage(page) {
    if (!PAGES.includes(page)) page = "dashboard";

    document.querySelectorAll(".nav-item").forEach(item => {
      item.classList.toggle("active", item.dataset.page === page);
    });

    document.querySelectorAll(".panel").forEach(panel => {
      panel.hidden = panel.dataset.panel !== page;
    });

    const titleEl = document.getElementById("page-title");
    if (titleEl) {
      const label = page.charAt(0).toUpperCase() + page.slice(1);
      titleEl.textContent = label;
    }

    if (location.hash !== "#" + page) {
      history.replaceState(null, "", "#" + page);
    }
  }

  function initNav() {
    document.querySelectorAll(".nav-item").forEach(item => {
      item.addEventListener("click", (e) => {
        e.preventDefault();
        setActivePage(item.dataset.page);
        closeSidebar();
      });
    });

    window.addEventListener("hashchange", () => {
      setActivePage(location.hash.replace("#", "") || "dashboard");
    });

    setActivePage(location.hash.replace("#", "") || "dashboard");
  }

  // ---------------------------------------------------------
  // MOBILE SIDEBAR
  // ---------------------------------------------------------
  function openSidebar() {
    document.querySelector(".sidebar")?.classList.add("open");
  }
  function closeSidebar() {
    document.querySelector(".sidebar")?.classList.remove("open");
  }
  function initSidebar() {
    const toggle = document.getElementById("menu-toggle");
    if (!toggle) return;
    toggle.addEventListener("click", () => {
      const sidebar = document.querySelector(".sidebar");
      if (!sidebar) return;
      sidebar.classList.toggle("open");
    });
  }

  // ---------------------------------------------------------
  // BUILD / ENV BADGES
  // ---------------------------------------------------------
  function initBadges() {
    const build = document.getElementById("build-badge");
    if (build) build.textContent = BUILD;

    const env = document.getElementById("env-badge");
    if (!env) return;
    const host = location.hostname;
    if (host === "localhost" || host === "127.0.0.1" || host === "") {
      env.textContent = "ENV: LOCAL";
    } else if (host.endsWith("github.io")) {
      env.textContent = "ENV: PREVIEW";
    } else {
      env.textContent = "ENV: PROD";
    }
  }

  // ---------------------------------------------------------
  // SESSION (stub — no auth yet)
  // ---------------------------------------------------------
  function initSession() {
    const state = document.getElementById("session-state");
    const logout = document.getElementById("logout-btn");
    if (state) state.textContent = "Not authenticated";
    if (logout) logout.disabled = true;

    // TODO: wire to backend auth
    //   GET /api/admin/session   → { authenticated, user, roles }
    //   POST /api/admin/logout
    // Never store a JWT signing secret in this file.
  }

  // ---------------------------------------------------------
  // INIT
  // ---------------------------------------------------------
  function init() {
    initNav();
    initSidebar();
    initBadges();
    initSession();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
