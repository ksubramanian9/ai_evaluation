(function () {
  var G = window.GRAPH, svg = document.getElementById("graph"), NS = "http://www.w3.org/2000/svg";
  var W = 200, H = 28, GX = 90, GY = 10, PAD = 16;
  var cols = {}, pos = {}, byId = {}, up = {}, down = {};
  G.nodes.forEach(function (n) { byId[n.id] = n; (cols[n.l] = cols[n.l] || []).push(n); up[n.id] = []; down[n.id] = []; });
  G.edges.forEach(function (e) { up[e[1]].push(e[0]); down[e[0]].push(e[1]); });
  var maxRows = 0;
  Object.keys(cols).forEach(function (l) {
    cols[l].forEach(function (n, i) { pos[n.id] = { x: PAD + l * (W + GX), y: PAD + i * (H + GY) }; });
    maxRows = Math.max(maxRows, cols[l].length);
  });
  var width = PAD * 2 + (Object.keys(cols).length) * (W + GX) - GX, height = PAD * 2 + maxRows * (H + GY);
  svg.setAttribute("width", width); svg.setAttribute("height", height);
  function el(name, attrs, parent) {
    var e = document.createElementNS(NS, name);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    (parent || svg).appendChild(e); return e;
  }
  var edgeEls = G.edges.map(function (e) {
    var a = pos[e[0]], b = pos[e[1]], x1 = a.x + W, y1 = a.y + H / 2, x2 = b.x, y2 = b.y + H / 2, dx = Math.max(30, (x2 - x1) / 2);
    var p = el("path", { "class": "edge", d: "M" + x1 + "," + y1 + " C" + (x1 + dx) + "," + y1 + " " + (x2 - dx) + "," + y2 + " " + x2 + "," + y2 });
    return { e: e, p: p };
  });
  var nodeEls = {};
  G.nodes.forEach(function (n) {
    var p = pos[n.id];
    var g = el("g", { "class": "gn b" + n.b, tabindex: 0, transform: "translate(" + p.x + "," + p.y + ")", role: "link", "aria-label": n.t });
    g.style.setProperty("--c", "var(--b" + n.b + ")");
    el("rect", { width: W, height: H }, g);
    el("circle", { cx: 12, cy: H / 2, r: 4, "class": "sd st-" + n.s }, g);
    var t = el("text", { x: 24, y: H / 2 + 4 }, g);
    t.textContent = n.t.length > 28 ? n.t.slice(0, 27) + "…" : n.t;
    var title = el("title", {}, g); title.textContent = n.t;
    g.addEventListener("mouseenter", function () { focus(n.id); });
    g.addEventListener("focus", function () { focus(n.id); });
    g.addEventListener("mouseleave", clear); g.addEventListener("blur", clear);
    g.addEventListener("click", function () { location.href = "nodes/" + n.id + ".html"; });
    g.addEventListener("keydown", function (ev) { if (ev.key === "Enter") location.href = "nodes/" + n.id + ".html"; });
    nodeEls[n.id] = g;
  });
  function walk(id, map, seen) {
    map[id].forEach(function (q) { if (!seen[q]) { seen[q] = 1; walk(q, map, seen); } });
    return seen;
  }
  function focus(id) {
    var a = walk(id, up, {}), d = walk(id, down, {});
    svg.classList.add("focus");
    Object.keys(nodeEls).forEach(function (k) { nodeEls[k].classList.toggle("hit", k === id || !!a[k] || !!d[k]); nodeEls[k].classList.toggle("self", k === id); });
    edgeEls.forEach(function (o) {
      var isUp = (a[o.e[0]] || o.e[0] === id) && (a[o.e[1]] || o.e[1] === id);
      var isDown = (d[o.e[1]] || o.e[1] === id) && (d[o.e[0]] || o.e[0] === id);
      o.p.setAttribute("class", "edge" + (isUp ? " up hit" : isDown ? " down hit" : ""));
    });
  }
  function clear() {
    svg.classList.remove("focus");
    Object.keys(nodeEls).forEach(function (k) { nodeEls[k].classList.remove("hit", "self"); });
    edgeEls.forEach(function (o) { o.p.setAttribute("class", "edge"); });
  }
  // legend toggles dim branches
  var lg = document.getElementById("graph-legend"), hidden = {};
  Object.keys(G.branches).forEach(function (b) {
    var btn = document.createElement("button");
    btn.className = "b" + b; btn.style.setProperty("--c", "var(--b" + b + ")");
    btn.innerHTML = "<i></i>" + b + " " + G.branches[b];
    btn.addEventListener("click", function () {
      hidden[b] = !hidden[b]; btn.classList.toggle("off", hidden[b]);
      G.nodes.forEach(function (n) { nodeEls[n.id].style.opacity = hidden[n.b] ? .15 : ""; });
    });
    lg.appendChild(btn);
  });
})();
