# Standards - dante-martin.com

How this site is built, where content goes, and how it is written.

This site is a single static page deployed from this GitHub repository to
Cloudflare Pages and served at `dante-martin.com`. The public content is written
directly as semantic HTML in `index.html`; JavaScript only adds optional theme,
scroll-spy, and image-preview behavior. There is no framework, templating system,
or build step. If JavaScript fails or is disabled, the portfolio content,
navigation, links, and project images still work.

---

## The one rule that matters most

**The HTML is the product. Keep the complete portfolio readable without JavaScript.**

To change what the site says, edit the corresponding semantic HTML in `index.html`.
Do not move public copy back into JavaScript or create a second content source.
Newest entries stay first within their section. Delete markup that does not apply
rather than leaving empty labels or placeholder elements.

---

## The files, and when to touch each

| File | What it is | Touch it when... |
|------|------------|----------------|
| `styles.css` | All styling, built from the tokens and components in `DESIGN.md`. | You want to change colours, spacing, fonts. Update `DESIGN.md` in the same commit. |
| `DESIGN.md` | The visual standard: tokens and components. | You add or change any visual element. |
| `index.html` | Complete semantic page content + small progressive-enhancement script. | You change public copy, links, entries, or page structure. **This is the normal one.** |
| `projects/<slug>/index.html` | Project detail page (currently only Baja). Reuses `styles.css` and follows every rule in this file. | A featured project has more real evidence than its homepage entry can hold. |
| `STANDARDS.md` | General project rules & standards. | The rules change. |
| `README.md` | Public repository documentation. | You want to update repo guidelines or project overview. |
| `.gitignore` | Git file exclusions. | You need to exclude new temp or IDE files. |
| `AGENTS.md` | Short instructions for coding agents. | The workflow for agents changes. |

### Hosting and domain rules

- Cloudflare Pages is the production host. The Pages project deploys this repository's `main` branch.
- `dante-martin.com` belongs to that Cloudflare Pages project and is managed through Cloudflare DNS.
- Do not add a repository `CNAME` file; the domain is managed in Cloudflare.
- Do not change Cloudflare DNS, the Pages custom-domain association, or production hosting unless the user explicitly asks for a hosting change.

Do not move public content into JavaScript. Do not add a second stylesheet, a
framework, a CDN link, a font import, or a build tool. The whole point is that
one person with a text editor can maintain this and that the HTML remains useful
without JavaScript.

---

## Recipes

**Add a featured project** - in `index.html`, copy an existing featured `<article
class="entry">` block, keep it in the Projects section, and edit the visible text.
Preserve the existing hierarchy: title/descriptor, organization/date metadata,
`My work`, project tools/status/method where applicable, one concise paragraph,
a descriptive link, and at most one homepage evidence image.

**Add a compact project (Other Work)** - copy an existing `<article class="entry
compact-entry">` block under `Other Work`. Keep metadata and prose shorter than a
featured project. Compact entries normally remain text-first.

**Add experience** - copy an existing Experience `<article class="entry">` and
edit the title, organization/date metadata, paragraph, and optional descriptive link.

**Add education or recognition** - copy the matching block inside
`#education`. Maintain the heading hierarchy: Education & Recognition is H2,
schools and the Recognition subsection are H3, and individual award titles are H4.

**Add a capability group** - copy an existing `.capability-group`, keep its H3
heading and one evidence-linked inline paragraph.

**Add or change a project image** - use a normal anchor pointing directly to the
image so it still works without JavaScript. Keep the `project-image-button` class
and `data-preview-*` attributes so JavaScript can progressively enhance the link
into the shared native dialog preview. Use exactly one representative homepage
image per featured project.

**Re-colour the site** - in `styles.css`, change the variables in the `:root`
block at the top. Dark-mode colours are in the `@media (prefers-color-scheme:
dark)` block right under it - update both.

---

## Writing style and attribution

### Attribution
- **Separate personal role from project technology.** A project's languages and
  frameworks go under its `tech`, not under personal skills.
- **Describe AI assistance once.** Keep the authorship note in the
  Capabilities development note, and use a project's `method` field only where
  it helps. Don't repeat it in every paragraph.
- **Match the verb to the work.** "Built" or "developed" when Dante owned the
  idea, direction, testing, and result; "designed" for architecture, UX,
  workflows, or CAD; "tested", "maintained", "integrated", or "researched" when
  that is what happened.

### General writing rules
- **Be specific. Use numbers and names.** "1.5 m wingspan, NACA 4412 airfoil"
  beats "an innovative aerodynamic design." "$10,000 enrichment fund" beats
  "significant club funds."
- **Say what YOU did**, not what the team or the field does in general.
- **No emoji. Anywhere.** Not in content, not in headings.
- **Use ordinary keyboard punctuation in visible copy.** Do not use em dashes,
  en dashes, curly quotes/apostrophes, middle-dot separators, or typographic
  ellipses. Use plain `-`, straight quotes/apostrophes, `|`, commas, or `...`
  where appropriate. Rephrase when a special punctuation mark is unnecessary.
- **Ban these words and their cousins:** passionate, innovative, cutting-edge,
  leverage, synergy, seamless, robust, dynamic, "the intersection of",
  "I'm excited to", "always eager to learn", "wearing many hats."
- **One paragraph per entry.** If you need two, the entry is doing too much.
- **Plain verbs.** "I wrote the design docs." Not "spearheaded" or
  "orchestrated."
- **No exclamation marks.** No rhetorical questions.

If a sentence could appear on anyone's portfolio, it is too vague. Cut it or
make it concrete.

---

## Hard limits

- No unnecessary external runtime dependencies: no CDNs, no web fonts, and no additional trackers. Cloudflare Web Analytics is intentionally enabled at the edge for aggregate traffic and performance measurement; adding any other analytics or tracking requires an explicit decision.
- No JavaScript libraries. JavaScript is progressive enhancement only; it must
  not create or hide essential portfolio content.
- Keep homepage copy concise, but there is no hard word cap. Featured project summaries may run roughly 60-100 words when that space is needed to explain the problem, personal contribution, and result/current state. Compact entries should stay shorter.
- Homepage featured projects use one meaningful evidence image. That image may open the shared native `<dialog>` preview for larger inspection. Compact Other Work entries normally stay text-first without image galleries.
- External web links (`http://` / `https://`) open in a new tab with `target="_blank"` and `rel="noopener noreferrer"` so visitors can inspect evidence without losing the portfolio. The visible `↗` marker means an external/new-tab destination. In-page anchors and `mailto:` links stay in the current context.
- Test before you push: confirm raw `index.html` contains the complete portfolio,
  then open it in a browser and verify light/dark mode, keyboard navigation, image
  preview behavior, narrow-screen reflow, and no console errors.

---

## Code conventions

When editing `index.html` or `styles.css`, match the existing structure and conventions.
These rules describe how the current code is written.

**JavaScript (progressive enhancement in `index.html`)**

- Do not generate public portfolio content with JavaScript. The HTML must stand alone.
- Use native controls and enhance existing links/buttons instead of replacing them.
- The project image preview must retain a direct-image anchor fallback when JavaScript
  is unavailable.
- Keep variable and function names descriptive.
- External web links open in a new tab with `target="_blank"` and `rel="noopener noreferrer"`; in-page and `mailto:` links do not. Keep `↗` reserved for external/new-tab destinations.
- Plain ES5/ES6 only; no framework, library, transpiler, bundler, or build step.

**CSS (`styles.css`)**

- **All colour, sizing, and font choices come from the `:root` variables.** Use
  `var(--accent)` and friends; do not hard-code a hex value in a rule.
- **Use the semantic typography scale.** Primary project, experience, education,
  and honor titles use `--text-title`; primary descriptions use `--text-body`;
  metadata uses `--text-meta`; subsection headings use `--text-subsection`;
  coursework and capabilities use `--text-supporting`. Compact Other Work intentionally
  uses the smaller `--text-title-compact` and
  `--text-body-compact` roles. Nested headings such as `Other Work`, Recognition,
  and Capabilities categories must remain visually secondary to top-level section headings. Dates
  belong in metadata, not title-sized subtitle text. Do not introduce one-off font
  sizes per section.
- **Theme control:** keep the button near identity/contact in DOM/tab order, while CSS may visually fix it at the top-right.
- **Dark mode is defined twice** (the `prefers-color-scheme` block and the
  `[data-theme="dark"]` block) and the two value lists must stay identical. If
  you add a variable or a dark override, update both.
- **One accent colour, used sparingly** (links, rules, active nav). Keep the
  high-contrast, near-white/near-black look and the rough 60-30-10 split.
- Group related rules under the existing `/* --- SECTION --- */` banners.
  Use `rem` units and the `0.15s` transition timing the rest of the file uses.
- Anything interactive needs a visible `:focus-visible` outline. Keep the print
  block working: it hides the nav and toggle and prints in black on white.

---

## Commit messages

### Conventional commits
Always use **Conventional Commits** format for commit messages (`type: short description` or `type(scope): short description`):
- `feat:` new feature or content section
- `fix:` bug fix or correction
- `docs:` documentation or standards updates
- `style:` visual styling, CSS adjustments, or theme changes
- `refactor:` code restructuring without changing behavior
- `chore:` maintenance, repo configuration, or cleanup

Examples:
```
feat(content): add the 2026-27 scholarships to Recognition
style(theme): adjust accent contrast ratio for dark mode
docs(standards): document the image preview recipe
fix(nav): correct active section highlight on mobile viewport
```
Keep commits atomic (one logical change per commit). Provide an optional body only when additional context or rationale is needed.
