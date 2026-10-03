# Portfolio website

[Visit the public portfolio](https://emanuel-walker-cyber.walkwithemanuel.chatgpt.site)

Responsive, static HTML/CSS/JavaScript portfolio with an interactive six-project map, project filters and detail views, career timeline, and two downloadable resumes.

## Preview locally

From the repository root:

```sh
python -m http.server 8000 --directory website
```

Open http://localhost:8000 in your browser. No package installation or build step is required.

## Edit

- `index.html`: introduction, career history, education, and contact links.
- `app.js`: project content, filters, project dialogs, and resume selection.
- `style.css`: visual design and responsive layouts.
- `assets/`: resume PDF location used by the hosted site. The PDFs are not included in this repository pending explicit publication approval. Local resume download buttons require those files.

The website uses Google Fonts, with local fallback fonts. Project links point to this repository.

## Publishing

The public site is hosted on ChatGPT Sites. This directory is a source copy of the published portfolio. GitHub commits do not automatically redeploy that site. Apply future website changes to the hosted Site and republish it to update the public URL.
