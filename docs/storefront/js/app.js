/* =========================================================
   KDCN STORE — MAIN APP
   Theme toggle + Service rendering + Filters
   ========================================================= */

(function () {
  "use strict";

  const USD_RATE = 130; // 1 USD ≈ 130 KES

  // =========================================================
  // THEME TOGGLE
  // =========================================================
  function initTheme() {
    const body = document.body;
    const toggle = document.getElementById("theme-toggle");

    if (localStorage.getItem("kdcn-shop-theme") === "light") {
      body.classList.add("light");
    }

    function updateIcon() {
      toggle.textContent = body.classList.contains("light") ? "☀️" : "🌙";
    }
    updateIcon();

    toggle.addEventListener("click", () => {
      body.classList.toggle("light");
      const theme = body.classList.contains("light") ? "light" : "dark";
      localStorage.setItem("kdcn-shop-theme", theme);
      updateIcon();
    });
  }

  // =========================================================
  // MOBILE NAV
  // =========================================================
  function initNav() {
    const hamburger = document.getElementById("hamburger");
    const navMenu = document.getElementById("nav-menu");
    if (!hamburger || !navMenu) return;

    hamburger.addEventListener("click", () => {
      navMenu.classList.toggle("active");
      const isOpen = navMenu.classList.contains("active");
      hamburger.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    navMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active");
        hamburger.setAttribute("aria-expanded", "false");
      });
    });
  }

  // =========================================================
  // HELPERS
  // =========================================================
  function kesToUsd(kes) {
    return Math.round(kes / USD_RATE);
  }

  function parseRange(priceStr) {
    // Extract numbers from "KES 250 – 300" → [250, 300]
    const nums = priceStr.match(/\d[\d,]*/g) || [];
    const cleaned = nums.map(n => parseInt(n.replace(/,/g, "")));
    return cleaned;
  }

  function formatUsdRange(priceStr) {
    const [min, max] = parseRange(priceStr);
    if (!min) return "";
    if (!max || min === max) return `~$${kesToUsd(min)}`;
    return `~$${kesToUsd(min)} – $${kesToUsd(max)}`;
  }

  // =========================================================
  // RENDER SERVICE CARD
  // =========================================================
  function renderServiceCard(service) {
    const usdRange = formatUsdRange(service.price);

    return `
      <article class="service-card reveal" data-tier="${service.tier}">
        <div class="service-image">
          <img src="${service.image}" alt="${service.name}" loading="lazy" decoding="async">
        </div>
        <div class="service-body">
          <span class="service-tier-tag ${service.tier}">${service.tier}</span>
          <h3>${service.name}</h3>
          <p>${service.tagline}</p>
          <div class="service-price">
            <span class="kes">${service.price}</span>
            <span class="usd">${usdRange}</span>
          </div>
          <div class="service-actions">
            <a href="https://wa.me/254111843716?text=${encodeURIComponent(service.whatsapp)}"
               class="btn btn-whatsapp"
               target="_blank" rel="noopener">
              💬 Inquire
            </a>
          </div>
        </div>
      </article>
    `;
  }

  // =========================================================
  // RENDER ALL SERVICES
  // =========================================================
  function renderServices(tier) {
    const grid = document.getElementById("services-grid");
    if (!grid) return;

    let services = KDCN_SERVICES;
    if (tier && tier !== "all") {
      services = KDCN_SERVICES.filter(s => s.tier === tier);
    }

    grid.innerHTML = services.map(renderServiceCard).join("");

    // Re-run reveal observer
    setTimeout(initReveal, 50);
  }

  // =========================================================
  // FILTER CHIPS
  // =========================================================
  function initFilters() {
    const chips = document.querySelectorAll(".chip");
    chips.forEach(chip => {
      chip.addEventListener("click", () => {
        chips.forEach(c => c.classList.remove("active"));
        chip.classList.add("active");
        renderServices(chip.dataset.tier);
      });
    });
  }

  // =========================================================
  // REVEAL ON SCROLL
  // =========================================================
  function initReveal() {
    const elements = document.querySelectorAll(".reveal:not(.active)");
    if (!("IntersectionObserver" in window)) {
      elements.forEach(el => el.classList.add("active"));
      return;
    }
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    elements.forEach(el => observer.observe(el));
  }

  // =========================================================
  // UPDATE STAT COUNT
  // =========================================================
  function updateStats() {
    const el = document.getElementById("stat-count");
    if (el) el.textContent = KDCN_SERVICES.length;
  }

  // =========================================================
  // INIT
  // =========================================================
  function init() {
    initTheme();
    initNav();
    updateStats();
    renderServices("all");
    initFilters();
    initReveal();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
