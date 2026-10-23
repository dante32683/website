# AGENTS.md

Instructions for coding agents editing **dante-martin.com**, a personal
portfolio site.

## Read first

- **[STANDARDS.md](STANDARDS.md)**: which file to edit, how to add content, and
  the writing rules.
- **[DESIGN.md](DESIGN.md)**, for any visual change: every colour, size,
  spacing, button, and link style comes from it.

## Summary

- All public content lives in semantic `index.html`. Don't add a client-side
  content renderer or a second content source.
- To add something, copy the matching HTML block, place it in the right
  section, and edit the visible text and links. Newest entries stay first.
- Styling is in `styles.css`; re-skin through the `:root` variables at the top.
- No build step, frameworks, CDNs, web fonts, or extra trackers. JavaScript is
  progressive enhancement only.

## Writing

Be specific: numbers, names, and what Dante did. No emoji, no hype words, one
short paragraph per entry. Project languages and frameworks go under the
project's `tech`, not under personal skills. AI assistance is described once,
in the development note; don't repeat it in every project. Details are in
STANDARDS.md.

## Before you finish

Open `index.html` in a browser and confirm it renders in light and dark mode
with no blank labels and no console errors. Commit with Conventional Commits
(`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `chore:`) and push.
