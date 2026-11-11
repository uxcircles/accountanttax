"""Self-hosted web fonts. Run after editing Chinese text (no dependencies):

    python3 _build/fonts.py && python3 _build/pages.py

- Newsreader (roman + italic, opsz and weight 400–600 axes) and Hanken Grotesk: Google's Latin subset
- Noto Serif TC 600: only the Chinese characters used on the site (Google Fonts `text=` subsetting)
"""
import glob
import html
import os
import re
import urllib.parse
import urllib.request

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
OUT = os.path.join(ROOT, "assets", "fonts")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
API = "https://fonts.googleapis.com/css2?"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def latin_src(css, italic=False):
    """Pick the woff2 URL of the `latin` block (optionally the italic one) from a css2 response."""
    for comment, block in re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", css, re.S):
        if comment == "latin" and (("font-style: italic" in block) == italic):
            return re.search(r"url\((.*?)\)", block).group(1)
    raise SystemExit("latin block not found")


def save(name, data):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name + ".woff2")
    with open(path, "wb") as f:
        f.write(data)
    print(f"{name}.woff2  {len(data) // 1024} KB")


def site_cjk():
    chars = set("0123456789年月日天還有今明距離月")  # what main.js writes at runtime
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S)
        text = html.unescape(re.sub(r"<[^>]+>", " ", text))
        chars.update(ch for ch in text if ord(ch) > 0x2E7F)
    return "".join(sorted(chars))


if __name__ == "__main__":
    css = get(API + "family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400..600&display=swap").decode()
    save("newsreader", get(latin_src(css)))
    save("newsreader-italic", get(latin_src(css, italic=True)))
    css = get(API + "family=Hanken+Grotesk:wght@400..700&display=swap").decode()
    save("hanken-grotesk", get(latin_src(css)))
    text = site_cjk()
    css = get(API + "family=Noto+Serif+TC:wght@600&display=swap&text=" + urllib.parse.quote(text)).decode()
    save("noto-serif-tc-600", get(re.search(r"url\((.*?)\)", css).group(1)))
    print(len(text), "Chinese characters")
