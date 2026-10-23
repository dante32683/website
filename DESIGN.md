# DESIGN.md

The visual standard for dante-martin.com. `STANDARDS.md` covers content and
code. This file covers how things look. Every visual value lives in a token
at the top of `styles.css`, and every element on the page is one of the
components below.

**The rule:** before you add or change anything visual, find the component
here and use it as written. If nothing fits, add a component, plus any new
tokens, to this file in the same commit as the CSS. Don't put one-off colours,
sizes, radii, borders, or timings in a rule.

## Principles

- Quiet, document-like, high contrast. The work is the content; styling stays
  out of the way.
- One accent colour, used for things you can act on (links, controls on
  hover, the active nav item) and for nothing else.
- Hover states change colour or border. They never add fills, shadows, or
  movement beyond the small arrow nudge.
- Every page works without JavaScript and in both themes.

## Tokens

All tokens are defined in `:root` in `styles.css`.

### Colour

Roughly 60% background, 30% ink, 10% accent.

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `--bg` | `#fbfbfa` | `#121316` | Page and control backgrounds |
| `--ink` | `#17191c` | `#e8e9ea` | Body text, titles |
| `--muted` | `#52565c` | `#9aa0a6` | Meta text, labels, section headings, idle nav |
| `--faint` | `#d9d9d4` | `#2c2f34` | Borders, rules, image placeholders |
| `--accent` | `#196a3c` | `#52b788` | Links, hover borders, active nav, focus ring |
| `--accent-tint` | 6% accent | 8% accent | Active nav capsule only |

Overlays use `--shadow-dialog` and `--backdrop`. The dark palette is set in two
places in `styles.css`, and both lists must stay identical.

### Type

| Token | Size | Role |
| --- | --- | --- |
| `--text-name` | 2rem | Site name, project page title |
| `--text-lead` | 1.15rem | Homepage intro, project lede |
| `--text-title` | 1.15rem | Entry titles (`h3`), honor titles |
| `--text-title-compact` | 1.1rem | Other Work titles (`h4`) |
| `--text-section` | 1.25rem | Section headings (`h2`, uppercase, muted) |
| `--text-body` | 1rem | Paragraphs |
| `--text-body-compact` | 0.95rem | Other Work paragraphs |
| `--text-subsection` | 0.95rem | Capability and recognition subheadings |
| `--text-supporting` | 0.9rem | Sidebar text, nav, buttons, capability lists |
| `--text-link-small` | 0.85rem | Text links under entries |
| `--text-meta` | 0.82rem | Org/date lines, detail rows, footer |
| `--text-caption` | 0.8rem | Image captions |
| `--text-label` | 0.78rem | Uppercase labels |
| `--text-icon` | 1.15rem | Theme control icon |
| `--text-icon-close` | 1.5rem | Image-dialog close icon |

Weights: 700 for the name, titles, and section headings; 600 for entry titles,
labels in detail rows, the active nav item, and buttons; 500 for nav; 400
otherwise. Line heights use the `--leading-*` tokens.

### Spacing

| Token | Value | Use |
| --- | --- | --- |
| `--space-rail` | 3.5rem | Top padding of sidebar and content |
| `--space-section` | 3rem | Above and below each section rule; under a project page header |
| `--space-entry` | 2.5rem | Between entries in a section |
| `--space-group` | 1.75rem | Under section headings; between capability groups |
| `--space-block` | 1.5rem | Between sidebar blocks (contact, nav groups, back link) |

### Size

| Token | Value | Use |
| --- | --- | --- |
| `--headshot` | 6rem | Sidebar headshot diameter |

Spacing inside a component (title to meta, meta to details, details to
paragraph) belongs to that component and is written as a literal rem value in
its rule. Copy the component; don't invent new gaps.

### Shape and motion

| Token | Value | Use |
| --- | --- | --- |
| `--line` | 1px | Every border and rule (`--faint` colour) |
| `--radius-control` | 4px | Controls, buttons, nav capsules, skip link |
| `--radius-media` | 6px | Evidence images |
| `--radius-dialog` | 8px | Image preview dialog |
| `--radius-round` | 50% | Headshot circle |
| `--motion` | 0.15s | Hover and focus transitions |
| `--motion-theme` | 0.3s | Light/dark colour fade |

`prefers-reduced-motion` disables all transitions and the arrow nudge.

## Components

### Text link

Accent text with an underline that grows from the centre on hover. Used for
contact links, the link under an entry (`.entry .more a`), the project header's
`.more` link, and the back link
on project pages. Destinations are marked by an arrow:

- `↗` (`<span class="arrow">`): external site, opens in a new tab. The arrow
  nudges up and right on hover.
- No arrow: in-page anchor, `mailto:`, or the back link.

Evidence references within `.capabilities-inline` use accent text and a
persistent underline with a 0.18em offset so they remain identifiable within
body text. Their visible wording stays the same as the existing reference.

### Button

`.button`: the control look applied to a link. It has a `--line` border in
`--faint`, `--radius-control`, `--text-supporting` at weight 600, and accent
text. On hover the border turns accent. It's followed by
`<span class="arrow arrow-forward">→</span>`, which nudges right on hover.

Use it only for the one link per homepage entry that opens a project-detail
page ("View Baja SAE project"). At most one button per entry. Everything else
is a text link.

### Control

Icon buttons: the theme toggle and the image-dialog close. They are
2.75rem square, with a `--line` border in `--faint`, `--radius-control`, and
`--bg` fill. On hover the border and icon turn accent. A button is the same
look in text form.

On mobile, the sidebar's top padding is `--space-section` plus
`--space-block` (4.5rem). This places identity text below the theme control,
including when the visitor enlarges the browser's preferred font size.

### Nav

The sidebar nav is a vertical list of `--text-supporting` links in `--muted`.
Hover turns them accent. The active item gets an accent left border,
`--accent-tint` capsule, and weight 600. Below 50rem it wraps horizontally.

The sidebar has two nav groups:

1. **Sections** of the current page (scroll-spy marks the active one).
2. **Project pages**: a `.nav-label` heading, then one link per detail page.
   On a detail page, its own link is marked `class="active"
   aria-current="page"`.

The desktop sidebar stays within the viewport height and scrolls when enlarged
text makes it taller. A 1.25rem horizontal padding gutter, offset by matching
negative margins, leaves room for link focus rings without changing the rail's
normal content alignment. On mobile, short desktop viewports, and print, the
sidebar uses the normal page flow without a height limit.

### Label

`.nav-label`, `.sidebar .location`, `.project-eyebrow`: `--text-label`,
uppercase, 0.05em letter-spacing, `--muted`.

### Entry

The building block of every section:

1. Title (`h3` with optional `.subtitle` in muted after a separator)
2. `.meta`: organisation | date
3. `.entry-details`: detail rows with a bold `.detail-label`
4. Paragraph
5. `.more`: one text link, or one button for a project page
6. Optional evidence image

Compact entries (Other Work) use the same order at the compact sizes and
normally have no image.

### Evidence image

`.project-image-card`: an image in a `--line` border with `--radius-media`,
`cursor: zoom-in`, and a caption in `--text-caption` muted. On hover the
border turns accent. Clicking opens the shared preview dialog. One per
homepage entry. A project page may stack several in one
`.project-images-grid`, 1.5rem apart. Crop an image to the part that matters
and let the preview open the full source.

Print hides the image-preview dialog and its backdrop, including when a
preview is open. It also removes the preview's page scroll lock so the
portfolio remains available in the printed document.

### Headshot

`.headshot`: one small photo of Dante at the top of the sidebar, above the
name, on every page that has the sidebar identity block. It is a
`--headshot` circle (`--radius-round`) with a `--line` border in `--faint`
and 1rem below it. It is not a link and has no hover state. The alt text is
"Dante Martin". It supports the name and stays the same size at every
breakpoint; don't enlarge it or add a second photo of Dante.

The file is `images/headshot.webp`: a tight head-and-shoulders square,
192px (2x the display size), with EXIF and location metadata removed.

### Section heading

`h2`: `--text-section`, weight 700, uppercase, 0.06em letter-spacing,
`--muted`, `--space-group` below. Sections are separated by a `--line` rule
with `--space-section` above and below.

## Adding something new

1. Check whether an existing component does the job. Usually one does.
2. If not, write the component here: what it's for, its tokens, and its
   hover/active states in both themes.
3. Add the CSS using only tokens, in the `SHARED COMPONENTS` block of
   `styles.css` if it's used in more than one place.
4. Check both themes, keyboard focus, narrow screens, and reduced motion.
