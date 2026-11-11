# William Lai & Co International Accountants: website redesign

A concept redesign of [accountanttax.co.uk](https://accountanttax.co.uk/) for William Lai & Co, a Sheffield accountancy practice founded in 2007 by William Lai (AIA, HKICPA). Plain HTML, CSS and JavaScript: host the repository root on any static host (GitHub Pages, Netlify, Cloudflare Pages, Vercel).

## Languages

| Path   | Language                       |
|--------|--------------------------------|
| `/`    | English                        |
| `/zh/` | 繁體中文 (Traditional Chinese) |

Every page exists in both languages, with `hreflang` links and a language switch in the header, menu and footer.

**Pages:** Home · Services · Tax guides · About · Contact · Privacy & legal

## Run locally

```bash
python3 -m http.server 5200
```

Then open http://localhost:5200.

## Editing

The HTML is generated, so the header, footer and contact details stay the same across all 12 pages:

- Contact details, header, footer, UI strings: `_build/layout.py`
- Services, client types, tax rates, start-up checklist (both languages side by side, via `L(english, 中文)`): `_build/content.py`
- Page layouts and headlines: `_build/pages.py`. A `|` in a headline marks a line break for the reveal animation.

Rebuild after editing (Python 3, no dependencies):

```bash
python3 _build/pages.py
```

Fonts are self-hosted in `assets/fonts/`: Newsreader (headings), Hanken Grotesk (body) and Noto Serif TC (Chinese headings, subset to the characters used). **After changing Chinese text, run** `python3 _build/fonts.py && python3 _build/pages.py`.

**Each April**, update `RATES` and `COMING` in `_build/content.py`, the ledger card on the home page and the estimator thresholds in `assets/js/main.js`.

## What this fixes on the current site

Reviewed on accountanttax.co.uk in November 2026:

- **Not mobile-friendly.** It runs the 2010 WordPress "Twenty Ten" theme at a fixed 940px width with no viewport tag, so phones show a shrunken desktop page. The header image is an unrelated beach photo.
- **Wrong Making Tax Digital advice.** The News page says MTD applies to people with income "up to £50,000" from April 2026. It is the reverse: it applies to qualifying income **over** £50,000 (then over £30,000 in 2027 and over £20,000 in 2028). It also calls the quarterly updates "quarterly tax returns".
- **Out-of-date tax rates.** The rates page is for 2025/26. In 2026/27 the dividend ordinary and upper rates rose to 10.75% and 35.75%, and Business Asset Disposal Relief rose to 18%.
- **The rates page contradicts itself.** The Dividend Allowance for 2024/25 is shown as £1,000 in one table and £500 in another (it was £500).
- **Dead links and stale examples.** The Business Start Up page links to Business Link (closed in 2012) and an old `hmrc.gov.uk` URL, and its example uses the 2011/12 tax year.
- **Confusing navigation.** The "Blog" link opens "Business Start Up", and "Services" lives at `/accountants-sheffield/`.
- **Typos:** "indiviauals", "requied", "Income taxe", "amnount".
- **No tel: link**, the phone number is written as "0792 004 5128", and the Facebook link uses an old `#!` URL format.
- **No privacy notice**, keyword-stuffed page titles, and the AIA logo has no alt text.

## What the redesign adds

**Design.** A WL monogram in a ledger box, with a double rule underneath (the way an accountant rules off a total). The palette is slate ink, warm paper and a forged-copper accent, a nod to Sheffield's steel. There are no stock photos.

**Motion** is restrained (headlines slide up line by line, numbers count up, a copper progress line runs down the step lists) and switches off for visitors who ask for reduced motion.

**Useful features:**

- **Ledger card** on the home page: 2026/27 Personal Allowance, VAT threshold, MTD threshold, the next HMRC deadline and years in practice (worked out from today's date)
- **Income tax estimator** for 2026/27 (employed or self-employed, England/Wales/NI), with National Insurance, take-home pay and the Personal Allowance taper over £100,000
- **"Do I need MTD?" checker**: enter turnover plus rental income to see when Making Tax Digital applies, with the next quarterly date
- **Tax rates 2026/27** next to 2025/26, with changes highlighted, plus changes already announced for 2027
- **HMRC deadline countdown** (Self Assessment and MTD quarterly updates)
- **Start-up checklist**, rewritten and updated (council food registration, HMRC registration deadlines, VAT and PAYE)
- Fixed **Call / Email / Map** bar on phones
- **Contact form** that opens the visitor's email app with the enquiry filled in, including their preferred language (English, Cantonese or Putonghua). "Ask about this" links pre-select the service.
- `AccountingService` structured data and a title and description for each page in both languages
- A plain-English **UK GDPR privacy notice** and professional body disclosure

## For the firm to check before launch

- **Free first conversation and fixed quotes.** The site offers both. Please confirm, or the wording can change.
- **CIS, payroll pensions and P11Ds** are listed under services because of the construction and property focus. The current site doesn't mention them explicitly, so please confirm.
- **Client types** (landlords, builders, shops and takeaways, Chinese-speaking clients) are inferred from the current About page.
- **"Over 36 years"** is copied from the current site. If that was written some years ago, please update it.
- **Business audit** is mentioned on the current site but left out here, because audit work needs registered auditor status. Add it back if that applies.
- **Address.** 24 Darfield Avenue is shown, with meetings "by appointment". Remove it if you'd rather not publish it.
- **Privacy notice** is a draft. Please have it reviewed, especially the retention periods.
- **Tax figures** are for 2026/27 (England, Wales and NI). Please check them against GOV.UK before launch.
- **Redirects:** `/accountants-sheffield/` → `/services.html`, `/news/`, `/blog/` and `/budget-2025-26-tax-rates-and-allowances/` → `/guides.html`, `/contact-us/` → `/contact.html`.
