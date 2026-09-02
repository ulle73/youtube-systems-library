# Architecture

```mermaid
flowchart TD
    A[Business brief + niche] --> B[Gold-standard reference]
    B --> C[Relume sitemap]
    C --> D[Wireframes + style guide]
    D --> E[Export HTML ZIP + reference URL]
    E --> F[Claude implementation]
    F --> G[Design Loop critique]
    G --> H[Higgsfield assets]
    H --> I[Interactive scroll-stopper / lead magnet]
    I --> J[Mobile optimization + manual QA]
    J --> K[SlopMonster / copy QA]
    K --> L[UI sniping + icons]
    L --> M[SEO research + content roadmap]
    M --> N[Private GitHub repo]
    N --> O[Vercel deployment]
```

## Control philosophy

This is a **pipeline of specialist checks**, not one giant prompt. The important implementation idea is to freeze or improve one layer at a time: structure before polish, visual system before assets, conversion interaction before final copy, and QA before launch.

## Human gates

1. Select a credible reference rather than blindly copying aesthetics.
2. Review the sitemap and wireframes before exporting.
3. Manually inspect mobile output on real/small screens.
4. Verify every proof/statistic in copy before shipping.
5. Review SEO recommendations before producing content.
