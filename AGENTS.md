# AGENTS.md

Instructions for coding agents editing **dante-martin.com**, a personal
portfolio site.

## Read first

- **[STANDARDS.md](STANDARDS.md)**: which file to edit, how to add content, and
  the writing rules.
- **[DESIGN.md](DESIGN.md)**, for any visual change: every colour, size,
  spacing, button, and link style comes from it.

## Summary

- The homepage content lives in semantic `index.html`; static project detail
  pages live in `projects/<slug>/index.html`. Don't add a client-side content
  renderer or external content data source.
- Add homepage content in `index.html`. For a featured project with more
  evidence than the homepage entry can hold, edit its project page. Follow
  STANDARDS.md to choose the page that owns the content; newest homepage
  entries stay first.
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

Open the changed page in a browser and confirm it renders in light and dark
mode with no blank labels and no console errors. Commit with Conventional
Commits (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `chore:`). A push to
`main` deploys the live site, so get Dante's approval before pushing unless
that specific deployment is already authorized.
