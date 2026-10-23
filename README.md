# dante-martin.com

The source code for Dante Martin's personal website and portfolio. It is a lightweight, single static page deployed from this repository to Cloudflare Pages and served at `dante-martin.com`.

## Core Design Principles

- **Static HTML First:** The complete portfolio is present in `index.html` before JavaScript runs. No compilers, transpilers, templating system, or bundlers.
- **Minimal Runtime Dependencies:** No CDN, web-font, or CSS/JS framework dependencies. Cloudflare Web Analytics is intentionally enabled at the edge for aggregate site-traffic and real-user performance measurement.
- **Progressive Enhancement:** JavaScript only handles the saved theme override, active-section highlighting, and image-preview dialog. The portfolio remains readable and navigable without it.

## Project Structure

- `index.html` - **Main file.** Complete semantic portfolio content plus small progressive-enhancement JavaScript.
- `styles.css` - High-contrast, minimal CSS styling using custom property themes (green color palette) with smooth transitions, native responsive queries, and dedicated print stylesheets.
- `DESIGN.md` - Visual tokens and components.
- `STANDARDS.md` - Content structure, writing style, and code conventions.
- `AGENTS.md` - Short instructions for coding agents.

## Hosting

Cloudflare Pages deploys `main` to `dante-martin.com`.

## Making Changes

See **[STANDARDS.md](STANDARDS.md)** for structure and writing style.

1. Edit the relevant semantic content in `index.html`.
2. Open `index.html` in a web browser to test locally.
3. Confirm the page renders correctly in both **light and dark modes** (using the theme toggle).
4. Run standard print-to-PDF previews to ensure layout prints cleanly.
5. Commit using **Conventional Commits** (`feat:`, `fix:`, `docs:`, `style:`, etc.) and push.
