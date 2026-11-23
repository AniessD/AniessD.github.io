# Portfolio Quarto

Portfolio data analyst freelance (version française et anglaise), déployé sur GitHub Pages.

## Structure

```text
Portfolio/
├── _quarto.yml                 # Configuration du site FR (navigation, thème, format)
├── index.qmd                   # Page d'accueil FR (à propos, expériences, recommandations, contact)
├── prestations.qmd             # Page des prestations et offres de services (FR)
├── projects.qmd                # Page listing affichant automatiquement les projets FR
├── mentions-legales.qmd        # Mentions légales (FR)
├── projects/                   # Fiches projets en français (.qmd)
│   └── ...
├── documents/                  # Documents téléchargeables (grilles de prestations PDF)
│   ├── grille_de_prestations.pdf
│   └── Services grid.pdf
├── images/                     # Vignettes, illustrations des projets et logos
├── styles.css                  # Feuille de style principale
├── fonts.html                  # Import Google Fonts (Space Grotesk / Inter / JetBrains Mono)
├── fix-accessibility.html      # Ajustements d'accessibilité
├── build.py                    # Script de compilation du site (FR + EN)
├── copy_assets.py              # Script de synchronisation des ressources entre FR et EN
│
└── en/                         # Version anglaise du site
    ├── _quarto.yml             # Configuration du site EN
    ├── index.qmd               # Page d'accueil EN
    ├── services.qmd            # Page des prestations (EN)
    ├── projects.qmd            # Page listing des projets EN
    ├── legal-notice.qmd        # Mentions légales (EN)
    ├── projects/               # Fiches projets en anglais (.qmd)
    ├── documents/              # Documents PDF côté EN
    ├── images/                 # Ressources visuelles côté EN
    ├── styles.css              # Feuille de style côté EN
    ├── fonts.html              # Import des polices côté EN
    └── fix-accessibility.html  # Ajustements d'accessibilité côté EN

