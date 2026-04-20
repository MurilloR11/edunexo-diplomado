(function () {
  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".nav__toggle");
  const links = document.querySelectorAll(".nav__link");

  if (!nav || !toggle) return;

  const closeMenu = () => {
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });

  links.forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 900) closeMenu();
  });
})();

(function () {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const sections = document.querySelectorAll("main > section:not(.hero)");
  const targets = [];

  sections.forEach((section) => {
    const container = section.querySelector(":scope > .container");
    const blocks = container ? Array.from(container.children) : [section];

    blocks.forEach((block, index) => {
      block.classList.add("reveal-on-scroll");
      block.style.setProperty("--reveal-delay", `${Math.min(index * 90, 270)}ms`);
      targets.push(block);
    });
  });

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    targets.forEach((target) => target.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      });
    },
    { threshold: 0.16, rootMargin: "0px 0px -12% 0px" }
  );

  targets.forEach((target) => observer.observe(target));
})();

(function () {
  const values = document.querySelectorAll(".hero__stat-value[data-target]");
  const stats = document.querySelector(".hero__stats");
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!values.length) return;

  const formatValue = (value, format) => {
    if (format === "k") {
      return `${Math.max(0, Math.round(value / 1000))}K`;
    }
    return `${Math.max(0, Math.round(value))}`;
  };

  const setFinalValues = () => {
    values.forEach((el) => {
      const target = Number(el.getAttribute("data-target") || 0);
      const format = el.getAttribute("data-format");
      el.textContent = formatValue(target, format);
    });
  };

  let hasStarted = false;

  const animate = () => {
    if (hasStarted) return;
    hasStarted = true;

    const duration = 1800;
    const easeOut = (t) => 1 - Math.pow(1 - t, 3);
    const start = performance.now();

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = easeOut(progress);

      values.forEach((el) => {
        const target = Number(el.getAttribute("data-target") || 0);
        const format = el.getAttribute("data-format");
        el.textContent = formatValue(target * eased, format);
      });

      if (progress < 1) {
        requestAnimationFrame(tick);
      }
    };

    requestAnimationFrame(tick);
  };

  if (prefersReducedMotion) {
    setFinalValues();
    return;
  }

  if (!stats || !("IntersectionObserver" in window)) {
    animate();
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animate();
        obs.unobserve(entry.target);
      });
    },
    { threshold: 0.45 }
  );

  observer.observe(stats);
})();
