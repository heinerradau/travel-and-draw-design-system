import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
LOGO = "https://cdn.klaviyomail.com/company/VFrCC2/images/aa1d7b55-271e-4a94-be1a-ca608a505e1e.png"
NYC = "https://cdn.klaviyomail.com/company/VFrCC2/images/eb5d57c4-e901-46cb-ab5d-7c65942cbfca.png"
BERLIN = "https://cdn.klaviyomail.com/company/VFrCC2/images/b1db7b51-06a1-40e5-8a4d-528362a64303.png"
AMS = "https://cdn.klaviyomail.com/company/VFrCC2/images/cbd89333-c33b-4001-b7bd-94489d4419b6.jpeg"
ARTIST = "https://cdn.klaviyomail.com/company/VFrCC2/images/58335834-f6b8-4ef0-b6fa-f84c4f796c84.jpeg"
SHOP = "https://heinerradau.de"
P, P2, INK, INK2, SOFT, RED, LINE = "#F2EBDD", "#EDE4D1", "#15120E", "#3A332A", "#6B6256", "#C8102E", "#D8CDB6"
DISP = "'Bebas Neue',Impact,'Arial Narrow Bold',sans-serif"
COND = "'Barlow Condensed','Arial Narrow',Arial,sans-serif"
BODY = "Barlow,Arial,Helvetica,sans-serif"
STORY = "Georgia,'Times New Roman',serif"

def wrap(preheader, inner):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;500&family=Barlow+Condensed:wght@600&display=swap" rel="stylesheet">
<style>body{{margin:0;padding:0;background:{P};}} a{{color:{RED};}} img{{border:0;display:block;max-width:100%;height:auto;}}
@media (max-width:620px){{.px{{padding-left:20px!important;padding-right:20px!important}} .h1{{font-size:44px!important}} .col{{display:block!important;width:100%!important}}}}</style></head>
<body style="margin:0;padding:0;background:{P};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preheader}&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{P};"><tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:{P};">
<tr><td class="px" style="padding:8px 40px 20px;border-bottom:1px solid {LINE};" align="left"><a href="{SHOP}"><img src="{LOGO}" width="150" alt="heiner radau – Travel &amp; Draw" style="width:150px;"></a></td></tr>
{inner}
<tr><td class="px" style="padding:28px 40px 8px;border-top:1px solid {LINE};font:400 13px/1.6 {BODY};color:{SOFT};" align="left">
<p style="margin:0 0 6px;font:600 12px/1.4 {COND};letter-spacing:.14em;text-transform:uppercase;color:{INK};">Travel &amp; Draw — Heiner Radau</p>
<p style="margin:0 0 6px;">Hand-drawn cities, drawn on location in Berlin and around the world.</p>
<p style="margin:0;"><a href="{SHOP}" style="color:{SOFT};">heinerradau.de</a> &nbsp;·&nbsp; {{% unsubscribe 'Unsubscribe' %}}</p>
<p style="margin:10px 0 0;font-size:12px;">{{{{ organization.name }}}} · {{{{ organization.full_address }}}}</p>
</td></tr></table></td></tr></table></body></html>"""

def eyebrow(t): return f'<p style="margin:0 0 10px;font:600 12px/1.4 {COND};letter-spacing:.14em;text-transform:uppercase;color:{RED};">{t}</p>'
def h1(t): return f'<h1 class="h1" style="margin:0 0 16px;font:400 54px/.92 {DISP};letter-spacing:.01em;text-transform:uppercase;color:{INK};">{t}</h1>'
def h2(t): return f'<h2 style="margin:0 0 12px;font:400 34px/.95 {DISP};text-transform:uppercase;color:{INK};">{t}</h2>'
def p(t, story=False):
    f = f"400 18px/1.6 {STORY}" if story else f"400 17px/1.6 {BODY}"
    return f'<p style="margin:0 0 16px;font:{f};color:{INK2};">{t}</p>'
def btn(label, url):
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" style="margin:8px 0 8px;"><tr><td style="background:{RED};border-radius:2px;">
<a href="{url}" style="display:inline-block;padding:16px 30px;font:600 15px/1 {COND};letter-spacing:.12em;text-transform:uppercase;color:#ffffff;text-decoration:none;">{label}</a></td></tr></table>'''
def sec(inner, pad="32px 40px 8px", bg=None):
    b = f"background:{bg};" if bg else ""
    return f'<tr><td class="px" style="padding:{pad};{b}" align="left">{inner}</td></tr>'
def img(src, alt, href=SHOP):
    return f'<tr><td style="padding:8px 40px 8px;" class="px"><a href="{href}"><img src="{src}" width="520" alt="{alt}" style="width:100%;border-radius:2px;"></a></td></tr>'
def code_box(code, line):
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 18px;border:2px dashed {INK};"><tr><td align="center" style="padding:18px 12px;background:{P2};">
<p style="margin:0 0 4px;font:600 12px/1.4 {COND};letter-spacing:.14em;text-transform:uppercase;color:{SOFT};">{line}</p>
<p style="margin:0;font:400 44px/1 {DISP};letter-spacing:.06em;color:{INK};">{code}</p></td></tr></table>'''
def trust():
    items = [("Hand-drawn original", "Dip pen and ink, line by line."), ("Made on location", "Drawn live on the street."),
             ("Giclée on canvas", "Fade-resistant, ready to hang."), ("Free shipping", "Germany from €50 · EU from €100 · worldwide from €150.")]
    cells = "".join(f'<tr><td style="padding:10px 0;border-top:1px solid {LINE};"><p style="margin:0;font:400 22px/1 {DISP};text-transform:uppercase;color:{INK};">{a}</p><p style="margin:4px 0 0;font:400 15px/1.5 {BODY};color:{SOFT};">{b}</p></td></tr>' for a, b in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 8px;">{cells}</table>'
CART = f'''{{% if event.extra.line_items %}}<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:6px 0 14px;">
{{% for item in event.extra.line_items %}}<tr><td width="110" valign="top" style="padding:12px 16px 12px 0;border-top:1px solid {LINE};"><img src="{{{{ item.product.images.0.src }}}}" width="96" alt="{{{{ item.product.title }}}}" style="width:96px;border-radius:2px;"></td>
<td valign="top" style="padding:12px 0;border-top:1px solid {LINE};"><p style="margin:0 0 4px;font:400 22px/1 {DISP};text-transform:uppercase;color:{INK};">{{{{ item.product.title }}}}</p>
<p style="margin:0;font:400 15px/1.5 {BODY};color:{SOFT};">{{% if item.variant.title and item.variant.title != 'Default Title' %}}{{{{ item.variant.title }}}} · {{% endif %}}Qty {{{{ item.quantity|floatformat:0 }}}} · {{% currency_format item.line_price|floatformat:2 %}}</p></td></tr>{{% endfor %}}
</table>{{% endif %}}'''
CHECKOUT = "{{ event.extra.checkout_url|default:'https://heinerradau.de/cart' }}"
CANVAS = f"{SHOP}/collections/city-art-canvas-prints-new"

mails = {}
mails["welcome-0-existing"] = ("THANKS FOR SUBSCRIBING", "You're in – first look at every new city.", wrap("You're in – first look at every new city.",
  sec(eyebrow("Welcome back") + h1("You're in.") + p("Hey {{ first_name|title|default:'there' }}, thanks for joining – and for already having one of my drawings at home.") +
      p("From now on you'll see every new city first: where I'm drawing, how the sheet grows day by day, and when a new canvas is ready.") +
      btn("See the latest cities", CANVAS)) + img(NYC, "New York City canvas by Heiner Radau", CANVAS) +
  sec(p("Every line is a memory.<br>Every place has a story.", story=True) + p("— Heiner"), pad="16px 40px 24px")))

mails["welcome-1"] = ("Welcome – here's 5% for your first piece", "Cities, drawn by hand on location. Your code: ARTLOVE5", wrap("Cities, drawn by hand on location. Your code: ARTLOVE5",
  sec(eyebrow("Welcome to Travel &amp; Draw") + h1("Cities.<br>By hand.<br>Drawn on location.") +
      p("Hey {{ first_name|title|default:'there' }}, I'm glad you're here.") +
      p("Every line is drawn live on the street — with dip pen and ink, no photo reference, no eraser. Weeks on a single sheet. No stock design, real art for your wall.") +
      p("As a little thank-you for joining:") + code_box("ARTLOVE5", "5% off your first order") + btn("Find your city", CANVAS)) +
  img(NYC, "New York City – hand-drawn cityscape as a canvas", CANVAS) +
  sec(trust(), pad="16px 40px 24px")))

mails["welcome-2"] = ("One city. One sheet. One month.", "How my drawings are made – not in a studio, on the street.", wrap("How my drawings are made – not in a studio, on the street.",
  sec(eyebrow("How the drawings are made") + h1("Not in a studio.<br>On the street.")) +
  img(AMS, "Heiner Radau drawing on the streets of Amsterdam", f"{SHOP}/pages/about-1") +
  sec(p("For about 30 days I draw the busy scenes of a city with pen and ink, right on the street. The daily, diary-like drawings grow together on the sheet and store time and stories – a dense web of black and white lines, full of life.", story=True) +
      p("Line by line in ink — with no way to erase anything. In wind, rain and among curious passers-by.") +
      p("I started out as a Berlin graffiti artist, became known as the “subway pop-up artist” on the U-Bahn, and later exhibited at Galerie Hilt in Basel. The street is still in every line.") +
      btn("Read my story", f"{SHOP}/pages/about-1"), pad="16px 40px 24px")))

mails["welcome-3"] = ("Explore Berlin the way I drew it", "62 places, 4 tours – the Berlin Art Map.", wrap("62 places, 4 tours – the Berlin Art Map.",
  sec(eyebrow("Berlin Art Map") + h1("Walk Berlin<br>through the drawing.") +
      p("My Berlin drawing is full of places with a story. In the Berlin Art Map you can tap on 62 of them and follow four tours through the city – right on the artwork or on the street map.") +
      btn("Open the Berlin Art Map", f"{SHOP}/pages/berlin-art-map?view=bam-app")) +
  img(BERLIN, "Berlin canvas by Heiner Radau", f"{SHOP}/products/berlin-new") +
  sec(p("Want Berlin on your wall? The canvas comes ready to hang, with free shipping in Germany.") + btn("See the Berlin canvas", f"{SHOP}/products/berlin-new"), pad="16px 40px 24px")))

mails["welcome-4"] = ("Your 5% is still waiting", "ARTLOVE5 – for your first hand-drawn city.", wrap("ARTLOVE5 – for your first hand-drawn city.",
  sec(eyebrow("A small reminder") + h1("Bring a city<br>to your wall.") +
      p("Hey {{ first_name|title|default:'there' }}, your welcome code is still valid for your first order:") +
      code_box("ARTLOVE5", "5% off your first order") + btn("Choose your city", CANVAS) + trust() +
      p("No risk: if you don't love it, send it back."), pad="32px 40px 24px")))

mails["cart-1"] = ("Your city is still waiting", "You left something in your cart.", wrap("You left something in your cart.",
  sec(eyebrow("Still thinking about it?") + h1("Your city<br>is still waiting.") +
      p("Hey {{ first_name|title|default:'there' }}, you left this in your cart:") + CART + btn("Back to my cart", CHECKOUT) +
      p("Questions about size or framing? Just reply to this email.", ) + p("— Heiner"), pad="32px 40px 24px")))

mails["cart-2"] = ("Why every line takes weeks", "Hand-drawn on location, printed to last.", wrap("Hand-drawn on location, printed to last.",
  sec(eyebrow("What you get") + h1("Weeks on<br>one sheet.")) +
  img(ARTIST, "Heiner Radau at work", CHECKOUT) +
  sec(p("Every drawing is made live on the street — dip pen and ink, no photo reference, no eraser.", story=True) +
      p("The canvas: 344 g/m² poly-cotton, printed on all sides for a 3-D gallery effect, on a 3.1 cm wooden stretcher – fade-resistant and ready to hang. Optional floater frame.") +
      p("Canvases are produced for you and arrive in 6–12 working days. Shipping is free in Germany from €50, in the EU from €100 and worldwide from €150.") +
      CART + btn("Complete my order", CHECKOUT), pad="16px 40px 24px")))

mails["cart-3"] = ("10% off your city – a last nudge", "Use ENJOY10 on the piece in your cart.", wrap("Use ENJOY10 on the piece in your cart.",
  sec(eyebrow("A last nudge") + h1("10% off<br>your city.") +
      p("Hey {{ first_name|title|default:'there' }}, I'd hate for you to miss out on the piece in your cart. To make the decision a little easier:") +
      code_box("ENJOY10", "10% off your order") + CART + btn("Use my 10%", CHECKOUT) +
      p("No risk: if you don't love it, send it back."), pad="32px 40px 24px")))

for k, (subj, pre, html) in mails.items():
    open(os.path.join(OUT, k + ".html"), "w").write(html)
json.dump({k: {"subject": s, "preview": pr} for k, (s, pr, _) in mails.items()}, open(os.path.join(OUT, "meta.json"), "w"), indent=1)
print(list(mails))
