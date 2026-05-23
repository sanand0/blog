(() => {
  const script = document.currentScript
    || document.querySelector("script[data-site-script=\"true\"]");
  const data = script ? script.dataset : {};
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

  // Render nav items into a footer <ul>. countKey items get proportional bar widths.
  // Uses 3rd largest count as 100% to avoid outliers dominating the scale.
  const fillNav = (selector, items, labelKey, countKey) => {
    const ul = document.querySelector(selector);
    if (!ul) return;
    const counts = countKey ? items.map((i) => i[countKey]).sort((a, b) => b - a) : [];
    const threshold = counts[2] ?? counts[0] ?? 1;
    ul.innerHTML = items.map((item) => {
      const bar = countKey ? ` style="--bar-width:${Math.min(100, item[countKey] / threshold * 100).toFixed(1)}%"` : "";
      const count = countKey ? `<span class="nav-count">${item[countKey]}</span>` : "";
      return `<li><a href="${esc(item.url)}"${bar}><span class="nav-name">${esc(item[labelKey])}</span>${count}</a></li>`;
    }).join("");
  };

  if (data.navJson) {
    fetch(data.navJson)
      .then((r) => r.json())
      .then((nav) => {
        fillNav("#footer-categories ul", nav.categories, "name", "count");
        fillNav("#footer-archives ul", nav.archives, "label", "count");
        fillNav("#footer-pages ul", nav.pages, "name", null);
      });
  }
  const enableScrollTop = data.enableScrollTop === "true";
  const enableThemeToggle = data.enableThemeToggle === "true";
  const enableCodeCopy = data.enableCodeCopy === "true";
  const codeCopyText = data.codeCopy || "copy";
  const codeCopiedText = data.codeCopied || "copied!";

  const menu = document.getElementById("menu");
  if (menu) {
    const scrollPosition = localStorage.getItem("menu-scroll-position");
    if (scrollPosition) {
      menu.scrollLeft = parseInt(scrollPosition, 10);
    }
    menu.addEventListener("scroll", () => {
      localStorage.setItem("menu-scroll-position", menu.scrollLeft);
    });
  }

  document.querySelectorAll("a[href^=\"#\"]").forEach((anchor) => {
    anchor.addEventListener("click", (event) => {
      const href = anchor.getAttribute("href") || "";
      if (!href.startsWith("#") || href.length < 2) {
        return;
      }
      const id = href.slice(1);
      const target = document.getElementById(decodeURIComponent(id));
      if (!target) {
        return;
      }
      event.preventDefault();
      if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        target.scrollIntoView({ behavior: "smooth" });
      } else {
        target.scrollIntoView();
      }
      if (id === "top") {
        history.replaceState(null, null, " ");
      } else {
        history.pushState(null, null, `#${id}`);
      }
    });
  });

  if (enableScrollTop) {
    const topLink = document.getElementById("top-link");
    if (topLink) {
      window.addEventListener("scroll", () => {
        if (
          document.body.scrollTop > 800
          || document.documentElement.scrollTop > 800
        ) {
          topLink.style.visibility = "visible";
          topLink.style.opacity = "1";
        } else {
          topLink.style.visibility = "hidden";
          topLink.style.opacity = "0";
        }
      });
    }
  }

  if (enableThemeToggle) {
    const toggle = document.getElementById("theme-toggle");
    if (toggle) {
      toggle.addEventListener("click", () => {
        const html = document.documentElement;
        if (html.dataset.theme === "dark") {
          html.dataset.theme = "light";
          localStorage.setItem("pref-theme", "light");
        } else {
          html.dataset.theme = "dark";
          localStorage.setItem("pref-theme", "dark");
        }
      });
    }
  }

  if (enableCodeCopy) {
    document.querySelectorAll("pre > code").forEach((codeblock) => {
      const container = codeblock.parentNode.parentNode;
      const copybutton = document.createElement("button");
      copybutton.classList.add("copy-code");
      copybutton.textContent = codeCopyText;

      function copyingDone() {
        copybutton.textContent = codeCopiedText;
        setTimeout(() => {
          copybutton.textContent = codeCopyText;
        }, 2000);
      }

      copybutton.addEventListener("click", () => {
        if ("clipboard" in navigator) {
          navigator.clipboard.writeText(codeblock.textContent);
          copyingDone();
          return;
        }

        const range = document.createRange();
        range.selectNodeContents(codeblock);
        const selection = window.getSelection();
        if (!selection) {
          return;
        }
        selection.removeAllRanges();
        selection.addRange(range);
        try {
          document.execCommand("copy");
          copyingDone();
        } catch (error) {
          // Ignore clipboard errors.
        }
        selection.removeRange(range);
      });

      if (container.classList.contains("highlight")) {
        container.appendChild(copybutton);
      } else if (container.parentNode.firstChild === container) {
        // td containing LineNos
      } else if (
        codeblock.parentNode.parentNode.parentNode.parentNode.parentNode
          .nodeName === "TABLE"
      ) {
        codeblock.parentNode.parentNode.parentNode.parentNode.parentNode.appendChild(
          copybutton,
        );
      } else {
        codeblock.parentNode.appendChild(copybutton);
      }
    });
  }

  // AI disclosure badges and attribution footers.
  // Works with any data-ai-* attributes — future-proof by reading all of them.
  document.querySelectorAll("section[ai-disclosure]").forEach((section) => {
    // Collect all data-ai-* attributes generically
    const aiAttrs = {};
    for (const attr of section.attributes) {
      if (attr.name.startsWith("data-ai-")) {
        aiAttrs[attr.name.slice("data-ai-".length)] = attr.value;
      }
    }

    const disclosure = section.getAttribute("ai-disclosure") || "ai-generated";
    const model = aiAttrs["model"] || "";
    const provider = aiAttrs["provider"] || "";

    // Badge at top-right
    const badge = document.createElement("span");
    badge.className = "ai-disclosure-badge";
    badge.textContent = "AI";

    const tooltipParts = [model, provider].filter(Boolean);
    if (tooltipParts.length) {
      const tooltip = document.createElement("span");
      tooltip.className = "ai-disclosure-tooltip";
      tooltip.textContent = tooltipParts.join(" \u00b7 ");
      badge.appendChild(tooltip);
    }

    section.insertBefore(badge, section.firstChild);

    // Bottom attribution
    const footer = document.createElement("p");
    footer.className = "ai-disclosure-footer";
    const footerParts = [disclosure.toUpperCase().replace(/-/g, "\u2011"), model, provider].filter(Boolean);
    footer.textContent = footerParts.join(" \u00b7 ");
    section.appendChild(footer);
  });
})();
