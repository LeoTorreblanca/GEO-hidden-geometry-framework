# GEO Data

This folder contains the main observational datasets used in the initial GEO exploratory tests.

## Included datasets

### Pantheon / Pantheon+SH0ES

Used for supernova distance-modulus consistency tests.

Files included:

- `Pantheon+SH0ES.dat`
- `Pantheon+SH0ES_STAT+SYS.cov`

### BAO

BAO data used in the initial exploratory likelihood comparisons.

Folder included:

- `bao_data-master/`

---

## Internally encoded compressed priors

Some compact observational inputs were encoded directly inside the Python scripts during exploratory testing.

These include:

- fσ8 compilation
- KiDS-like compressed S8 prior
- DES/HSC-like compressed S8 prior
- DES-Y3-like compressed S8 prior

These priors can be inspected directly inside the corresponding scripts under `scripts/`.

---

## Scientific note

The current repository represents an exploratory and reproducible numerical framework.

Future versions should replace compact priors with full likelihood implementations where possible.
