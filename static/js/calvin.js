(() => {
  const DATA_URL = "https://files.s-anand.net/images/calvin.tsv";
  const IMAGE_BASE = "https://picayune.uclick.com/comics/ch";

  const searchInput = document.getElementById("calvin-search");
  const prevButton = document.getElementById("calvin-prev");
  const nextButton = document.getElementById("calvin-next");
  const image = document.getElementById("calvin-image");
  const caption = document.getElementById("calvin-caption");
  const meta = document.getElementById("calvin-meta");
  const stage = document.getElementById("calvin-stage");

  if (!searchInput || !prevButton || !nextButton || !image || !caption || !meta || !stage) {
    return;
  }

  let allStrips = [];
  let filteredStrips = [];
  let currentIndex = 0;
  let fuse = null;
  let preloadImage = null;

  const setLoading = (value) => {
    stage.classList.toggle("is-loading", value);
  };

  const imageUrlForId = (id) => {
    const year = id.slice(0, 4);
    const shortId = id.slice(2);
    return `${IMAGE_BASE}/${year}/ch${shortId}.gif`;
  };

  const formatDate = (id) => {
    if (!id || id.length !== 8) {
      return id || "";
    }
    return `${id.slice(0, 4)}-${id.slice(4, 6)}-${id.slice(6)}`;
  };

  const updateMeta = () => {
    if (filteredStrips.length === 0) {
      meta.textContent = "No matches.";
      return;
    }
    const current = filteredStrips[currentIndex];
    const total = allStrips.length;
    const shown = filteredStrips.length;
    const date = formatDate(current.id);
    const suffix = shown === total ? `${shown} strips` : `${shown} of ${total} strips`;
    meta.textContent = `${date} - ${suffix}`;
  };

  const updateButtons = () => {
    prevButton.disabled = filteredStrips.length === 0 || currentIndex <= 0;
    nextButton.disabled = filteredStrips.length === 0 || currentIndex >= filteredStrips.length - 1;
  };

  const renderStrip = () => {
    if (filteredStrips.length === 0) {
      image.removeAttribute("src");
      image.alt = "";
      caption.textContent = "No matches.";
      updateMeta();
      updateButtons();
      return;
    }

    const strip = filteredStrips[currentIndex];
    setLoading(true);
    image.src = imageUrlForId(strip.id);
    image.alt = strip.quote;

    const quoteNode = document.createTextNode(strip.quote);
    const idNode = document.createElement("em");
    idNode.textContent = `#${strip.id}`;
    caption.replaceChildren(quoteNode, idNode);

    updateMeta();
    updateButtons();
  };

  const preloadNext = () => {
    if (filteredStrips.length === 0) {
      preloadImage = null;
      return;
    }
    const nextIndex = currentIndex + 1;
    if (nextIndex >= filteredStrips.length) {
      preloadImage = null;
      return;
    }
    const nextStrip = filteredStrips[nextIndex];
    preloadImage = new Image();
    preloadImage.src = imageUrlForId(nextStrip.id);
  };

  const setHash = (id) => {
    if (!id) {
      return;
    }
    const hash = `#${id}`;
    if (location.hash !== hash) {
      history.replaceState(null, "", hash);
      syncFromHash();
    } else {
      syncFromHash();
    }
  };

  const applyFilter = (query, keepId) => {
    const trimmed = query.trim();
    if (!trimmed) {
      filteredStrips = [...allStrips];
    } else {
      filteredStrips = fuse.search(trimmed).map((result) => result.item);
    }

    if (filteredStrips.length === 0) {
      currentIndex = 0;
      renderStrip();
      return;
    }

    if (keepId) {
      const index = filteredStrips.findIndex((strip) => strip.id === keepId);
      if (index >= 0) {
        currentIndex = index;
      } else {
        currentIndex = 0;
        setHash(filteredStrips[0].id);
        return;
      }
    } else {
      currentIndex = 0;
      setHash(filteredStrips[0].id);
      return;
    }

    renderStrip();
  };

  const syncFromHash = () => {
    const id = location.hash.replace(/^#/, "");
    if (!id) {
      setHash(filteredStrips[0]?.id || allStrips[0]?.id);
      return;
    }

    const index = filteredStrips.findIndex((strip) => strip.id === id);
    if (index === -1) {
      if (searchInput.value && filteredStrips.length > 0) {
        setHash(filteredStrips[0].id);
      }
      return;
    }

    currentIndex = index;
    renderStrip();
  };

  const handleSearch = () => {
    const query = searchInput.value;
    const currentId = filteredStrips[currentIndex]?.id;
    applyFilter(query, currentId);
  };

  const handleKeys = (event) => {
    const target = event.target;
    const isEditable = target.isContentEditable
      || ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName);

    if (isEditable) {
      return;
    }

    if (event.key === "ArrowLeft") {
      prevButton.click();
    }
    if (event.key === "ArrowRight") {
      nextButton.click();
    }
  };

  const loadData = async () => {
    setLoading(true);
    const response = await fetch(DATA_URL, { cache: "no-store" });
    const text = await response.text();
    allStrips = text
      .trim()
      .split(/\r?\n/)
      .map((line) => line.split("\t"))
      .filter(([id, quote]) => id && quote)
      .map(([id, quote]) => ({ id: id.trim(), quote: quote.trim() }))
      .filter((strip) => strip.id !== "id");

    fuse = new Fuse(allStrips, {
      keys: ["quote"],
      threshold: 0.35,
      distance: 120,
      ignoreLocation: true,
      minMatchCharLength: 2,
    });

    filteredStrips = [...allStrips];
    setLoading(false);
    if (!location.hash && filteredStrips.length > 0) {
      setHash(filteredStrips[0].id);
      return;
    }
    syncFromHash();
  };

  image.addEventListener("load", () => {
    setLoading(false);
    preloadNext();
  });

  image.addEventListener("error", () => {
    setLoading(false);
    caption.textContent = "Failed to load this strip.";
  });

  prevButton.addEventListener("click", () => {
    if (currentIndex > 0) {
      setHash(filteredStrips[currentIndex - 1].id);
    }
  });

  nextButton.addEventListener("click", () => {
    if (currentIndex < filteredStrips.length - 1) {
      setHash(filteredStrips[currentIndex + 1].id);
    }
  });

  searchInput.addEventListener("input", handleSearch);
  window.addEventListener("hashchange", syncFromHash);
  document.addEventListener("keydown", handleKeys);

  loadData().catch(() => {
    setLoading(false);
    caption.textContent = "Failed to load strips.";
  });
})();
