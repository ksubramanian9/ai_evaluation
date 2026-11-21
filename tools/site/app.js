(function () {
  var root = document.body.dataset.root || "";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  // theme
  $(".theme-btn").addEventListener("click", function () {
    var cur = document.documentElement.dataset.theme ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
  });

  // mobile nav
  var menu = $(".menu-btn"), scrim = $(".scrim");
  function nav(open) {
    document.body.classList.toggle("nav-open", open);
    menu.setAttribute("aria-expanded", open);
    scrim.hidden = !open;
  }
  menu.addEventListener("click", function () { nav(!document.body.classList.contains("nav-open")); });
  scrim.addEventListener("click", function () { nav(false); });

  // keep current node visible in sidebar
  var cur = $('.side [aria-current="page"]');
  if (cur) cur.scrollIntoView({ block: "center" });

  // on-this-page highlighting
  var tocLinks = $$(".toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && map[e.target.id]) {
          tocLinks.forEach(function (a) { a.classList.remove("on"); });
          map[e.target.id].classList.add("on");
        }
      });
    }, { rootMargin: "-70px 0px -70% 0px" });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  // filters
  $$(".filterable").forEach(function (box) {
    var ctrls = $$("[data-f]", box), items = $$(".node-item", box), count = $(".count", box);
    function apply() {
      var f = {};
      ctrls.forEach(function (c) { f[c.dataset.f] = c.value.trim().toLowerCase(); });
      var shown = 0;
      items.forEach(function (it) {
        var d = it.dataset;
        var ok = (!f.q || d.text.indexOf(f.q) > -1) && (!f.branch || d.branch === f.branch) &&
          (!f.depth || d.depth.toLowerCase() === f.depth) && (!f.status || d.status === f.status) &&
          (!f.bridge || d.bridge === f.bridge) && (!f.tag || (" " + d.tags + " ").indexOf(" " + f.tag + " ") > -1);
        it.hidden = !ok; if (ok) shown++;
      });
      $$(".stage", box).forEach(function (s) { s.classList.toggle("empty", !$(".node-item:not([hidden])", s)); });
      if (count) count.textContent = shown + " of " + items.length;
      try { history.replaceState(null, "", "#" + new URLSearchParams(Object.keys(f).filter(function (k) { return f[k]; }).map(function (k) { return [k, f[k]]; }))); } catch (e) {}
    }
    var h = new URLSearchParams(location.hash.slice(1));
    ctrls.forEach(function (c) { if (h.get(c.dataset.f)) c.value = h.get(c.dataset.f); c.addEventListener("input", apply); });
    apply();
  });

  // search palette
  var pal = $(".palette"), input = $("input", pal), res = $(".results", pal), sel = 0, shown = [];
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function open() { pal.hidden = false; input.value = ""; input.focus(); run(); }
  function close() { pal.hidden = true; }
  $$("[data-open-search]").forEach(function (b) { b.addEventListener("click", open); });
  pal.addEventListener("mousedown", function (e) { if (e.target === pal) close(); });
  document.addEventListener("keydown", function (e) {
    var typing = /input|textarea|select/i.test((e.target.tagName || ""));
    if ((e.key === "/" && !typing) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) { e.preventDefault(); open(); }
    else if (e.key === "Escape") { close(); nav(false); }
  });
  function score(it, terms) {
    var t = it.t.toLowerCase(), g = (it.g || "").toLowerCase(), x = (it.x || "").toLowerCase(), s = 0;
    for (var i = 0; i < terms.length; i++) {
      var q = terms[i], hit = 0;
      if (t.indexOf(q) > -1) hit += t.indexOf(q) === 0 ? 12 : 8;
      if (g.indexOf(q) > -1) hit += 4;
      var p = x.indexOf(q);
      if (p > -1) { hit += 2; var n = 0, k = -1; while ((k = x.indexOf(q, k + 1)) > -1 && n < 8) n++; hit += Math.min(n, 8) * .25; }
      if (!hit) return 0;
      s += hit;
    }
    return s;
  }
  function snippet(it, terms) {
    var x = it.x || "", l = x.toLowerCase(), p = l.indexOf(terms[0]);
    if (p < 0) return it.b;
    var a = Math.max(0, p - 50), out = esc(x.slice(a, a + 140));
    terms.forEach(function (q) { out = out.replace(new RegExp("(" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<em>$1</em>"); });
    return (a ? "…" : "") + out + "…";
  }
  function run() {
    var terms = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    var data = window.SEARCH || [];
    shown = terms.length
      ? data.map(function (it) { return [score(it, terms), it]; }).filter(function (p) { return p[0] > 0; })
          .sort(function (a, b) { return b[0] - a[0]; }).slice(0, 12).map(function (p) { return p[1]; })
      : data.filter(function (it) { return it.k === "Page"; }).concat(data.filter(function (it) { return it.k === "Node"; }).slice(0, 6));
    sel = 0;
    res.innerHTML = shown.length ? shown.map(function (it, i) {
      return '<a class="res' + (i ? "" : " sel") + '" role="option" href="' + root + it.u + '"><span class="k">' + it.k + "</span><b>" + esc(it.t) + "</b><small>" +
        (terms.length ? snippet(it, terms) : esc(it.b)) + "</small></a>";
    }).join("") : '<div class="noresult">No matches.</div>';
  }
  input.addEventListener("input", run);
  input.addEventListener("keydown", function (e) {
    var els = $$(".res", res);
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      if (!els.length) return;
      els[sel].classList.remove("sel");
      sel = (sel + (e.key === "ArrowDown" ? 1 : -1) + els.length) % els.length;
      els[sel].classList.add("sel"); els[sel].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && els[sel]) { location.href = els[sel].href; }
  });
})();
