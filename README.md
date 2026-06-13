
# Sumit Prajapat — Portfolio

A single-page portfolio for a **Data Analyst & BI Developer**, built around a
terminal / SQL editor aesthetic. No framework, no build step — one hand-written
`index.html` (HTML, CSS, and vanilla JS).

🔗 **Live:** https://skpkush.github.io

## Highlights

- **psql-style hero** — an animated SQL query that "returns" the intro row
- **Projects as SQL** — tab filters rewrite a live `SELECT … WHERE … ORDER BY`
  query, with a psql result-set table of headline metrics
- **Journey as a git log** — career history rendered as `git log` commits
- **Command palette** — `⌘K` / `Ctrl+K` to jump between sections and actions
- **Light / dark theme**, scroll-reveal animations, and a downloadable
  ATS-friendly resume

## Stack

Plain `HTML` + `CSS` + vanilla `JavaScript`. Fonts: Inter + JetBrains Mono
(Google Fonts). Hosted free on **GitHub Pages**.

## Run locally

It's a static site — just open `index.html` in a browser. Or serve it:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

## Structure

```
index.html                      # the entire site
resume/
  └─ Sumit_Prajapat_Resume.pdf  # downloadable resume
```

## Contact

- **Email:** sumitkprajapat29@gmail.com
- **GitHub:** [github.com/Skpkush](https://github.com/Skpkush)
- **LinkedIn:** [in/sumit-k-prajapat](https://www.linkedin.com/in/sumit-k-prajapat/)
