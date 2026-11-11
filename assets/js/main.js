/* William Lai & Co: menu, reveals, years count, HMRC deadlines, tax estimator, MTD checker, contact form */
(function () {
  var T = window.WLAI || {};
  var LANG = document.documentElement.lang || "en-GB";
  var LOCALE = LANG.indexOf("zh") === 0 ? "zh-HK" : "en-GB";
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  // ---------------------------------------------------------------- header & menu
  var header = $("[data-header]");
  var lastY = window.scrollY;
  function onHeader() {
    var y = window.scrollY;
    header.classList.toggle("is-scrolled", y > 20);
    header.classList.toggle("is-hidden", y > 520 && y > lastY && !document.body.classList.contains("menu-open"));
    lastY = y;
  }
  var btn = $(".menu-btn"), menu = $("#menu");
  function setMenu(open) {
    btn.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("menu-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { menu.hidden = false; requestAnimationFrame(function () { menu.classList.add("is-open"); }); }
    else { menu.classList.remove("is-open"); setTimeout(function () { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 400); }
  }
  if (btn && menu) {
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.classList.contains("is-open")) { setMenu(false); btn.focus(); } });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  }

  // ---------------------------------------------------------------- London date
  function londonNow() {
    var o = {};
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit" })
      .formatToParts(new Date()).forEach(function (p) { o[p.type] = p.value; });
    return { y: +o.year, m: +o.month, d: +o.day };
  }
  var now = londonNow();
  $$("[data-year]").forEach(function (el) { el.textContent = now.y; });
  $$("[data-since]").forEach(function (el) {
    el.setAttribute("data-count", now.y - +el.getAttribute("data-since"));
    el.textContent = el.getAttribute("data-count");
  });

  // ---------------------------------------------------------------- reveals & count-up
  var revealables = $$(".split, .reveal-up");
  var hasIO = "IntersectionObserver" in window;
  if (hasIO && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    revealables.forEach(function (el) {
      if (el.closest(".hero, .page-hero")) requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add("is-in"); }); });
      else io.observe(el);
    });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }
  var cio = hasIO && !reduced ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      cio.unobserve(en.target);
      var el = en.target, end = +el.getAttribute("data-count"), t0 = performance.now();
      (function tick(t) {
        var k = Math.min(1, (t - t0) / 1400), e = 1 - Math.pow(1 - k, 4);
        el.textContent = Math.round(end * e);
        if (k < 1) requestAnimationFrame(tick);
      })(t0);
    });
  }, { threshold: .5 }) : null;
  if (cio) $$("[data-count]").forEach(function (el) { el.textContent = "0"; cio.observe(el); });

  // ---------------------------------------------------------------- scroll-linked progress lines
  var progressEls = $$("[data-progress]");
  var ticking = false;
  function progress(el) {
    var r = el.getBoundingClientRect(), vh = window.innerHeight;
    return Math.max(0, Math.min(1, (vh * .75 - r.top) / (r.height + vh * .25)));
  }
  function onScroll() {
    ticking = false;
    onHeader();
    if (!reduced) progressEls.forEach(function (el) { el.style.setProperty("--p", progress(el).toFixed(3)); });
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  // ---------------------------------------------------------------- HMRC deadlines
  function utc(y, m, d) { return new Date(Date.UTC(y, m - 1, d)); }
  var today = utc(now.y, now.m, now.d);
  function fmt(date, opts) { return new Intl.DateTimeFormat(LOCALE, Object.assign({ timeZone: "UTC" }, opts)).format(date); }
  function longDate(date) { return fmt(date, { day: "numeric", month: "long", year: "numeric" }); }
  function shortDate(date) { return fmt(date, { day: "numeric", month: "short", year: "numeric" }); }
  function ty(start) { return start + "/" + String(start + 1).slice(2); }
  function daysUntil(date) { return Math.round((date - today) / 864e5); }
  function inText(n) { return n === 0 ? T.today : n === 1 ? T.tomorrow : (T.inDays || "").replace("{n}", n); }
  var MTD_START = utc(2026, 8, 7); // first quarterly update under MTD for Income Tax
  function upcomingDeadlines(count) {
    var list = [];
    for (var y = now.y - 1; y <= now.y + 2; y++) {
      list.push({ date: utc(y, 1, 31), key: "jan", ty: ty(y - 2) });
      list.push({ date: utc(y, 7, 31), key: "jul", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 5), key: "oct5", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 31), key: "oct31", ty: ty(y - 1) });
      // MTD quarterly updates: 7 Aug, 7 Nov, 7 Feb, 7 May for quarters ending 5 Jul, 5 Oct, 5 Jan, 5 Apr
      [[8, 7, 5], [11, 10, 5], [2, 1, 5], [5, 4, 5]].forEach(function (q) {
        list.push({ date: utc(y, q[0], 7), key: "mtd", end: utc(y, q[1], q[2]) });
      });
    }
    return list.filter(function (d) { return d.date >= today && (d.key !== "mtd" || d.date >= MTD_START); })
      .sort(function (a, b) { return a.date - b.date; }).slice(0, count);
  }
  function label(d) {
    var s = T.dl[d.key].replace("{ty}", d.ty || "");
    return d.end ? s.replace("{end}", fmt(d.end, { day: "numeric", month: "long" })) : s;
  }
  if (T.dl) {
    var up = upcomingDeadlines(6);
    $$("[data-next-deadline]").forEach(function (el) {
      $("[data-dl-date]", el).textContent = longDate(up[0].date);
      $("[data-dl-in]", el).textContent = inText(daysUntil(up[0].date));
      el.hidden = false;
    });
    var cd = $("[data-countdown]");
    if (cd) {
      var n = daysUntil(up[0].date);
      var nEl = $("[data-cd-days]", cd);
      nEl.setAttribute("data-count", n);
      nEl.textContent = n;
      if (cio) { nEl.textContent = "0"; cio.observe(nEl); }
      $("[data-cd-unit]", cd).textContent = n === 1 ? T.day : T.days;
      $("[data-cd-until]", cd).textContent = (T.until || "{date}").replace("{date}", longDate(up[0].date));
      $("[data-cd-what]", cd).textContent = label(up[0]);
      var ol = $("[data-deadlines]", cd);
      ol.innerHTML = "";
      up.slice(1).forEach(function (d) {
        var li = document.createElement("li");
        li.innerHTML = '<span class="dl-d"></span><span class="dl-l"></span><span class="dl-in"></span>';
        $(".dl-d", li).textContent = shortDate(d.date);
        $(".dl-l", li).textContent = label(d);
        $(".dl-in", li).textContent = inText(daysUntil(d.date));
        ol.appendChild(li);
      });
    }
  }

  // ---------------------------------------------------------------- 2026/27 income tax & NI estimator (rUK)
  var money = function (n) { return "£" + Math.round(n).toLocaleString("en-GB"); };
  var parseMoney = function (v) { var n = parseFloat(String(v).replace(/[^0-9.]/g, "")); return isFinite(n) ? n : 0; };
  function incomeTax(income) {
    var pa = Math.max(0, 12570 - Math.floor(Math.max(0, income - 100000) / 2));
    var taxable = Math.max(0, income - pa);
    var tax = Math.min(taxable, 37700) * .2 + Math.max(0, Math.min(taxable, 125140) - 37700) * .4 + Math.max(0, taxable - 125140) * .45;
    return { pa: pa, tax: tax };
  }
  function ni(income, self) {
    var main = self ? .06 : .08;
    return Math.max(0, Math.min(income, 50270) - 12570) * main + Math.max(0, income - 50270) * .02;
  }
  var taxForm = $("[data-tax-calc]");
  if (taxForm && T.tax) {
    var tout = $("[data-tax-out]", taxForm), bar = $("[data-tax-bar]", taxForm);
    var renderTax = function () {
      var inc = Math.min(parseMoney(taxForm.elements.income.value), 1e8);
      var self = taxForm.elements.kind.value === "self";
      var it = incomeTax(inc), n = ni(inc, self), total = it.tax + n;
      var rows = [
        ["", T.tax.pa, money(it.pa)],
        ["", T.tax.tax, money(it.tax)],
        ["", T.tax.ni + " · " + (self ? T.tax.c4 : T.tax.c1), money(n)],
        ["total", T.tax.total, money(total) + "<small>" + T.tax.eff + " " + (inc ? (total / inc * 100).toFixed(1) : "0.0") + "%</small>"],
        ["take", T.tax.take, money(inc - total) + "<small>" + money((inc - total) / 12) + " / " + (LOCALE === "zh-HK" ? "月" : "month") + "</small>"]
      ];
      tout.innerHTML = rows.map(function (r) { return '<div class="' + r[0] + '"><dt>' + r[1] + "</dt><dd>" + r[2] + "</dd></div>"; }).join("");
      $(".bar-tax", bar).style.width = (inc ? it.tax / inc * 100 : 0) + "%";
      $(".bar-ni", bar).style.width = (inc ? n / inc * 100 : 0) + "%";
    };
    taxForm.addEventListener("input", renderTax);
    taxForm.addEventListener("change", renderTax);
    taxForm.addEventListener("submit", function (e) { e.preventDefault(); });
    taxForm.elements.income.addEventListener("blur", function () {
      var v = parseMoney(this.value); this.value = v ? Math.round(v).toLocaleString("en-GB") : "";
    });
    renderTax();
  }

  // ---------------------------------------------------------------- Making Tax Digital checker
  var mtdForm = $("[data-mtd-check]");
  if (mtdForm && T.mtd) {
    var mout = $("[data-mtd-out]", mtdForm);
    var nextMtd = (T.dl ? upcomingDeadlines(12) : []).filter(function (d) { return d.key === "mtd"; })[0];
    var renderMtd = function () {
      var v = parseMoney(mtdForm.elements.income.value);
      var state = v > 50000 ? "in26" : v > 30000 ? "in27" : v > 20000 ? "in28" : "out";
      mout.setAttribute("data-state", state);
      mout.innerHTML = "<p>" + T.mtd[state].replace("{next}", nextMtd ? longDate(nextMtd.date) : "") + "</p>";
    };
    mtdForm.addEventListener("input", renderMtd);
    mtdForm.addEventListener("submit", function (e) { e.preventDefault(); });
    mtdForm.elements.income.addEventListener("blur", function () {
      var v = parseMoney(this.value); this.value = v ? Math.round(v).toLocaleString("en-GB") : "";
    });
    renderMtd();
  }

  // ---------------------------------------------------------------- services table of contents
  var tocLinks = $$(".toc a[href^='#']");
  if (tocLinks.length && hasIO) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
        var a = byId[en.target.id];
        if (!a) return;
        a.classList.add("is-active");
        if (window.innerWidth <= 960) a.closest("ul").scrollTo({ left: a.offsetLeft - 16, behavior: reduced ? "auto" : "smooth" });
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    $$(".svc-section").forEach(function (s) { tio.observe(s); });
  }

  // ---------------------------------------------------------------- contact form → email app
  var form = $("[data-contact-form]");
  if (form) {
    var want = (location.search.match(/[?&]service=(\w+)/) || [])[1];
    if (want) $$("option", form.elements.service).forEach(function (o) { if (o.getAttribute("data-id") === want) o.selected = true; });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements, ok = true;
      ["name", "email", "message"].forEach(function (k) {
        var bad = !f[k].value.trim() || (k === "email" && !/^\S+@\S+\.\S+$/.test(f[k].value));
        f[k].setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad) ok = false;
      });
      $("[data-form-error]", form).hidden = ok;
      if (!ok) { $("[aria-invalid='true']", form).focus(); return; }
      var body = [
        f.message.value.trim(), "", "—",
        T.mailName + ": " + f.name.value.trim(),
        "Email: " + f.email.value.trim(),
        f.phone.value.trim() ? T.mailPhone + ": " + f.phone.value.trim() : null,
        T.mailService + ": " + f.service.value,
        T.mailLang + ": " + f.lang.value
      ].filter(function (l) { return l !== null; }).join("\n");
      var subject = T.mailSubject + " — " + f.service.value + " — " + f.name.value.trim();
      window.location.href = "mailto:wlai@accountanttax.co.uk?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
