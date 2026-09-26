/* =========================================================
   KDCN STORE — MAIN APP (4-Tier Version)
   ========================================================= */

(function () {
  "use strict";

  const USD_RATE = 130;

  // =========================================================
  // THEME TOGGLE
  // =========================================================
  function initTheme() {
    const body = document.body;
    const toggle = document.getElementById("theme-toggle");
    if (!toggle) return;

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
      hamburger.setAttribute("aria-expanded", navMenu.classList.contains("active") ? "true" : "false");
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
  function parseKES(str) {
    const nums = str.match(/\d[\d,]*/g) || [];
    return nums.map(n => parseInt(n.replace(/,/g, "")))[0] || 0;
  }

  function kesToUsd(kes) {
    return Math.round(kes / USD_RATE);
  }

  // =========================================================
  // TIER CARDS
  // =========================================================
  function renderTiers() {
    const grid = document.getElementById("tier-grid");
    if (!grid) return;

    grid.innerHTML = KDCN_TIERS.map(tier => `
      <a href="#${tier.id}" class="tier-card reveal" style="--tier-color: ${tier.color}">
        <div class="tier-icon">${tier.icon}</div>
        <h3>${tier.name}</h3>
        <p>${tier.description}</p>
        <span class="tier-price">${tier.priceRange}</span>
        <span class="tier-ideal">Ideal for: ${tier.idealFor}</span>
      </a>
    `).join("");
  }

  // =========================================================
  // SERVICE CARDS
  // =========================================================
  function renderServiceCard(service) {
    const usd = kesToUsd(service.feeMin);
    const tierInfo = KDCN_TIERS.find(t => t.id === service.tier);

    return `
      <article class="service-card reveal" data-tier="${service.tier}">
        <div class="service-image">
          <img src="${service.image}" alt="${service.name}" loading="lazy" decoding="async">
          ${service.badge ? `<span class="service-badge">${service.badge}</span>` : ""}
        </div>
        <div class="service-body">
          <span class="service-tier-tag" style="background: ${tierInfo.color}20; color: ${tierInfo.color}">
            ${tierInfo.icon} ${tierInfo.name.split(" ")[0]}
          </span>
          <h3>${service.name}</h3>
          <p>${service.tagline}</p>
          <div class="service-price">
            <span class="kes">${service.fee}</span>
            <span class="usd">~$${usd} USD</span>
          </div>
          <div class="service-actions">
            <a href="services/${service.id}.html" class="btn btn-details">View Details</a>
            <a href="https://wa.me/254111843716?text=${encodeURIComponent(service.whatsapp)}"
               class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Inquire</a>
          </div>
        </div>
      </article>
    `;
  }

  function renderServices(tier) {
    const grid = document.getElementById("services-grid");
    if (!grid) return;

    let services = KDCN_SERVICES;
    if (tier && tier !== "all") {
      services = KDCN_SERVICES.filter(s => s.tier === tier);
    }

    grid.innerHTML = services.map(renderServiceCard).join("");
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
  // INIT
  // =========================================================
  function init() {
    initTheme();
    initNav();
    renderTiers();
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
