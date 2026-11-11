"""Shared header, footer, page shell, contact details and UI strings for both languages."""
import hashlib
import json
import os

LANGS = {
    "en": {"dir": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"dir": "zh/", "html": "zh-Hant", "label": "中文", "name": "繁體中文"},
}

SITE = "https://accountanttax.co.uk/"
OLD_SITE = "https://accountanttax.co.uk/"
PHONE_DISPLAY = "07920 045128"
PHONE_INTL = "+44 7920 045128"
PHONE_TEL = "+447920045128"
EMAIL = "wlai@accountanttax.co.uk"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=24+Darfield+Avenue+Sheffield+S20+6SU"
FOUNDED = 2007


def L(en, zh):
    return {"en": en, "zh": zh}


def r(x, lang):
    return x[lang] if isinstance(x, dict) else x


def lines(text):
    """Split a headline on '|' into masked lines for the reveal animation."""
    return "".join(f'<span class="line"><span>{part}</span></span>' for part in text.split("|"))


NAV = [
    ("services.html", L("Services", "服務範圍")),
    ("guides.html", L("Tax guides", "稅務指南")),
    ("about.html", L("About", "關於我們")),
    ("contact.html", L("Contact", "聯絡我們")),
]

ADDRESS = L(["24 Darfield Avenue", "Sheffield S20 6SU"],
            ["24 Darfield Avenue", "Sheffield（錫菲） S20 6SU"])

UI = {
    "skip": L("Skip to content", "跳至正文"),
    "menu": L("Menu", "選單"),
    "call": L("Call", "致電"),
    "email": L("Email", "電郵"),
    "visit": L("Map", "地圖"),
    "hours": L("Appointments", "預約會面"),
    "hours_text": L("By appointment, at our office<br>or at your premises", "請先預約，可於本所<br>或閣下公司會面"),
    "office": L("Office", "辦事處"),
    "pages": L("Pages", "頁面"),
    "language": L("Language", "語言"),
    "legal": L("Privacy &amp; legal", "私隱政策及法律聲明"),
    "directions": L("Get directions", "查看地圖"),
    "footer_q": L("A tax question|you’d like answered?", "稅務或帳目|有疑問？"),
    "footer_lead": L("Call or email William directly — in English, Cantonese or Putonghua. No language barrier.",
                     "歡迎直接致電或電郵 William，可用英語、廣東話或普通話溝通，沒有語言障礙。"),
    "reg": L("William Lai &amp; Co International Accountants · Sheffield, South Yorkshire",
             "William Lai &amp; Co 國際會計師事務所 · 英國南約克郡錫菲"),
    "body": L("William Lai practises under a practising certificate issued by the Association of International Accountants (AIA).",
              "William Lai 持有英國國際會計師公會（AIA）發出的執業證書執業。"),
    "top": L("Back to top", "返回頂部"),
    "concept": L("Concept", "概念"),
    "concept_long": L(f'Concept redesign. Not the <a href="{OLD_SITE}" target="_blank" rel="noopener">official William Lai &amp; Co website</a>.',
                      f'概念設計展示，並非 <a href="{OLD_SITE}" target="_blank" rel="noopener">William Lai &amp; Co 官方網站</a>。'),
    "concept_by": L("Designed by ", "設計："),
    "concept_note": L("Unofficial redesign concept by", "非官方概念設計："),
}

# Strings main.js needs (deadlines, calculators, form)
JS_STRINGS = {
    "en": {
        "today": "today", "tomorrow": "tomorrow", "inDays": "in {n} days", "days": "days", "day": "day",
        "until": "until {date}",
        "dl": {
            "jan": "Self Assessment online return and balancing payment for {ty}",
            "jul": "Second payment on account for {ty}",
            "oct5": "Register for Self Assessment if you started self-employment or letting in {ty}",
            "oct31": "Paper Self Assessment return deadline for {ty}",
            "mtd": "Making Tax Digital quarterly update for the quarter to {end} (if you’re in MTD)",
        },
        "tax": {"tax": "Income tax", "ni": "National Insurance", "total": "Total tax and NI", "take": "Left after tax and NI",
                "eff": "Overall rate", "pa": "Personal Allowance used", "c1": "Class 1 (employee)", "c4": "Class 4 (self-employed)"},
        "mtd": {
            "in26": "<strong>You’re in from 6 April 2026.</strong> Your 2024/25 qualifying income was over £50,000, so you should already be keeping digital records and sending quarterly updates. The next update is due on {next}.",
            "in27": "<strong>You’ll need to join from 6 April 2027</strong>, if your 2025/26 qualifying income is also over £30,000. Start using MTD-compatible software before then.",
            "in28": "<strong>You’ll need to join from 6 April 2028</strong>, if your 2026/27 qualifying income is also over £20,000.",
            "out": "<strong>Not required yet.</strong> At £20,000 or less, you’re below every threshold announced so far. You can still sign up voluntarily.",
        },
        "mailSubject": "Website enquiry", "mailName": "Name", "mailPhone": "Phone", "mailLang": "Preferred language",
        "mailService": "Service",
    },
    "zh": {
        "today": "今天", "tomorrow": "明天", "inDays": "還有 {n} 天", "days": "天", "day": "天",
        "until": "距離 {date}",
        "dl": {
            "jan": "{ty} 稅務年度網上個人報稅及結算繳稅截止",
            "jul": "{ty} 稅務年度第二期預繳稅款",
            "oct5": "如於 {ty} 稅務年度開始自僱或出租物業，須登記個人報稅",
            "oct31": "{ty} 稅務年度紙本個人報稅表截止",
            "mtd": "數碼報稅（MTD）季度申報：截至 {end} 的季度（如適用）",
        },
        "tax": {"tax": "入息稅", "ni": "國民保險供款", "total": "稅款及國民保險合計", "take": "扣除後實得",
                "eff": "整體稅率", "pa": "已使用個人免稅額", "c1": "第一類（受僱）", "c4": "第四類（自僱）"},
        "mtd": {
            "in26": "<strong>閣下由 2026 年 4 月 6 日起已須參加。</strong>由於 2024/25 年度合資格收入超過 £50,000，閣下現時應已使用數碼記帳並遞交季度申報。下一次申報截止日為 {next}。",
            "in27": "<strong>閣下須於 2027 年 4 月 6 日起參加</strong>（如 2025/26 年度合資格收入亦超過 £30,000），請於此之前開始使用 MTD 兼容軟件。",
            "in28": "<strong>閣下須於 2028 年 4 月 6 日起參加</strong>（如 2026/27 年度合資格收入亦超過 £20,000）。",
            "out": "<strong>暫時毋須參加。</strong>£20,000 或以下低於目前公佈的所有門檻，但閣下仍可自願登記。",
        },
        "mailSubject": "網站查詢", "mailName": "姓名", "mailPhone": "電話", "mailLang": "希望使用的語言",
        "mailService": "查詢服務",
    },
}

ICON = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrow-ne": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
}

# Monogram: W and L set inside a ruled ledger box with a double rule underneath (the way a total is ruled off).
MARK_SVG = """<svg class="mark" viewBox="0 0 36 36" aria-hidden="true">
  <rect class="mark-box" x="1" y="1" width="34" height="34" rx="2"/>
  <path class="mark-wl" d="M7 9.5l3 13 3-9.5 3 9.5 3-13M23 9.5v13h6.5"/>
  <path class="mark-rule" d="M7 27h22M7 30h22"/>
</svg>"""


def lang_switch(lang, page):
    prefix = "../" if LANGS[lang]["dir"] else ""
    items = []
    for code, meta in LANGS.items():
        href = prefix + meta["dir"] + (page if page != "index.html" else "")
        if not href:
            href = "./"
        cur = ' aria-current="true"' if code == lang else ""
        items.append(f'<a href="{href}" lang="{meta["html"]}" hreflang="{meta["html"]}"{cur}>{meta["label"]}</a>')
    return '<div class="lang" role="group" aria-label="Language / 語言">' + "".join(items) + "</div>"


_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ver(rel):
    """Short content hash for cache-busting ?v= query strings."""
    with open(os.path.join(_ROOT, "assets", rel), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def asset(lang):
    return ("../" if LANGS[lang]["dir"] else "") + "assets/"


def brand_block(lang):
    sub = "International Accountants" if lang == "en" else "國際會計師事務所"
    return f"""<a class="brand" href="./" aria-label="{'William Lai &amp; Co — home' if lang == 'en' else 'William Lai &amp; Co — 主頁'}">
      {MARK_SVG}
      <span class="brand-text"><span class="brand-name">William Lai &amp; Co</span><span class="brand-sub">{sub}</span></span>
    </a>"""


def header(lang, page):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a>' for href, label in NAV)
    big = "".join(f'<li><a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a></li>' for href, label in NAV)
    return f"""<a class="skip" href="#main">{r(UI['skip'], lang)}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{r(UI['concept'], lang)}</span><span class="concept-long">{r(UI['concept_long'], lang)}</span></p>
    <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener"><span class="concept-by">{r(UI['concept_by'], lang)}</span><strong>UX CIRCLES</strong> {ICON['arrow-ne']}</a>
  </div>
</div>
<header class="site-header" data-header>
  <div class="wrap header-inner">
    {brand_block(lang)}
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    {lang_switch(lang, page)}
    <a class="btn btn-ink header-cta" href="tel:{PHONE_TEL}">{ICON['phone']}<span>{PHONE_DISPLAY}</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-lines"><span></span><span></span></span><span class="sr">{r(UI['menu'], lang)}</span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <div class="wrap menu-inner">
    <ul class="menu-links">{big}</ul>
    <div class="menu-foot">
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      {lang_switch(lang, page)}
    </div>
  </div>
</div>"""


def footer(lang, page):
    nav = "".join(f'<li><a href="{h}">{r(lbl, lang)}</a></li>' for h, lbl in NAV)
    nav += f'<li><a href="legal.html">{r(UI["legal"], lang)}</a></li>'
    addr = "<br>".join(r(ADDRESS, lang))
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <h2 class="footer-q split">{lines(r(UI['footer_q'], lang))}</h2>
        <p class="footer-lead">{r(UI['footer_lead'], lang)}</p>
      </div>
      <div class="footer-contact">
        <a class="big-link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
    <div class="footer-grid">
      <div><h3 class="f-h">{r(UI['office'], lang)}</h3><p>{addr}</p><p><a class="u" href="{MAPS_URL}" rel="noopener" target="_blank">{r(UI['directions'], lang)} ↗</a></p></div>
      <div><h3 class="f-h">{r(UI['hours'], lang)}</h3><p>{r(UI['hours_text'], lang)}</p></div>
      <div><h3 class="f-h">{r(UI['pages'], lang)}</h3><ul class="f-links">{nav}</ul></div>
      <div><h3 class="f-h">{r(UI['language'], lang)}</h3>{lang_switch(lang, page)}</div>
    </div>
  </div>
  <div class="wrap footer-base">
    <span>© <span data-year>2026</span> {r(UI['reg'], lang)}<br>{r(UI['body'], lang)}<br><span class="concept-note">{r(UI['concept_note'], lang)} <a class="u" href="https://ux-circles.com/professionals" target="_blank" rel="noopener">UX CIRCLES</a></span></span>
    <a href="#main" class="u">{r(UI['top'], lang)} ↑</a>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']}<span>{r(UI['call'], lang)}</span></a>
  <a href="mailto:{EMAIL}">{ICON['mail']}<span>{r(UI['email'], lang)}</span></a>
  <a href="{MAPS_URL}" target="_blank" rel="noopener">{ICON['pin']}<span>{r(UI['visit'], lang)}</span></a>
</nav>"""


PRELOAD = {"en": ["newsreader", "hanken-grotesk"], "zh": ["newsreader", "noto-serif-tc-600"]}


def page(lang, name, title, description, body, body_class=""):
    a = asset(lang)
    meta = LANGS[lang]
    path = "" if name == "index.html" else name
    alts = "\n".join(f'<link rel="alternate" hreflang="{m["html"]}" href="{SITE}{m["dir"]}{path}">' for m in LANGS.values())
    js = json.dumps(JS_STRINGS[lang], ensure_ascii=False)
    preloads = "\n".join(f'<link rel="preload" href="{a}fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>'
                         for f in PRELOAD[lang])
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "AccountingService",
        "name": "William Lai & Co International Accountants",
        "url": SITE, "telephone": PHONE_INTL, "email": EMAIL, "foundingDate": str(FOUNDED),
        "founder": {"@type": "Person", "name": "William Lai",
                    "memberOf": [{"@type": "Organization", "name": "Association of International Accountants"},
                                 {"@type": "Organization", "name": "Hong Kong Institute of Certified Public Accountants"}]},
        "address": {"@type": "PostalAddress", "streetAddress": "24 Darfield Avenue",
                    "addressLocality": "Sheffield", "postalCode": "S20 6SU", "addressCountry": "GB"},
        "areaServed": ["Sheffield", "South Yorkshire", "United Kingdom"], "knowsLanguage": ["en", "yue", "cmn"],
    }, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{meta['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{meta['dir']}{path}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'zh_HK'}">
<meta name="theme-color" content="#f1efe9">
<link rel="icon" href="{a}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{a}img/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.png">
{preloads}
<link rel="stylesheet" href="{a}css/style.css?v={ver("css/style.css")}">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{schema}</script>
</head>
<body class="{body_class}">
{header(lang, name)}
<main id="main">
{body}
</main>
{footer(lang, name)}
<script>window.WLAI = {js};</script>
<script src="{a}js/main.js?v={ver("js/main.js")}" defer></script>
</body>
</html>
"""
