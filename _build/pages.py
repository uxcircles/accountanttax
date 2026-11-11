"""Builds every page in both languages. Run: python3 _build/pages.py"""
import os

from content import CLIENTS, COMING, RATES, SERVICES, STARTUP, WHY
from layout import (ADDRESS, EMAIL, FOUNDED, ICON, L, LANGS, MAPS_URL, PHONE_DISPLAY, PHONE_TEL, lines, page, r)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOV_RATES = "https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past"


def arrow_btn(href, text, cls="btn btn-accent"):
    return f'<a class="{cls}" href="{href}"><span>{text}</span>{ICON["arrow"]}</a>'


def page_hero(eyebrow, title, lead):
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="label reveal-up">{eyebrow}</p>
    <h1 class="page-title split">{lines(title)}</h1>
    <p class="page-lead reveal-up">{lead}</p>
  </div>
</section>"""


def deadlines_section(lang):
    t = {
        "label": L("Key dates", "重要日期"),
        "title": L("Next HMRC|deadline", "下一個 HMRC|截止日期"),
        "after": L("Coming up after that", "之後的截止日期"),
        "note": L("Self Assessment and Making Tax Digital dates, worked out from today’s date. A late Self Assessment return costs £100 straight away, even if there’s no tax to pay.",
                  "以今天日期計算的個人報稅及數碼報稅截止日期。個人報稅表逾期遞交，即使毋須繳稅，亦會即時罰款 £100。"),
    }
    return f"""<section class="section deadlines" id="key-dates" aria-labelledby="kd-h">
  <div class="wrap dl-grid" data-countdown>
    <div>
      <p class="label reveal-up">{r(t['label'], lang)}</p>
      <h2 class="h2 split" id="kd-h">{lines(r(t['title'], lang))}</h2>
      <p class="muted reveal-up">{r(t['note'], lang)}</p>
    </div>
    <div class="dl-card reveal-up">
      <p class="dl-big"><span data-cd-days>—</span> <span class="dl-unit" data-cd-unit></span></p>
      <p class="dl-until" data-cd-until></p>
      <p class="dl-what" data-cd-what></p>
      <h3 class="dl-after">{r(t['after'], lang)}</h3>
      <ol class="dl-list" data-deadlines></ol>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ home
def home(lang):
    t = {
        "eyebrow": L("Qualified accountant in Sheffield · since 2007", "錫菲專業會計師 · 始於 2007"),
        "title": L("Accounts and tax,|handled by someone|<em>who speaks your language.</em>",
                   "會計及稅務|由懂你語言的|<em>專業會計師處理。</em>"),
        "lead": L("William Lai &amp; Co looks after sole traders, companies, landlords and builders across Sheffield and South Yorkshire — in English, Cantonese or Putonghua.",
                  "William Lai &amp; Co 為錫菲及南約克郡的自僱人士、有限公司、業主及建築商提供會計及稅務服務，可用英語、廣東話或普通話溝通。"),
        "cta": L("Arrange a free first chat", "預約免費初步諮詢"),
        "cta2": L("Our services", "服務範圍"),
        "ledger": L("Tax year 2026/27", "2026/27 稅務年度"),
        "pa": L("Personal Allowance", "個人免稅額"),
        "vat": L("VAT threshold", "增值稅門檻"),
        "mtd": L("MTD for Income Tax", "所得稅數碼報稅"),
        "mtd_v": L("over £50k", "超過 £50k"),
        "next": L("Next HMRC deadline", "下一個 HMRC 截止日期"),
        "years": L("years in practice", "年執業"),
        "langs": L("English · 廣東話 · 普通話", "English · 廣東話 · 普通話"),
        "who_label": L("Who we help", "服務對象"),
        "who_title": L("Experience where|it counts", "專注|擅長領域"),
        "svc_label": L("Services", "服務範圍"),
        "svc_title": L("Everything from|the books to the return", "由記帳|到報稅一手包辦"),
        "svc_all": L("All services", "全部服務"),
        "why_label": L("Why William Lai &amp; Co", "為何選擇我們"),
        "why_title": L("A qualified accountant,|not a call centre", "專業會計師|親自為你服務"),
        "tools_label": L("Free tools", "免費工具"),
        "tools_title": L("Check where|you stand", "先了解|自己的情況"),
        "tool1": L("Income tax estimator", "入息稅估算"),
        "tool1_p": L("See your 2026/27 income tax and National Insurance in a few seconds.", "數秒內估算 2026/27 年度入息稅及國民保險供款。"),
        "tool2": L("Do I need Making Tax Digital?", "我須要參加數碼報稅嗎？"),
        "tool2_p": L("Enter your self-employed and rental income to see when MTD applies to you.", "輸入自僱及租金收入，查看何時須參加 MTD。"),
        "tool3": L("Tax rates 2026/27", "2026/27 稅率一覽"),
        "tool3_p": L("Allowances and rates for this tax year next to last year’s, with what’s changed.", "本稅務年度與上年度的免稅額及稅率對照，並標示變動。"),
    }
    clients = "".join(f"""
        <li class="who-item reveal-up"><h3>{r(h, lang)}</h3><p>{r(p, lang)}</p></li>""" for h, p in CLIENTS)
    svc = "".join(f"""
        <li class="svc-row reveal-up"><a href="services.html#{sid}"><span class="svc-t">{r(title, lang)}</span><span class="svc-s">{r(summ, lang)}</span>{ICON['arrow']}</a></li>"""
                  for sid, title, summ, _ in SERVICES)
    why = "".join(f"""
        <li class="why-item reveal-up">{ICON['check']}<div><h3>{r(h, lang)}</h3><p>{r(p, lang)}</p></div></li>""" for h, p in WHY)
    tools = "".join(f"""
        <a class="tool-card reveal-up" href="guides.html#{anchor}"><span class="tool-n">{i}</span><h3>{r(t[k], lang)}</h3><p>{r(t[k + '_p'], lang)}</p>{ICON['arrow']}</a>"""
                    for i, (k, anchor) in enumerate([("tool1", "estimator"), ("tool2", "mtd"), ("tool3", "rates")], 1))
    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="label reveal-up">{r(t['eyebrow'], lang)}</p>
      <h1 class="display split">{lines(r(t['title'], lang))}</h1>
      <p class="lead reveal-up">{r(t['lead'], lang)}</p>
      <div class="hero-ctas reveal-up">{arrow_btn('contact.html', r(t['cta'], lang))}<a class="btn btn-line" href="services.html">{r(t['cta2'], lang)}</a></div>
    </div>
    <aside class="ledger reveal-up" aria-label="{r(t['ledger'], lang)}">
      <p class="ledger-h"><span>{r(t['ledger'], lang)}</span><span class="ledger-est">Est. {FOUNDED}</span></p>
      <dl class="ledger-rows">
        <div><dt>{r(t['pa'], lang)}</dt><dd>£12,570</dd></div>
        <div><dt>{r(t['vat'], lang)}</dt><dd>£90,000</dd></div>
        <div><dt>{r(t['mtd'], lang)}</dt><dd>{r(t['mtd_v'], lang)}</dd></div>
        <div class="ledger-next" data-next-deadline hidden><dt>{r(t['next'], lang)}</dt><dd><span data-dl-date></span><small data-dl-in></small></dd></div>
      </dl>
      <div class="ledger-total">
        <p><span class="ledger-num" data-since="{FOUNDED}">{2026 - FOUNDED}</span><span>{r(t['years'], lang)}</span></p>
        <p class="ledger-langs">{r(t['langs'], lang)}</p>
      </div>
      <div class="ledger-badges"><span>AIA</span><span>HKICPA</span></div>
    </aside>
  </div>
</section>

<section class="section" aria-labelledby="who-h">
  <div class="wrap split-grid">
    <div class="sticky-col">
      <p class="label reveal-up">{r(t['who_label'], lang)}</p>
      <h2 class="h2 split" id="who-h">{lines(r(t['who_title'], lang))}</h2>
    </div>
    <ul class="who-list">{clients}
    </ul>
  </div>
</section>

<section class="section section-ink" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="label reveal-up">{r(t['svc_label'], lang)}</p>
      <h2 class="h2 split" id="svc-h">{lines(r(t['svc_title'], lang))}</h2></div>
      {arrow_btn('services.html', r(t['svc_all'], lang), 'btn btn-on-ink')}
    </div>
    <ul class="svc-list">{svc}
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="why-h">
  <div class="wrap split-grid">
    <div class="sticky-col">
      <p class="label reveal-up">{r(t['why_label'], lang)}</p>
      <h2 class="h2 split" id="why-h">{lines(r(t['why_title'], lang))}</h2>
    </div>
    <ul class="why-list">{why}
    </ul>
  </div>
</section>

{deadlines_section(lang)}

<section class="section" aria-labelledby="tools-h">
  <div class="wrap">
    <p class="label reveal-up">{r(t['tools_label'], lang)}</p>
    <h2 class="h2 split" id="tools-h">{lines(r(t['tools_title'], lang))}</h2>
    <div class="tool-grid">{tools}
    </div>
  </div>
</section>"""
    title = L("William Lai &amp; Co | Accountants in Sheffield · English &amp; Chinese",
              "William Lai &amp; Co | 錫菲會計師 · 中英雙語會計及稅務服務")
    desc = L("Qualified accountant in Sheffield since 2007: accounts, Self Assessment, Corporation Tax, VAT, payroll and Making Tax Digital. English, Cantonese and Putonghua.",
             "自 2007 年起於錫菲執業的專業會計師：帳目、個人報稅、公司稅、增值稅、薪俸及數碼報稅，可用英語、廣東話及普通話溝通。")
    return page(lang, "index.html", r(title, lang), r(desc, lang), body, "home")


# ------------------------------------------------------------------ services
def services(lang):
    t = {
        "eyebrow": L("Services", "服務範圍"),
        "title": L("What we|do for you", "我們的|服務"),
        "lead": L("Everything a sole trader, landlord or small company needs from an accountant, from monthly bookkeeping to dealing with HMRC on your behalf.",
                  "自僱人士、業主及小型公司所需的會計服務，由每月記帳到代表閣下與 HMRC 交涉，一應俱全。"),
        "incl": L("Includes", "包括"),
        "ask": L("Ask about this", "查詢此服務"),
        "jump": L("On this page", "本頁內容"),
        "fee_label": L("Fees", "收費"),
        "fee_title": L("A fixed quote,|agreed up front", "預先確定|固定報價"),
        "fee_p": L("Every client is different, so we start with a free, no-obligation conversation about what you need. You’ll get a fixed fee in writing before any work starts, so there are no surprise bills.",
                   "每位客戶需要不同，因此我們先免費了解閣下的情況，不設任何承諾。開始工作前會以書面確定固定收費，不會有意外帳單。"),
        "fee_cta": L("Ask for a quote", "索取報價"),
    }
    toc = "".join(f'<li><a href="#{sid}">{r(title, lang)}</a></li>' for sid, title, _, _ in SERVICES)
    secs = "".join(f"""
      <section class="svc-section reveal-up" id="{sid}">
        <h2 class="h3">{r(title, lang)}</h2>
        <p class="svc-sum">{r(summ, lang)}</p>
        <h3 class="mini">{r(t['incl'], lang)}</h3>
        <ul class="ticks">{''.join(f"<li>{ICON['check']}<span>{r(i, lang)}</span></li>" for i in items)}</ul>
        <a class="u ask" href="contact.html?service={sid}">{r(t['ask'], lang)} →</a>
      </section>""" for sid, title, summ, items in SERVICES)
    body = f"""{page_hero(r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<div class="wrap svc-layout">
  <nav class="toc" aria-label="{r(t['jump'], lang)}"><p class="mini">{r(t['jump'], lang)}</p><ul>{toc}</ul></nav>
  <div class="svc-body">{secs}
  </div>
</div>
<section class="section section-ink" aria-labelledby="fee-h">
  <div class="wrap split-grid">
    <div><p class="label reveal-up">{r(t['fee_label'], lang)}</p>
    <h2 class="h2 split" id="fee-h">{lines(r(t['fee_title'], lang))}</h2></div>
    <div><p class="lead reveal-up">{r(t['fee_p'], lang)}</p>
    <p class="reveal-up">{arrow_btn('contact.html', r(t['fee_cta'], lang))}</p></div>
  </div>
</section>"""
    title = L("Services | William Lai &amp; Co, Sheffield accountants", "服務範圍 | William Lai &amp; Co 錫菲會計師")
    desc = L("Bookkeeping, annual accounts, Self Assessment, Corporation Tax, Making Tax Digital, VAT, CIS, payroll and company formation in Sheffield.",
             "錫菲會計服務：記帳、年度帳目、個人報稅、公司稅、數碼報稅、增值稅、CIS、薪俸及成立公司。")
    return page(lang, "services.html", r(title, lang), r(desc, lang), body, "services")


# ------------------------------------------------------------------ guides
def guides(lang):
    t = {
        "eyebrow": L("Tax guides &amp; tools", "稅務指南及工具"),
        "title": L("The 2026/27|tax year, explained", "2026/27|稅務年度一覽"),
        "lead": L("Rates and allowances, a quick income tax estimate, the Making Tax Digital timetable and a checklist for starting a business, kept up to date.",
                  "稅率及免稅額、入息稅快速估算、數碼報稅時間表及創業清單，資料持續更新。"),
        "est_label": L("Estimator", "估算工具"),
        "est_title": L("Income tax|estimator", "入息稅|估算"),
        "est_p": L("For 2026/27 in England, Wales and Northern Ireland. It assumes a single job or business and the standard Personal Allowance. Scottish income tax rates are different.",
                   "適用於英格蘭、威爾斯及北愛爾蘭 2026/27 年度，假設只有單一工作或生意及標準個人免稅額。蘇格蘭入息稅率有所不同。"),
        "income": L("Annual income before tax (£)", "全年稅前收入（£）"),
        "type": L("I am", "身份"),
        "employed": L("Employed", "受僱"),
        "self": L("Self-employed (profit)", "自僱（利潤）"),
        "disc": L("An estimate only. It doesn’t include pension contributions, student loans, benefits in kind or other income.",
                  "僅供參考，未計算退休金供款、學生貸款、實物福利或其他收入。"),
        "mtd_label": L("Making Tax Digital", "數碼報稅"),
        "mtd_title": L("Do I need|MTD for Income Tax?", "我須要參加|所得稅數碼報稅嗎？"),
        "mtd_p": L("Since 6 April 2026, sole traders and landlords whose <strong>qualifying income</strong> is over £50,000 must keep digital records and send HMRC an update every quarter. Qualifying income is your total self-employment turnover plus gross rental income, before expenses.",
                   "自 2026 年 4 月 6 日起，<strong>合資格收入</strong>超過 £50,000 的自僱人士及業主須以數碼方式記帳，並每季向 HMRC 申報。合資格收入指自僱營業額加總租金收入（未扣除開支）。"),
        "mtd_in": L("Self-employed turnover plus rental income (£)", "自僱營業額加租金收入（£）"),
        "mtd_tbl": [
            (L("From 6 April 2026", "2026 年 4 月 6 日起"), L("over £50,000", "超過 £50,000"), L("based on your 2024/25 return", "按 2024/25 年度報稅表")),
            (L("From 6 April 2027", "2027 年 4 月 6 日起"), L("over £30,000", "超過 £30,000"), L("based on your 2025/26 return", "按 2025/26 年度報稅表")),
            (L("From 6 April 2028", "2028 年 4 月 6 日起"), L("over £20,000", "超過 £20,000"), L("based on your 2026/27 return", "按 2026/27 年度報稅表")),
        ],
        "mtd_q": L("Quarterly updates are due on 7 August, 7 November, 7 February and 7 May. HMRC doesn’t provide free software, so you’ll need an MTD-compatible product; we can help you choose one.",
                   "季度申報截止日為 8 月 7 日、11 月 7 日、2 月 7 日及 5 月 7 日。HMRC 不提供免費軟件，閣下須使用 MTD 兼容產品，我們可協助挑選。"),
        "rates_label": L("Rates &amp; allowances", "稅率及免稅額"),
        "rates_title": L("Tax rates|2026/27", "2026/27|稅率一覽"),
        "rates_p": L("England, Wales and Northern Ireland. Changes from last year are in bold.", "適用於英格蘭、威爾斯及北愛爾蘭，與上年度不同之處以粗體標示。"),
        "col_item": L("Allowance or rate", "項目"),
        "source": L("Source: HMRC. Full tables on GOV.UK", "資料來源：HMRC，完整表格見 GOV.UK"),
        "coming": L("Already announced", "已公佈的變動"),
        "start_label": L("Starting a business", "創業"),
        "start_title": L("Six things to sort|before you start", "創業前|六件要事"),
        "start_cta": L("Talk your plans through with us", "與我們商討創業計劃"),
        "dl_more": L("More guides on GOV.UK", "更多 GOV.UK 指南"),
    }
    rates = "".join(f"""
      <tbody>
        <tr class="grp"><th colspan="3" scope="colgroup">{r(group, lang)}</th></tr>
        {''.join(f'<tr><th scope="row">{r(label, lang)}</th><td>{a}</td><td>{b}</td></tr>' for label, a, b in rows)}
      </tbody>""" for group, rows in RATES)
    coming = "".join(f"<li>{r(c, lang)}</li>" for c in COMING)
    mtd_rows = "".join(f"<tr><th scope=\"row\">{r(a, lang)}</th><td>{r(b, lang)}</td><td>{r(c, lang)}</td></tr>" for a, b, c in t["mtd_tbl"])
    steps = "".join(f"""
      <li class="step reveal-up"><span class="step-n">{i}</span><div><h3>{r(h, lang)}</h3><p>{r(p, lang)}</p></div></li>"""
                    for i, (h, p) in enumerate(STARTUP, 1))
    body = f"""{page_hero(r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<nav class="wrap jump reveal-up" aria-label="Guides">
  <a href="#estimator">{r(t['est_title'], lang).replace('|', ' ')}</a>
  <a href="#mtd">{r(t['mtd_label'], lang)}</a>
  <a href="#rates">{r(t['rates_label'], lang)}</a>
  <a href="#key-dates">{r(L('Key dates', '重要日期'), lang)}</a>
  <a href="#start">{r(t['start_label'], lang)}</a>
</nav>

<section class="section" id="estimator" aria-labelledby="est-h">
  <div class="wrap split-grid">
    <div>
      <p class="label reveal-up">{r(t['est_label'], lang)}</p>
      <h2 class="h2 split" id="est-h">{lines(r(t['est_title'], lang))}</h2>
      <p class="muted reveal-up">{r(t['est_p'], lang)}</p>
    </div>
    <form class="tool reveal-up" data-tax-calc>
      <label class="field"><span>{r(t['income'], lang)}</span>
        <span class="money"><span aria-hidden="true">£</span><input name="income" inputmode="numeric" autocomplete="off" value="35,000"></span></label>
      <fieldset class="seg"><legend>{r(t['type'], lang)}</legend>
        <label><input type="radio" name="kind" value="emp" checked><span>{r(t['employed'], lang)}</span></label>
        <label><input type="radio" name="kind" value="self"><span>{r(t['self'], lang)}</span></label>
      </fieldset>
      <dl class="tool-out" data-tax-out aria-live="polite"></dl>
      <div class="bar" data-tax-bar aria-hidden="true"><span class="bar-tax"></span><span class="bar-ni"></span></div>
      <p class="fine">{r(t['disc'], lang)}</p>
    </form>
  </div>
</section>

<section class="section section-tint" id="mtd" aria-labelledby="mtd-h">
  <div class="wrap split-grid">
    <div>
      <p class="label reveal-up">{r(t['mtd_label'], lang)}</p>
      <h2 class="h2 split" id="mtd-h">{lines(r(t['mtd_title'], lang))}</h2>
      <p class="reveal-up">{r(t['mtd_p'], lang)}</p>
      <table class="tbl reveal-up"><tbody>{mtd_rows}</tbody></table>
      <p class="muted reveal-up">{r(t['mtd_q'], lang)}</p>
    </div>
    <form class="tool reveal-up" data-mtd-check>
      <label class="field"><span>{r(t['mtd_in'], lang)}</span>
        <span class="money"><span aria-hidden="true">£</span><input name="income" inputmode="numeric" autocomplete="off" value="42,000"></span></label>
      <div class="mtd-out" data-mtd-out aria-live="polite"></div>
      <p><a class="u" href="contact.html?service=mtd">{r(L('Get help setting up MTD', '協助設定 MTD'), lang)} →</a></p>
    </form>
  </div>
</section>

<section class="section" id="rates" aria-labelledby="rates-h">
  <div class="wrap">
    <p class="label reveal-up">{r(t['rates_label'], lang)}</p>
    <h2 class="h2 split" id="rates-h">{lines(r(t['rates_title'], lang))}</h2>
    <p class="muted reveal-up">{r(t['rates_p'], lang)}</p>
    <div class="rates-wrap reveal-up">
      <table class="rates">
        <thead><tr><th scope="col">{r(t['col_item'], lang)}</th><th scope="col">2026/27</th><th scope="col">2025/26</th></tr></thead>{rates}
      </table>
    </div>
    <p class="fine"><a class="u" href="{GOV_RATES}" target="_blank" rel="noopener">{r(t['source'], lang)} ↗</a></p>
    <div class="coming reveal-up">
      <h3 class="h3">{r(t['coming'], lang)}</h3>
      <ul>{coming}</ul>
    </div>
  </div>
</section>

{deadlines_section(lang)}

<section class="section" id="start" aria-labelledby="start-h">
  <div class="wrap split-grid">
    <div class="sticky-col">
      <p class="label reveal-up">{r(t['start_label'], lang)}</p>
      <h2 class="h2 split" id="start-h">{lines(r(t['start_title'], lang))}</h2>
      <p class="reveal-up">{arrow_btn('contact.html?service=company', r(t['start_cta'], lang))}</p>
      <p class="reveal-up"><a class="u" href="https://www.gov.uk/set-up-business" target="_blank" rel="noopener">{r(t['dl_more'], lang)} ↗</a></p>
    </div>
    <ol class="steps" data-progress>{steps}
    </ol>
  </div>
</section>"""
    title = L("Tax rates 2026/27, MTD checker &amp; tax estimator | William Lai &amp; Co",
              "2026/27 稅率、數碼報稅檢查及入息稅估算 | William Lai &amp; Co")
    desc = L("UK income tax, dividend, National Insurance and Corporation Tax rates for 2026/27, a quick income tax estimator, a Making Tax Digital checker and a start-up checklist.",
             "英國 2026/27 年度入息稅、股息稅、國民保險及公司稅稅率，附入息稅估算、數碼報稅檢查及創業清單。")
    return page(lang, "guides.html", r(title, lang), r(desc, lang), body, "guides")


# ------------------------------------------------------------------ about
def about(lang):
    t = {
        "eyebrow": L("About", "關於我們"),
        "title": L("One accountant,|two professions,|three languages", "一位會計師|兩地資格|三種語言"),
        "lead": L("William Lai &amp; Co was founded in Sheffield in 2007 by William Lai, who has worked in accountancy for over 36 years.",
                  "William Lai &amp; Co 於 2007 年由 William Lai 在錫菲創立，他從事會計工作已逾 36 年。"),
        "p1": L("Before setting up the practice, William worked for a large PLC and in the property investment and construction industry. That background still shapes the firm: many clients are landlords, developers and builders, and complicated tax problems are dealt with promptly and in plain language.",
                "創立本所前，William 曾任職大型上市公司，並於物業投資及建築業工作。這些經驗至今仍是本所的特色：不少客戶是業主、發展商及建築商，複雜的稅務問題都能及時處理，並以淺白語言解釋。"),
        "p2": L("He reads and writes Chinese and English, speaks fluent Cantonese and English and good Putonghua, so Chinese-speaking clients can talk through their affairs without a language barrier.",
                "William 能讀寫中英文，說流利廣東話及英語，亦能以普通話溝通，華語客戶可以毫無語言障礙地商討自己的財務事宜。"),
        "cred_label": L("Qualifications", "專業資格"),
        "cred_title": L("Regulated and|accountable", "受專業團體|監管"),
        "aia": L("Association of International Accountants (AIA)", "英國國際會計師公會（AIA）"),
        "aia_p": L("Member in the UK. William practises under an AIA practising certificate, which means continuing professional development, professional indemnity insurance and AIA’s code of ethics.",
                   "英國會員。William 持 AIA 執業證書執業，須持續進修、購買專業彌償保險並遵守 AIA 專業操守守則。"),
        "hk": L("Hong Kong Institute of Certified Public Accountants (HKICPA)", "香港會計師公會（HKICPA）"),
        "hk_p": L("Member in Hong Kong, useful for clients with business or family links between the UK and Hong Kong.",
                  "香港會員，對在英港兩地有生意或家庭聯繫的客戶尤其有幫助。"),
        "facts": [
            (str(FOUNDED), L("Practice founded in Sheffield", "於錫菲創立")),
            ("36+", L("Years in accountancy", "年會計經驗")),
            ("3", L("Languages: English, Cantonese, Putonghua", "種語言：英語、廣東話、普通話")),
        ],
        "how_label": L("How we work", "工作方式"),
        "how": [
            (L("A free first conversation", "免費初步諮詢"), L("By phone or in person. Tell us what you need and we’ll tell you honestly whether we can help.", "以電話或面談了解閣下需要，並坦誠告知我們能否協助。")),
            (L("A fixed quote in writing", "書面固定報價"), L("You’ll know the fee before we start, set out in a letter of engagement.", "開始前於委聘書列明收費。")),
            (L("Your records, collected simply", "簡便收集資料"), L("Email, post, cloud software or a box of receipts: whatever works for you.", "電郵、郵寄、雲端軟件或一盒收據，以閣下方便為準。")),
            (L("Filed early, explained clearly", "提早遞交，清楚解釋"), L("We aim to file well before the deadline and walk you through what you owe and why.", "我們爭取在截止日期前提早遞交，並解釋應繳稅款及原因。")),
        ],
    }
    facts = "".join(f'<div class="fact reveal-up"><p class="fact-n">{n}</p><p>{r(l, lang)}</p></div>' for n, l in t["facts"])
    how = "".join(f"""
      <li class="step reveal-up"><span class="step-n">{i}</span><div><h3>{r(h, lang)}</h3><p>{r(p, lang)}</p></div></li>"""
                  for i, (h, p) in enumerate(t["how"], 1))
    body = f"""{page_hero(r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<section class="section" aria-label="William Lai">
  <div class="wrap split-grid">
    <figure class="portrait reveal-up" aria-hidden="true"><span class="portrait-mono">WL</span><figcaption>William Lai<br><small>AIA · HKICPA</small></figcaption></figure>
    <div class="prose">
      <p class="lead reveal-up">{r(t['p1'], lang)}</p>
      <p class="reveal-up">{r(t['p2'], lang)}</p>
      <div class="facts">{facts}</div>
    </div>
  </div>
</section>
<section class="section section-ink" aria-labelledby="cred-h">
  <div class="wrap split-grid">
    <div><p class="label reveal-up">{r(t['cred_label'], lang)}</p>
    <h2 class="h2 split" id="cred-h">{lines(r(t['cred_title'], lang))}</h2></div>
    <div class="creds">
      <div class="cred reveal-up"><span class="cred-tag">AIA</span><h3>{r(t['aia'], lang)}</h3><p>{r(t['aia_p'], lang)}</p></div>
      <div class="cred reveal-up"><span class="cred-tag">HKICPA</span><h3>{r(t['hk'], lang)}</h3><p>{r(t['hk_p'], lang)}</p></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="how-h">
  <div class="wrap split-grid">
    <div class="sticky-col"><p class="label reveal-up">{r(t['how_label'], lang)}</p>
    <h2 class="h2 split" id="how-h">{lines(r(L('Straightforward,|start to finish', '由始至終|簡單直接'), lang))}</h2></div>
    <ol class="steps" data-progress>{how}
    </ol>
  </div>
</section>"""
    title = L("About William Lai | AIA &amp; HKICPA accountant in Sheffield", "關於 William Lai | 錫菲 AIA 及 HKICPA 會計師")
    desc = L("William Lai has worked in accountancy for over 36 years and founded his Sheffield practice in 2007. Member of the AIA and HKICPA; speaks English, Cantonese and Putonghua.",
             "William Lai 從事會計逾 36 年，2007 年於錫菲創立本所。AIA 及 HKICPA 會員，能說英語、廣東話及普通話。")
    return page(lang, "about.html", r(title, lang), r(desc, lang), body, "about")


# ------------------------------------------------------------------ contact
def contact(lang):
    t = {
        "eyebrow": L("Contact", "聯絡我們"),
        "title": L("Let’s talk about|your accounts", "與我們|談談你的帳目"),
        "lead": L("The first conversation is free. Call, email or send the form and William will get back to you, usually within one working day.",
                  "初步諮詢免費。歡迎致電、電郵或填寫表格，William 通常會於一個工作天內回覆。"),
        "phone": L("Phone", "電話"), "email": L("Email", "電郵"), "office": L("Office", "辦事處"),
        "appt": L("Meetings are by appointment, at the office or at your premises across Sheffield and South Yorkshire.",
                  "會面須預約，可於本所或閣下位於錫菲及南約克郡的公司進行。"),
        "form_h": L("Send an enquiry", "網上查詢"),
        "name": L("Your name", "姓名"), "em": L("Email", "電郵"), "ph": L("Phone (optional)", "電話（選填）"),
        "svc": L("What do you need help with?", "需要哪方面協助？"),
        "other": L("Something else", "其他"),
        "lang": L("Preferred language", "希望使用的語言"),
        "msg": L("Your message", "訊息內容"),
        "send": L("Open in my email app", "以電郵程式發送"),
        "note": L("This opens your email app with the message filled in, ready to send. Nothing is stored on this website.",
                  "按下後會開啟閣下的電郵程式並自動填好內容，確認後即可發送。本網站不會儲存任何資料。"),
        "err": L("Please fill in your name, a valid email address and a message.", "請填寫姓名、有效電郵地址及訊息內容。"),
    }
    opts = "".join(f'<option data-id="{sid}">{r(title, "en").replace("&amp;", "&")}</option>' if lang == "en"
                   else f'<option data-id="{sid}" value="{r(title, "en").replace("&amp;", "&")}">{r(title, lang)}</option>'
                   for sid, title, _, _ in SERVICES)
    opts += f'<option data-id="other" value="Other">{r(t["other"], lang)}</option>'
    langs = "".join(f'<option value="{v}">{lbl}</option>' for v, lbl in
                    [("English", "English"), ("Cantonese", "廣東話 Cantonese"), ("Putonghua", "普通話 Putonghua")])
    body = f"""{page_hero(r(t['eyebrow'], lang), r(t['title'], lang), r(t['lead'], lang))}
<section class="section section-tight">
  <div class="wrap contact-grid">
    <div class="contact-cards">
      <a class="c-card reveal-up" href="tel:{PHONE_TEL}">{ICON['phone']}<span class="mini">{r(t['phone'], lang)}</span><span class="c-big">{PHONE_DISPLAY}</span></a>
      <a class="c-card reveal-up" href="mailto:{EMAIL}">{ICON['mail']}<span class="mini">{r(t['email'], lang)}</span><span class="c-big c-email">{EMAIL}</span></a>
      <a class="c-card reveal-up" href="{MAPS_URL}" target="_blank" rel="noopener">{ICON['pin']}<span class="mini">{r(t['office'], lang)}</span><span class="c-big">{'<br>'.join(r(ADDRESS, lang))}</span></a>
      <p class="muted reveal-up">{r(t['appt'], lang)}</p>
    </div>
    <form class="form reveal-up" data-contact-form novalidate>
      <h2 class="h3">{r(t['form_h'], lang)}</h2>
      <label class="field"><span>{r(t['name'], lang)}</span><input name="name" autocomplete="name" required></label>
      <div class="two">
        <label class="field"><span>{r(t['em'], lang)}</span><input name="email" type="email" autocomplete="email" required></label>
        <label class="field"><span>{r(t['ph'], lang)}</span><input name="phone" type="tel" autocomplete="tel"></label>
      </div>
      <div class="two">
        <label class="field"><span>{r(t['svc'], lang)}</span><select name="service">{opts}</select></label>
        <label class="field"><span>{r(t['lang'], lang)}</span><select name="lang">{langs}</select></label>
      </div>
      <label class="field"><span>{r(t['msg'], lang)}</span><textarea name="message" rows="5" required></textarea></label>
      <p class="form-err" data-form-error hidden role="alert">{r(t['err'], lang)}</p>
      <button class="btn btn-accent" type="submit"><span>{r(t['send'], lang)}</span>{ICON['arrow']}</button>
      <p class="fine">{r(t['note'], lang)}</p>
    </form>
  </div>
</section>"""
    title = L("Contact | William Lai &amp; Co, accountants in Sheffield", "聯絡我們 | William Lai &amp; Co 錫菲會計師")
    desc = L("Call 07920 045128 or email wlai@accountanttax.co.uk. Free first conversation, in English, Cantonese or Putonghua.",
             "致電 07920 045128 或電郵 wlai@accountanttax.co.uk。免費初步諮詢，可用英語、廣東話或普通話。")
    return page(lang, "contact.html", r(title, lang), r(desc, lang), body, "contact")


# ------------------------------------------------------------------ legal
def legal(lang):
    if lang == "en":
        content = f"""
<h2>About us</h2>
<p>This website is run by William Lai, trading as William Lai &amp; Co International Accountants, 24 Darfield Avenue, Sheffield S20 6SU. William Lai is a member of the Association of International Accountants (AIA) and practises under an AIA practising certificate. He is also a member of the Hong Kong Institute of Certified Public Accountants (HKICPA). Professional indemnity insurance details are available on request.</p>
<h2>Privacy notice</h2>
<p>William Lai &amp; Co is the data controller for personal information you give us. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h3>What we collect and why</h3>
<ul>
<li><strong>Enquiries.</strong> Your name, contact details and message, so we can reply. Legal basis: legitimate interests.</li>
<li><strong>Client work.</strong> The financial and personal information needed to prepare accounts and tax returns. Legal basis: performing our contract with you, and legal obligations.</li>
<li><strong>Anti-money-laundering checks.</strong> Proof of identity and address, as the Money Laundering Regulations 2017 require. Legal basis: legal obligation.</li>
</ul>
<h3>Who we share it with</h3>
<p>HMRC, Companies House and other bodies when you ask us to file on your behalf, our professional body or insurers where required, and software providers who process data for us under contract. We never sell your information.</p>
<h3>How long we keep it</h3>
<p>Enquiries that don’t lead to work: up to 12 months. Client records: 6 years after the end of our engagement, or longer where the law requires.</p>
<h3>Your rights</h3>
<p>You can ask for a copy of your information, ask us to correct or delete it, or object to how we use it. If you’re unhappy with how we’ve handled your data, you can complain to the Information Commissioner’s Office at <a href="https://ico.org.uk/make-a-complaint/" target="_blank" rel="noopener">ico.org.uk</a>.</p>
<h3>This website</h3>
<p>This site sets no cookies and uses no tracking. The contact form doesn’t send anything to a server: it opens your own email app.</p>
<h2>Disclaimer</h2>
<p>The guides and calculators on this site are general information for the UK tax year shown, not advice for your circumstances. Please talk to us before acting on them.</p>"""
    else:
        content = f"""
<h2>關於我們</h2>
<p>本網站由 William Lai 營運，商號為 William Lai &amp; Co International Accountants，地址為 24 Darfield Avenue, Sheffield S20 6SU。William Lai 為英國國際會計師公會（AIA）會員，持 AIA 執業證書執業，亦為香港會計師公會（HKICPA）會員。專業彌償保險資料可按要求提供。</p>
<h2>私隱政策</h2>
<p>William Lai &amp; Co 為閣下提供之個人資料的資料控制者。聯絡電郵：<a href="mailto:{EMAIL}">{EMAIL}</a>。</p>
<h3>收集的資料及用途</h3>
<ul>
<li><strong>查詢：</strong>姓名、聯絡方法及訊息內容，以便回覆。法律依據：正當利益。</li>
<li><strong>客戶工作：</strong>編製帳目及報稅所需的財務及個人資料。法律依據：履行與閣下的合約及法律責任。</li>
<li><strong>反洗錢檢查：</strong>按《2017 年反洗錢條例》要求核實身份及地址。法律依據：法律責任。</li>
</ul>
<h3>與誰分享</h3>
<p>按閣下要求代為申報時提交予 HMRC、Companies House 等機構；如有需要提供予本所專業團體或保險公司；以及按合約代我們處理資料的軟件供應商。我們絕不出售閣下的資料。</p>
<h3>保存期限</h3>
<p>未有委託的查詢：最長 12 個月。客戶紀錄：委聘結束後 6 年，或按法律要求更長時間。</p>
<h3>閣下的權利</h3>
<p>閣下可要求索取個人資料副本、更正或刪除資料，或反對我們使用資料。如對處理方式不滿，可向資訊專員辦公室（ICO）投訴：<a href="https://ico.org.uk/make-a-complaint/" target="_blank" rel="noopener">ico.org.uk</a>。</p>
<h3>本網站</h3>
<p>本網站不使用 cookies，亦不作任何追蹤。聯絡表格不會傳送資料至伺服器，只會開啟閣下的電郵程式。</p>
<h2>免責聲明</h2>
<p>本網站的指南及計算工具僅提供所示英國稅務年度的一般資料，並非針對個別情況的專業意見。採取行動前請先與我們商討。</p>"""
    t = L("Privacy &amp; legal", "私隱政策及法律聲明")
    body = f"""{page_hero(r(L('Legal', '法律'), lang), r(t, lang), r(L('Who we are, how we handle your information, and the small print.', '我們是誰、如何處理閣下資料，以及其他細則。'), lang))}
<section class="section section-tight"><div class="wrap prose legal">{content}
<p class="fine">{r(L('Last updated: November 2026', '最後更新：2026 年 11 月'), lang)}</p></div></section>"""
    return page(lang, "legal.html", r(t, lang) + " | William Lai &amp; Co",
                r(L("Privacy notice, professional body details and disclaimer for William Lai &amp; Co, Sheffield.",
                    "William Lai &amp; Co 私隱政策、專業團體資料及免責聲明。"), lang), body, "legal")


if __name__ == "__main__":
    for lang, meta in LANGS.items():
        for name, fn in [("index.html", home), ("services.html", services), ("guides.html", guides),
                         ("about.html", about), ("contact.html", contact), ("legal.html", legal)]:
            path = os.path.join(ROOT, meta["dir"], name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))
