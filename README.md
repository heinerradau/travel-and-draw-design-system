# Travel & Draw — Design System

**Version:** 1.0  
**Date:** 2026-05-20  
**Author:** Heiner Radau / Alpha The Bat  
**Shopify Theme:** Impact (v5, 2024)

---

## 1. Brand Description

**Travel & Draw** is the artist brand of Heiner Radau — a German artist who creates graphic black-and-white city drawings with ink and fountain pen, drawn live on the streets of international cities. Every line is created on location, without photos, projectors, tracings, or studio redraws.

The brand communicates:
- **Authenticity** — real street drawing, not studio work
- **Urban storytelling** — each artwork is a personal document of a city
- **Process transparency** — the drawing journey is as valuable as the finished piece
- **Minimalist aesthetic** — black ink, white paper, no distractions

**Tagline:** *"Every line a story. Every city a sheet."*  
**Brand name:** Travel & Draw  
**Domain:** heinerradau.de

---

## 2. Target Audience

- Art buyers looking for unique, story-rich urban art (25–55)
- Interior design enthusiasts who value original, handcrafted pieces
- City lovers and travel enthusiasts
- B2B buyers: hotels, offices, city merchandise programs, tourism boards
- Instagram-native art discovery audience (~4.8k followers)
- International audience (shipping to 30+ countries)

---

## 3. Visual Style

### Core Principle: Minimalist Frame for Complex Art

The design system's primary function is to **stay out of the way** of the artwork. The black-and-white ink drawings carry all the visual weight. Everything else — layout, typography, color — creates a clean, gallery-like frame.

**Key characteristics:**
- High contrast: white backgrounds, dark text/accent
- Generous whitespace — gallery breathing room
- Typographic hierarchy through weight and size, not color
- No decorative elements, gradients, or visual noise
- Dark accent color (navy-charcoal) for interactive elements
- Rounded, friendly shapes for UI components (buttons, inputs)
- Subtle shadows for depth on cards and elevated elements

**Mood:** Calm, confident, architectural, international, artistic — not loud, not trendy, not commercial-feeling.

---

## 4. Color Palette

### Primary Palette (from Shopify Theme — Impact v5)

| Token | CSS Variable | RGB | Hex | Usage |
|-------|-------------|-----|-----|-------|
| **Text Primary** | `--text-primary` | `39 39 39` | `#272727` | Body text, headings, UI labels |
| **Text Light** | `--text-color` | `255 255 255` | `#FFFFFF` | Text on dark backgrounds |
| **Accent** | `--accent` | `31 38 51` | `#1F2633` | Buttons, links, interactive elements |
| **Background Primary** | `--background-primary` | `255 255 255` | `#FFFFFF` | Page background, cards |
| **Footer Background** | `--footer-background` | `242 242 242` | `#F2F2F2` | Footer, subtle section alternation |
| **Header Background** | `--header-background` | `255 255 255` | `#FFFFFF` | Sticky header with blur |

### Secondary / Functional Colors

| Token | RGB | Hex | Usage |
|-------|-----|-----|-------|
| **Error Text** | `170 40 38` | `#AA2826` | Form error messages |
| **Error Background** | `245 229 229` | `#F5E5E5` | Form error backgrounds |
| **Sale Badge** | `227 79 79` | `#E34F4F` | Sale/discount badges |
| **Primary Badge** | `60 97 158` | `#3C619E` | "New" or featured badges |
| **Border** | `text-primary / 0.12` | `rgba(39,39,39,0.12)` | Subtle borders |

### Portfolio/Print Palette (supplementary)

| Hex | Usage |
|-----|-------|
| `#111111` | Dark covers, hero backgrounds |
| `#F5F0EB` | Warm off-white paper tone |
| `#FEFEFE` | Print page backgrounds |
| `#F0ECE7` | Tag/chip backgrounds |

### Color Philosophy

- **Never use color as decoration.** The art is black and white — the UI should be too.
- Accent color (`#1F2633`) is a deep navy-charcoal — never pure black, never bright.
- White space is active design element, not empty space.
- Red is reserved for sale badges and errors only.
- Blue is reserved for informational badges only.

---

## 5. Typography

### Font Stack

| Role | Font Family | Weight | Style | Usage |
|------|------------|--------|-------|-------|
| **Headings** | `Playfair, serif` | 400 | normal | H1–H6, section titles, product titles |
| **Body** | `Libre Franklin, sans-serif` | variable (400–700) | normal | Body text, buttons, navigation, forms |

### CSS Implementation

```css
:root {
  --heading-font-family: 'Playfair', serif;
  --heading-font-weight: 400;
  --heading-font-style: normal;
  --heading-letter-spacing: 0;
  --heading-text-transform: normal;

  --text-font-family: 'Libre Franklin', sans-serif;
}
```

### Typographic Scale

| Level | Font Size | Line Height | Usage |
|-------|-----------|-------------|-------|
| H1 | `calc(min(20vw, 65px))` | 1.1 | Hero headlines (Impact text) |
| H2 | ~40px | 1.2 | Page titles, major sections |
| H3 | ~28px | 1.3 | Section headings |
| H4 | ~22px | 1.3 | Card titles, sub-sections |
| H5 | ~16px | 1.4 | Small headings |
| Body | 16px | 1.6 | Body text |
| Small | 14px | 1.5 | Captions, meta |
| X-Small | 12px | 1.4 | Legal, footer fine print |

### Typography Rules

- Headings in **Playfair** — elegant, editorial, never bold (400 weight is enough)
- Body text in **Libre Franklin** — clean, modern, highly readable
- Never use Playfair for body text (poor readability)
- Never use Libre Franklin for large headings (loses character)
- Letter-spacing on headings: `0` (natural Playfair spacing is sufficient)
- Uppercase only for small labels (10–12px) with `letter-spacing: 3–6px`

---

## 6. Button Styles

### Primary Button

```css
.button--primary {
  background: rgb(var(--button-background-primary)); /* #1F2633 */
  color: rgb(var(--button-text-primary));             /* #FFFFFF */
  font-family: var(--text-font-family);
  border-radius: var(--rounded-button);               /* 3.75rem — pill shape */
  padding: 0.875rem 2.5rem;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: background-opacity 0.2s;
}

.button--primary:hover {
  opacity: 0.85;
}
```

### Secondary / Ghost Button

```css
.button--secondary {
  background: transparent;
  color: rgb(var(--text-primary));                     /* #272727 */
  border: 1px solid rgba(var(--text-primary), 0.12);
  border-radius: var(--rounded-button);
  padding: 0.875rem 2.5rem;
  font-family: var(--text-font-family);
  font-size: 1rem;
  cursor: pointer;
}
```

### Button Variants

| Variant | Background | Text | Border | Usage |
|---------|-----------|------|--------|-------|
| **Primary** | `#1F2633` | `#FFFFFF` | none | Main CTAs, Add to Cart, Submit |
| **Secondary** | transparent | `#272727` | `rgba(39,39,39,0.12)` | Secondary actions, "Learn more" |
| **Ghost** | `rgba(39,39,39,0.05)` | `#272727` | none | Low-emphasis actions |

### Button Rules

- All buttons are **pill-shaped** (`border-radius: 3.75rem`)
- Minimum tap target: 44px height
- Font: Libre Franklin, never Playfair
- Only ONE primary button per section
- Button text: short, action-oriented, no punctuation
- Never use color (red/green) for buttons — only the accent navy

---

## 7. Layout Rules

### Grid System

| Token | Value | Usage |
|-------|-------|-------|
| Max container width | `1800px` | Full-width content |
| Narrow container | `1550px` | Reading-optimized content |
| Rich text max | `650px` | Long-form text blocks |
| Press section max | `1000px` | Press/logo sections |
| Grid gutter | `var(--spacing-5)` | ~20px on desktop |
| Container gutter | `var(--spacing-5)` | ~20px page edge padding |

### Spacing Scale

```
--spacing-2:  0.5rem   (8px)
--spacing-3:  0.75rem  (12px)
--spacing-4:  1rem     (16px)
--spacing-5:  1.25rem  (20px)
--spacing-6:  1.5rem   (24px)
--spacing-8:  2rem     (32px)
--spacing-9:  2.25rem  (36px)
--spacing-10: 2.5rem   (40px)
--spacing-12: 3rem     (48px)
```

### Section Spacing

- **Section outer spacing** (top/bottom margin): `--spacing-10` (40px)
- **Section stack gap** (between adjacent sections): `--spacing-8` (32px)
- **Section inner spacing** (padding inline): `--container-gutter` (20px)
- **Section inner max block**: `--spacing-9` (36px)

### Product Grid

```css
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  column-gap: var(--grid-gutter);
  row-gap: var(--spacing-8);
}
```

- Default: 3–4 columns on desktop
- Tablet: 2 columns
- Mobile: 1–2 columns

### Header

- Sticky header with backdrop blur (`14px blur`, 60% opacity)
- Logo: 170px wide × 85px high (desktop), 150×75 (mobile)
- Grid: `"main-nav logo secondary-nav"` centered layout
- Background: white, transparent text: `#272727`

### Layout Principles

1. **Gallery breathing room always wins over density.**
2. **Single-column for reading, grid for browsing.**
3. **No sidebars** — content is full-width within containers.
4. **Sticky header only** — no floating elements, no popups on load.
5. **Mobile-first breakpoints** — design for narrow screens first.

---

## 8. Imagery & Visual Language

### Artwork Photography

- **Style:** Documentary / process-oriented
- **In-situ shots:** Artwork in customer homes, on walls, in context
- **Process shots:** Heiner drawing on the street — the artist at work
- **Detail shots:** Close-ups of ink lines, textures, signatures
- **City context:** The artwork alongside the real location

### Photography Rules

- **No glossy product mockups** — real photos only
- **Natural lighting preferred** — no studio lighting aesthetic
- **People are secondary** — the artwork is always the subject
- **Color photos for context** — but the artwork itself is black and white
- **Aspect ratios:** Flexible, but hero images 16:9 or 3:2

### Image Treatment

- No filters or presets applied to artwork photos
- Customer photos: authentic, unpolished
- Product cards: artwork fills frame, minimal padding
- Overlay on hero images: `0 0 0 / 0.0` to `0 0 0 / 0.3` (subtle dark overlay)

### Logo & Brand Mark

- The header uses a **text-based logo**: "Travel & Draw" or "@heinerradau" 
- No standalone icon/logo mark currently in use
- Logo is positioned center in header grid
- Logo dimensions: 170×85px (desktop), 150×75px (mobile)

---

## 9. Components

### Product Card

```
┌──────────────────────┐
│                      │
│    [Artwork Image]   │
│                      │
├──────────────────────┤
│ City Name            │ ← Playfair, ~18px
│ Product Type         │ ← Libre Franklin, 14px, subdued
│ €XX,XX              │ ← Libre Franklin, 16px, semibold
└──────────────────────┘
```

- White background
- Subtle shadow on hover
- Image fills card, no border radius on image
- Title + price below image
- No "Sale" badge unless discounted

### Newsletter Form

```
┌─────────────────────────────────────┐
│         Section Heading             │ ← Playfair, centered
│       Subtitle / incentive          │ ← Libre Franklin, 16px
│                                     │
│  ┌──────────────────┐ ┌──────────┐ │
│  │  E-mail address  │ │ Sign up  │ │ ← Input + button inline
│  └──────────────────┘ └──────────┘ │
│                                     │
│       No spam, no ads text          │ ← Small, subdued
└─────────────────────────────────────┘
```

### Hero Section (Landing Page)

```
┌──────────────────────────────────────┐
│                                      │
│    [Full-width artwork/process       │
│     image with subtle dark           │
│     overlay]                         │
│                                      │
│    H1: Main headline                 │ ← Playfair, large, white
│    Subtitle text                     │ ← Libre Franklin, white
│                                      │
│    [Primary Button]                  │ ← Pill button
│                                      │
└──────────────────────────────────────┘
```

---

## 10. Dos & Don'ts

### ✅ DO

- Use lots of white space — let the artwork breathe
- Keep typography clean: Playfair for headings, Libre Franklin for body
- Use the deep navy (`#1F2633`) as the only accent color for UI
- Rounded pill buttons (`border-radius: 3.75rem`) for all CTAs
- Show real artwork, real processes, real customer photos
- Keep copy direct, honest, and personal — not corporate
- Maintain high contrast: dark text on white, white text on dark
- Design for mobile first, then scale up

### ❌ DON'T

- **Never use bright colors** — no orange, green, pink, or gradient CTAs
- **Never use pure black** (`#000`) — use `#272727` or `#1F2633`
- **Never add decorative borders, dividers, or ornamentation**
- **Never use sans-serif for large headings** — Playfair only
- **Never use serif for body text** — Libre Franklin only
- **Never use drop shadows aggressively** — subtle only (`rgba(39,39,39,0.1)`)
- **Never use stock photography** — all imagery must be authentic
- **Never use emoji in UI** — emoji in customer quotes only
- **Never use animation for decoration** — only for functional feedback (hover, loading)
- **Never use colored backgrounds for sections** — white or `#F2F2F2` only
- **Don't crowd elements** — spacing is generous by default
- **Don't use "sale!" language** — let the art speak, not the discount
- **Don't use corporate marketing clichés** — "revolutionary", "game-changing", etc.

---

## 11. Shopify Theme Reference

This design system is extracted from the live Shopify store using the **Impact** theme (v5, 2024 by Maestrooo).

The Impact theme uses:
- **CSS Custom Properties** for all design tokens (see `shopify/theme-tokens.css`)
- **Liquid sections** for modular page building
- **Shopify's `srcset`** for responsive images
- **Native Shopify cart/drawer** components

Custom theme customizations:
- Logo size: 170×85px (desktop), 150×75px (mobile)
- Header layout: centered logo with navigation on sides
- Footer: light gray background (`#F2F2F2`)
- Product cards: white background, clean layout
- Typography overrides: Playfair headings, Libre Franklin body

---

## 12. Related Resources

- **Live site:** https://www.heinerradau.de
- **NYC Art Map (funnel):** https://www.heinerradau.de/nyc-art-map
- **Instagram:** https://www.instagram.com/heinerradau
- **Shopify Theme:** Impact by Maestrooo (v5)
- **Font: Playfair** — https://fonts.google.com/specimen/Playfair (SIL Open Font License)
- **Font: Libre Franklin** — https://fonts.google.com/specimen/Libre+Franklin (SIL Open Font License)
