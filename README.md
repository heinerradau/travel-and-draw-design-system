# heiner radau · Travel & Draw — Visuelle Identität v2

**Stand:** 23.10.2026 · **Gilt für:** heinerradau.de (Shopify-Theme `heinerradau-theme`, Branch `relaunch`, live seit 23.10.2026), Checkout, Klaviyo-Mails, Landingpages, Print.
**Vorgänger:** v1 (05/2026, Impact-Theme, weiß/navy) liegt unter [`legacy/v1/`](legacy/v1/) – nicht mehr verwenden.

Übersicht zum Anschauen: [`index.html`](index.html) (alle Logos, Farben, Schriften, Bausteine auf einer Seite).

---

## 1. Marke in einem Satz

**heiner radau** ist der Künstler, **Travel & Draw** ist seine Arbeitsweise: Städte, live auf der Straße gezeichnet – mit Feder und Tinte, ohne Fotovorlage, ohne Radiergummi, wochenlang auf einem Blatt.

- Absender/Name: **heiner radau** (im Logo immer klein geschrieben)
- Linie/Untertitel: **Travel & Draw** (steht immer klein unter dem Schriftzug)
- Domain: heinerradau.de · Instagram: @heinerradau · B2B: studio@heinerradau.de
- Haltung: echt, handgemacht, urban, Street-Art-Wurzeln mit Uhrmacher-Präzision. Laut im Ausdruck, ruhig im Rahmen – das Kunstwerk trägt das Bild.

## 2. Logos

Alle Logos sind Vektoren (SVG) und liegen zusätzlich als PNG in 600/1200/2400 px bei. Quelle: Heiners Affinity-Dateien in [`logos/source/`](logos/source/) (nachgezeichnet aus deren Vorschaubild, weiße Außenkontur entfernt).

| Logo | Datei | Wofür |
|---|---|---|
| **Wortbildmarke** – Globus links, „heiner radau“ rechts | `logos/wordmark/heiner-radau-wordmark-{ink,black,paper,white,red}.svg` | Hauptlogo: Website-Header, Footer, Checkout, Mail-Kopf, Katalog-Cover |
| **Lockup** – Wortbildmarke + „TRAVEL & DRAW“ | `logos/lockup/heiner-radau-travel-and-draw-lockup-{ink,ink-solid,paper,white,black}.svg` | Überall, wo die Marke vollständig stehen soll: Header/Footer (so umgesetzt), Print, Präsentationen, Briefpapier |
| **Siegel** – Name im Globus | `logos/badge/heiner-radau-badge-color.svg` (weißer Globus), `-on-paper.svg` (Globus papierfarben), `-mono-{ink,black,paper,white,red}.svg` (einfarbig, Globus ausgestanzt) | Kleine/quadratische Flächen und „Stempel“ (siehe 2.2) |
| **Favicon/App-Icon** | `logos/favicon/favicon-badge.svg` + PNG 32/180/512 | Browser-Tab, Apple-Touch-Icon, Art-Map-App |

### 2.1 Regeln Wortbildmarke + Travel & Draw
- **„Travel & Draw“ steht unter dem Wortteil**, nicht unter dem Globus: Die Zeile beginnt genau dort, wo „heiner radau“ beginnt (**37,25 % der Logobreite**), und endet bündig rechts mit dem Schriftzug. Die Buchstaben werden auf diese Breite verteilt.
- Schrift: Barlow Condensed 600, Versalien. Auf Papier in Tinte-weich `#6B6256`, auf Dunkel in `#CABFAE`. Für Print in einer Farbe: `ink-solid`.
- Größe: Versalhöhe ≈ 12 % der Logohöhe, Abstand zum Logo ≈ 10 % der Logohöhe.
- Mindestbreite Wortbildmarke: 120 px digital / 30 mm Print. Darunter: Siegel nehmen.
- Schutzraum rundum: mindestens die Höhe des „h“.
- Keine weiße Kontur, keine Schatten, nicht verzerren, nicht drehen, nicht auf unruhigen Bildstellen platzieren.
- Farben: Tinte auf Papier (Standard), Papier auf Tinte (Footer, dunkle Bänder). Rot nur als Sonderfall (Sticker, Kampagne), nie auf Rot.
- In Liquid fertig: [`shopify/tnd-logo-mark.liquid`](shopify/tnd-logo-mark.liquid) (SVG mit `currentColor`) + [`shopify/tnd-logo-sub.liquid`](shopify/tnd-logo-sub.liquid) (verteilte Unterzeile).

### 2.2 Wo das Siegel (Name im Globus) hinpasst
Das Siegel ist quadratisch und trägt den Namen selbst – ideal dort, wo wenig Platz ist oder etwas „abgestempelt“ wirken soll. **Nicht** zusammen mit der Wortbildmarke auf derselben Fläche.

1. **Favicon / App-Icon** (Browser-Tab, Startbildschirm, Berlin-Art-Map-App) – Wortbildmarke ist dort zu breit.
2. **Profilbilder** auf Instagram, TikTok, YouTube, Facebook, Klaviyo-Absenderbild, Google-Unternehmensprofil.
3. **Echtheits-Stempel**: Rückseite der Leinwand, Echtheitszertifikat, Versandkarton-Sticker, Hang-Tags an Merch, Etikett im T-Shirt.
4. **„Original by heiner radau“-Siegel** auf der Produktseite (neben „Hand-drawn original“) und auf der „Über Heiner“-Seite beim Porträt.
5. **Mail-Fuß** (klein, Mono-Papier auf Tinte oder Mono-Tinte auf Papier) und E-Mail-Signatur.
6. **POS/B2B**: QR-Aufsteller, Regal-Wobbler, Katalog-Rückseite.

## 3. Farben

| Token | Hex | Einsatz |
|---|---|---|
| `--tnd-paper` | `#F2EBDD` | Seitenhintergrund (Papier) |
| `--tnd-paper-2` | `#F6F0E4` | Karten, Bildflächen (Papier hell) |
| `--tnd-paper-3` | `#EDE4D1` | Bänder, Bestellübersicht im Checkout (Checkout: `#EDE4D3`) |
| `--tnd-hair` | `#D8CDB6` | Haarlinien, Rahmen |
| `--tnd-ink` | `#15120E` | Text, Logo, dunkle Flächen (Tinte) |
| `--tnd-ink-2` | `#3A332A` | Fließtext |
| `--tnd-ink-soft` | `#6B6256` | Nebentexte, Unterzeile „Travel & Draw“ |
| `--tnd-muted` | `#CABFAE` | Text auf Dunkel |
| `--tnd-red` | `#C8102E` | Akzent, Buttons, Eyebrows, Links (Hover `#A50D25`) |
| `--tnd-rose` | `#E9A6AE` | Akzent auf Dunkel |
| `--tnd-star` | `#D4A017` | Bewertungs-Sterne |
| Art-Map-Touren | `#1E5BC6` `#F2C230` `#1F8A4C` `#7B3FB5` | nur in der Berlin Art Map |

Kein Weiß als Seitenhintergrund. Weiß nur in Formularfeldern und im Siegel-Globus.

## 4. Schrift

| Rolle | Schrift | Regeln |
|---|---|---|
| Display / Überschriften | **Bebas Neue** 400 | Versal, Zeilenhöhe 0,9. **Überall, wo es punchy, wichtig, produktbezogen und modern ist.** |
| Eyebrow, Buttons, Labels, Navigation | **Barlow Condensed** 600 | Versal, Laufweite .08–.14em; Eyebrow 12 px in Rot |
| Fließtext | **Barlow** 400/500 | 16–17 px, Zeilenhöhe 1,6 |
| Story | **Georgia** | **Story, Geschichte, Emotion**: Entstehungstext, Zitat, Bewertungen (`--tnd-font-story`) |

Google Fonts: `Bebas+Neue`, `Barlow:wght@400;500`, `Barlow+Condensed:wght@600`. In Mails fallen Webfonts oft weg → Fallbacks `Impact` / `Arial Narrow` / `Arial` / `Georgia` sind eingeplant.

## 5. Layout & Formen
- Inhaltsbreite max. 1180–1240 px, Rand `clamp(16px,4vw,56px)`, Sektionsabstand `clamp(48px,7vw,96px)`.
- Ecken **2 px** (eckig). Pillen-Form nur für Filter und Touren.
- Hero zweispaltig ab 900 px. Kunstwerk mit leichtem Schlagschatten.
- Buttons: Rot (Hauptaktion), Tinte, Linie. Mindesthöhe 48 px.

## 6. Bilder
- **Kunstwerke immer quadratisch.** Weißer Rand um den Rahmen mit einem normalen Rechteck weggeschnitten (kein Zauberstab).
- Keine weißen Hintergründe in Produktbildern – Freisteller/transparent oder Papierton.
- Kein Text im Bild (Texte gehören als echter, übersetzbarer Seitentext daneben). Wenn doch: Englisch.
- **Leinwand-Freisteller** (`14x14-angled-*.webp`, alle 13 Städte gleich): Die Leinwand beginnt bei **7,8 %** von links und endet **6 %** vor rechts. Titel und Preis in Produktkarten stehen bündig unter der Leinwand (`.tnd-on-canvas`, `.tnd-card--canvas`).

## 7. Sprache & Inhalte
- Website zweisprachig EN (Hauptsprache) / DE. Mails aktuell Englisch.
- Feste Fakten: 12 gezeichnete Städte (Berlin, New York, Paris, London, Amsterdam, München, Seoul, Hanoi, Brüssel, Basel, Valencia, Luang Prabang = Motiv „Laos“). „Universe“ ist ein Fantasiemotiv (keine Stadt, aber als Leinwand im Shop).
- Leinwand: 344 g/m² Poly-Cotton, rundum bedruckt (3-D-Galerie-Effekt), Keilrahmen 3,1 cm; Lieferzeit 6–12 Werktage. Versand frei: DE ab 50 €, EU ab 100 €, weltweit ab 150 €.
- POS-Regel: Seiten, auf die ein QR im Laden zeigt, nie mit Rabatt/Sale.

## 8. Umsetzung in Systemen

| System | Wo | Stand |
|---|---|---|
| Shopify-Theme | `heinerradau-theme` → `assets/tnd-base.css`, Sections `tnd-*` | live |
| Tokens | [`tokens/tokens.css`](tokens/tokens.css), [`tokens/tokens.json`](tokens/tokens.json) | Kopie aus dem Theme |
| Checkout (Basic) | Shopify → Einstellungen → Checkout → Anpassen | Papier `#F2EBDD`, Übersicht `#EDE4D3`, Rot `#C8102E`, Bebas/Barlow, Logo 180 px. Ecken/Feldrand im Basic-Tarif nicht einstellbar |
| Klaviyo-Mails | Vorlagen „TND v2 · …“; Referenz + Generator in [`email/`](email/) | Welcome v2 + Abandoned Checkout v2 als Entwurf |
| Klaviyo-Formulare | Popup noch im alten Look | offen |

## 9. Ordner
```
logos/      wordmark · lockup · badge · favicon · source (Affinity-Originale + Vorschau)
tokens/     tokens.css · tokens.json
shopify/    Liquid-Snippets für Logo + Unterzeile
email/      Referenz-Mails (HTML) + build.py (Generator)
legacy/v1/  alter Stand 05/2026 (Impact, weiß/navy) – nur Archiv
index.html  Übersicht zum Anschauen
```

## 10. Offen
- Logos direkt aus Affinity als SVG exportieren und die Nachzeichnungen ersetzen (gleiche Dateinamen).
- Favicon im Shop auf `logos/favicon/favicon-badge-512.png` umstellen (Theme-Editor → Theme-Einstellungen → Favicon).
- Klaviyo-Popup im v2-Look neu bauen.
