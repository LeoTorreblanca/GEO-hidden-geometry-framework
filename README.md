---
layout: default
---

<meta name="google-site-verification" content="Kila_Tq12oqpqTSHe5GuDIefLwcCL2V8Zenj-O5PUi4" />

# 🌌 GEO — Hidden Geometry Framework

**Author:** Leonel Hernan Torreblanca

**Framework:** GEO — Hidden Geometry / Geometría Oculta

📄 **Framework / Paper Archive (OSF):**  
https://doi.org/10.17605/OSF.IO/YHDMZ

💻 **Framework Code Archive (Zenodo):**  
https://doi.org/10.5281/zenodo.20225304

🧪 **Cosmological MCMC Validation (GitHub):**  
https://github.com/LeoTorreblanca/GEO-Cosmology-MCMC

📦 **Cosmological MCMC Archived Release (Zenodo):**  
https://doi.org/10.5281/zenodo.22103137

---

## Overview

GEO (Hidden Geometry Framework) is an exploratory mathematical and
cosmological framework investigating whether stable geometric transfer
relations can reproduce selected observational structures through an
internal operator architecture.

The framework explores geometric operators, transfer structures,
hidden efficiency relations, cosmological applications, planetary
architectures, and reproducible numerical experiments.

The central objective is not to introduce arbitrary phenomenological
corrections to individual datasets, but to investigate whether a
restricted geometric architecture can generate stable relations that
can subsequently be confronted with observations.

This repository is the principal public repository of the GEO
framework. It contains mathematical notes, validation studies,
experimental results, GEO-Lens applications, numerical tests, and
links to dedicated reproducibility repositories.

GEO should presently be regarded as an exploratory framework under
active numerical and theoretical testing, not as an established
physical theory.

---

# 1. Canonical GEO architecture

A central quantity appearing throughout the framework is the canonical
partition / efficiency parameter

$$\eta=\frac{3}{5}=0.6.$$

The corresponding geometric fraction is

$$f_c=\sqrt{\eta}=0.774596669241483.$$

A complementary sector can be represented by

$$f_{\mathrm{out}}=1-f_c.$$

The framework distinguishes the canonical parameter $\eta$ from the
effective GEO state $\mu$ relevant to a particular physical channel.

The canonical radial relation is

$$R=\mu^{1/3}.$$

This distinction is important.

The expression

$$R=\eta^{1/3}$$

must **not** be interpreted as the general GEO radial law.

The canonical law is

$$R=\mu^{1/3},$$

where $\mu$ denotes the relevant GEO efficiency or effective state.

For the specific Hubble-channel realization investigated in the
cosmological analysis,

$$\mu_H=\eta=0.6.$$

Therefore, specifically in that channel,

$$R=\mu_H^{1/3}=0.843432665301749.$$

The equality $\mu_H=\eta$ is a channel realization being tested by the
framework, not a replacement of the general distinction between
$\mu$ and $\eta$.

---

# 2. GEO operator chain

The Hubble realization uses the GEO operator

$$\Phi=1.88961381521168.$$

The associated intensity factor is

$$\alpha=\frac{\Phi(1-\eta)}{\sqrt{2}}=0.534463497023985.$$

Using the Hubble-channel radial state,

$$R=\mu_H^{1/3},$$

the corresponding projection factor is

$$P_{\mathrm{GEO}}=1+\alpha(1-R)=1.083679525222552.$$

The local GEO realization is consequently written as

$$H_{0,\mathrm{GEO}}=P_{\mathrm{GEO}}H_{0,\mathrm{primitive}}.$$

This relation provides the bridge between the primitive cosmological
expansion parameter and the locally realized GEO value used in the
Hubble-channel tests.

---

# 3. GEO-Lens application to the Hubble tension

The Hubble tension provides one of the principal cosmological test
cases of the GEO framework.

Historically, the GEO operator chain was evaluated using the reference
primitive value

$$H_{0,\mathrm{primitive}}=67.40\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

Application of the canonical GEO projection gives

$$H_{0,\mathrm{GEO}}=67.40\times1.083679525222552=73.040000\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

This numerical reconstruction motivated the subsequent CLASS,
profile-likelihood, and MCMC investigations.

The value $73.040000$ should therefore be understood as the
**canonical historical GEO reconstruction from the fixed 67.40 input**.

It should not be confused with the posterior value obtained when the
primitive cosmological parameters themselves are sampled against
Planck/NPIPE data.

That later statistical test is documented independently in
GEO-Cosmology-MCMC.

---

# 4. Cosmological MCMC validation

A dedicated numerical study now tests the GEO Hubble realization using
Cobaya, CLASS, Planck likelihoods, matched control calculations, and
multiple MCMC chains.

👉 **Repository:**  
https://github.com/LeoTorreblanca/GEO-Cosmology-MCMC

📦 **Archived release:**  
https://doi.org/10.5281/zenodo.22103137

The principal likelihood configuration includes:

- Planck 2018 low-$\ell$ TT;
- Planck 2018 low-$\ell$ EE;
- Planck NPIPE CamSpec TTTEEE;
- a local-$H_0$ likelihood for the joint comparison;
- a matched $\Lambda$CDM control.

The analysis preserves the distinction between the primitive
cosmological expansion parameter and the GEO local realization:

$$H_{0,\mathrm{GEO}}=P_{\mathrm{GEO}}H_{0,\mathrm{primitive}}.$$

The GEO projection factor is fixed by the canonical operator chain,

$$P_{\mathrm{GEO}}=1.083679525222552.$$

---

## 4.1 Extended GEO-29 posterior

The extended GEO-29 calculation gives

$$H_{0,\mathrm{primitive}}=67.7213\pm0.4884\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

After application of the canonical GEO projection,

$$H_{0,\mathrm{GEO}}=73.3882\pm0.5292\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

The corresponding posterior means include

$$\Omega_m=0.309465,$$

and

$$\sigma_8=0.818567.$$

The best sampled GEO-29 point gives

$$H_{0,\mathrm{primitive}}=67.833577\;\mathrm{km\,s^{-1}\,Mpc^{-1}},$$

which maps to

$$H_{0,\mathrm{GEO}}=73.509859\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

---

## 4.2 Matched GEO versus ΛCDM comparison

The matched best-point comparison gives, for GEO minus the
$\Lambda$CDM + local-$H_0$ control,

$$\Delta\chi^2_{\mathrm{CMB}}=-3.242000,$$

$$\Delta\chi^2_{\mathrm{local}\,H_0}=-16.696923,$$

and

$$\Delta\chi^2_{\mathrm{joint}}=-19.938923.$$

Negative values correspond to a lower best-point chi-square for the GEO
realization in this exact matched likelihood configuration.

The best sampled GEO-29 point has

$$\chi^2_{\mathrm{CMB}}=10962.919,$$

$$\chi^2_{\mathrm{local}\,H_0}=0.204111,$$

and

$$\chi^2_{\mathrm{joint}}=10963.123111.$$

The corresponding matched $\Lambda$CDM + local-$H_0$ control has

$$\chi^2_{\mathrm{CMB}}=10966.161,$$

$$\chi^2_{\mathrm{local}\,H_0}=16.901034,$$

and

$$\chi^2_{\mathrm{joint}}=10983.062034.$$

These numbers refer specifically to the likelihood, priors, model
mapping, nuisance parameters, and numerical configuration documented
in the dedicated MCMC repository.

They should not be interpreted as a general Bayesian evidence ratio or
as proof that GEO supersedes $\Lambda$CDM.

---

# 5. Independent profile test of the canonical eta node

The canonical GEO efficiency was also tested through profile-likelihood
calculations in which the corresponding geometric fraction was allowed
to vary.

The wide profile gives

$$f_{c,\mathrm{best}}=0.774088414673177.$$

Since

$$\eta=f_c^2,$$

this corresponds to

$$\eta_{\mathrm{best}}=0.599212873731233.$$

The canonical GEO prediction is

$$f_{c,\mathrm{GEO}}=\sqrt{\frac{3}{5}}=0.774596669241483,$$

and

$$\eta_{\mathrm{GEO}}=0.600000000000000.$$

At the canonical node, the profile penalty is

$$\Delta\chi^2_{\mathrm{GEO}}=0.001005928553.$$

Thus, within this profile experiment, the canonical GEO node lies
extremely close to the numerical likelihood minimum.

Cross-configuration calculations give a median preferred value

$$\eta_{\mathrm{median}}=0.6.$$

The mean canonical-node penalty across the tested configurations is

$$\left\langle\Delta\chi^2_{\mathrm{GEO}}\right\rangle=0.089354084305,$$

with a maximum tested penalty of

$$\Delta\chi^2_{\mathrm{GEO,max}}=0.267647200015.$$

These configurations are not all statistically independent.

Consequently, these calculations establish **compatibility and
cross-configuration numerical stability** of the canonical
$\eta=3/5$ node within the tested setup.

They do not independently establish $\eta=3/5$ as a measured universal
constant of nature.

---

# 6. MCMC convergence and numerical stability

The dedicated GEO cosmological study contains matched short-chain and
extended-chain calculations.

The principal extended GEO-29 calculation used four MPI chains with
30,000 stored rows per chain:

$$4\times30,000=120,000$$

stored chain rows.

The final recorded convergence diagnostic was

$$R-1=0.017309752619.$$

A stricter pre-specified target was

$$R-1<0.01.$$

That strict stopping criterion was not formally reached before the
sample cap.

For this reason, GEO-29 is reported as an **extended, numerically
stable / near-converged MCMC calculation**, rather than as a chain that
formally satisfies the stricter $R-1<0.01$ criterion.

The shorter GEO-28B and extended GEO-29 runs nevertheless give closely
consistent posterior results.

For GEO-28B,

$$H_{0,\mathrm{GEO}}=73.3998\pm0.4998\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

For GEO-29,

$$H_{0,\mathrm{GEO}}=73.3882\pm0.5292\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

This agreement provides an internal numerical stability check while
the exact convergence diagnostic remains explicitly reported.

---

# 7. Reproducibility package

The cosmological MCMC repository contains the publication-oriented
reproducibility package used for the current GEO cosmological
validation.

It includes:

- matched GEO and $\Lambda$CDM Cobaya configurations;
- Planck/NPIPE likelihood configuration;
- MCMC checkpoints;
- proposal covariance matrices;
- convergence histories;
- posterior summaries;
- best-point comparisons;
- machine-readable CSV tables;
- publication-quality figures;
- profile-likelihood validation of $\eta$;
- cross-configuration tests;
- software environment freeze;
- Python dependency freeze;
- CLASS source hashes;
- GEO-modified source hashes;
- SHA256 chain manifests;
- consistency-audit scripts;
- reproducibility documentation.

The frozen publication audit reports:

```text
AUDIT PASSED
All frozen numerical quantities are internally consistent.
```

The archived release is available at:

https://doi.org/10.5281/zenodo.22103137

---

# 8. Technical validation kit — CLASS

The public implementation of GEO-related cosmological calculations for
CLASS v3.x is available separately.

👉 **GEO Launch Kit:**  
https://github.com/LeoTorreblanca/GEO_Launch_Kit

The GEO Launch Kit contains source modifications and diagnostic scripts
used in the development and reproducibility analysis of GEO-Lens
calculations.

It is released under the MIT License for independent inspection,
testing, reproduction, and scientific discussion.

---

## CLASS-GEO-Lens

Public implementation:

https://github.com/LeoTorreblanca/CLASS-GEO-Lens

Archived release:

https://doi.org/10.5281/zenodo.20529415

CLASS-GEO-Lens should be distinguished from the dedicated
GEO-Cosmology-MCMC statistical validation repository.

The former provides a public implementation environment for the GEO
cosmological mapping.

The latter contains the dedicated matched MCMC and profile-likelihood
analysis.

---

# 9. Scientific documentation

The mathematical development of the GEO Hubble realization is
documented through the technical sheets included in this repository.

- [PDF 1 — Hubble Tension 12-Digit Auditing](./docs/mathematics/01-HUBBLE_12_DIG_GEO_response_EN.pdf)
- [PDF 2 — Reconstructive vs Strong Prediction Levels](./docs/mathematics/02-HUBBLE_MATHS_EN.pdf)
- [PDF 3 — GEO Bridge & Coupling Metrics](./docs/mathematics/03-GEO_BRIDGE_EXPLAINED_EN.pdf)
- [PDF 4 — Universal Alpha Derivation Thesis](./docs/mathematics/04-GEO_ALPHA_FINAL_DEMONSTRATION_EN.pdf)
- [PDF 5 — Final Cosmological Closure Report](./docs/mathematics/05-FINAL_RESOLUTION_HUBBLE_EN.pdf)

These documents describe the mathematical and historical development of
the framework.

The dedicated MCMC repository should be used for the current
statistical cosmological validation.

---

# 10. GEO experimental test series

The GEO framework developed through a sequence of numerical and
geometric tests.

## PRUEBA 1 — SOP emergence

Initial exploration of:

- growth suppression;
- stable $S_8$ regions;
- emergence of an effective geometric fraction;
- complementary-sector interpretation.

---

## PRUEBA 2 — Geometric node analysis

Analysis of preferred geometric regions including:

- $3/4$;
- $\sqrt{3/5}$;
- $\pi/4$;
- effective geometric bands.

---

## PRUEBA 3 — Architectural transfer structure

Investigation of:

- geometric partition;
- active/complementary transfer;
- efficiency structure;
- architectural consistency.

---

## PRUEBA 4 — Prediction law

Exploration of the radial prediction relation

$$R=\mu^{1/3}$$

and its transfer consistency.

The relevant state is $\mu$.

The historical expression $R=\eta^{1/3}$ should not be treated as the
general GEO radial identity.

---

## PRUEBA 5 — Observational consistency

Exploratory consistency analysis involving:

- $S_8$;
- effective suppression;
- $E_G$;
- geometric prediction stability;
- cross-observable behavior.

These exploratory stages motivated the later dedicated profile and
MCMC analyses.

---

# 11. Multi-planetary empirical validation

The GEO framework has also been explored outside the primary
cosmological Hubble application.

A dedicated empirical study analyzes orbital architectures in
multi-planetary systems using data derived from the NASA Exoplanet
Archive.

👉 **GEO Exoplanets Validation:**  
https://github.com/LeoTorreblanca/GEO-Exoplanets-Validation

The study investigates geometric transition statistics, orbital
spacing, node structure, and possible architecture-dependent
discontinuities.

Reported exploratory results include:

- analysis of 2,099 multi-planetary systems with $N\geq3$;
- a reported 98.09% coherence rate under the adopted transition
  definition;
- changes in transition frequency around higher-multiplicity systems;
- concentration of selected internal transition locations.

These results belong to a separate empirical application of GEO and
should not be treated as statistically independent evidence for the
cosmological Hubble realization without an explicit joint statistical
model.

---

# 12. Spanish technical reconstruction

A dedicated Spanish-language technical reconstruction of the framework
is maintained separately.

👉 **GEO — Geometría Oculta ESP:**  
https://github.com/LeoTorreblanca/GEO-Geometria-Oculta-ESP

This repository provides a cleaner Spanish-language presentation of
the framework, its geometric architecture, and its experimental
development.

---

# 13. Current scientific status

The current public GEO program now contains several distinct levels of
evidence and development.

### Mathematical framework

GEO proposes a constrained internal geometric architecture involving
partition, projection, complementary sectors, effective states, and
geometric transfer operators.

### Historical Hubble reconstruction

The canonical Hubble operator chain maps

$$67.40\longrightarrow73.040000\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

This is the original fixed-input GEO reconstruction.

### Profile-likelihood validation

When the relevant efficiency parameter is allowed to vary in the
profile experiment,

$$\eta_{\mathrm{best}}=0.599212873731233,$$

very close to the canonical prediction

$$\eta_{\mathrm{GEO}}=0.6.$$

### Cosmological MCMC validation

The Planck/NPIPE MCMC calculation independently samples the primitive
cosmological scale and obtains

$$H_{0,\mathrm{primitive}}=67.7213\pm0.4884\;\mathrm{km\,s^{-1}\,Mpc^{-1}},$$

which the fixed GEO operator maps to

$$H_{0,\mathrm{GEO}}=73.3882\pm0.5292\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

Within the exact matched joint likelihood experiment, the best sampled
comparison gives

$$\Delta\chi^2_{\mathrm{joint}}=-19.938923.$$

These are stronger numerical tests than the original fixed-input
reconstruction because the primitive cosmological parameter is sampled
within an explicit likelihood analysis.

They remain tests of the proposed GEO realization rather than proof of
the framework as a fundamental physical theory.

---

# 14. Present limitations and next tests

Earlier versions of the GEO documentation identified a full
cosmological MCMC analysis as an outstanding validation step.

**That step has now been performed.**

The dedicated GEO-Cosmology-MCMC repository provides the current
Planck/NPIPE MCMC validation and its reproducibility package.

The principal remaining limitations are therefore no longer the
absence of an MCMC analysis.

They are:

1. **Stricter chain convergence**

   The extended run reached

   $$R-1=0.017309752619,$$

   but not the stricter target

   $$R-1<0.01.$$

2. **Independent cosmological datasets**

   The GEO mapping should be confronted with additional independent
   BAO, supernova, growth, weak-lensing, and other cosmological
   likelihood combinations.

3. **Alternative local-$H_0$ likelihoods**

   The sensitivity of the result to different local distance-ladder
   determinations should be quantified.

4. **Bayesian model comparison**

   The reported $\Delta\chi^2$ comparison is not a Bayesian evidence
   calculation.

   Bayesian evidence, information criteria where appropriate, and
   explicit treatment of model complexity remain future tests.

5. **Out-of-sample prediction**

   Additional observables should be predicted before being included in
   parameter estimation.

6. **Physical derivation of channel realization**

   The identification

   $$\mu_H=\eta$$

   remains a physical hypothesis of the Hubble-channel realization and
   should be derived or independently tested beyond its present
   numerical performance.

7. **Independent replication**

   External reproduction of the complete pipeline remains essential.

8. **Broader theoretical embedding**

   The relation between the GEO operator architecture and established
   relativistic field equations, perturbation theory, conservation
   principles, and fundamental dynamics requires further formal
   development.

These limitations define the next stage of the GEO research program.

---

# 15. Interpretation policy

The numerical results in this repository and its associated validation
repositories should be interpreted according to the exact experiment
that produced them.

In particular:

- $\eta=0.6$ is the canonical GEO value;
- the profile calculations show compatibility with that value but do
  not independently establish a new universal constant;
- $R=\mu^{1/3}$ is the canonical radial law;
- $\mu_H=\eta$ is the specific Hubble-channel realization tested here;
- $H_0=73.040000$ is the historical fixed-input GEO reconstruction;
- $H_{0,\mathrm{GEO}}=73.3882\pm0.5292$ is the extended MCMC posterior
  result;
- $\Delta\chi^2_{\mathrm{joint}}=-19.938923$ refers to the exact matched
  likelihood comparison documented in GEO-Cosmology-MCMC;
- the reported $\Delta\chi^2$ is not a Bayesian evidence ratio;
- the longest MCMC run is near-converged / numerically stable under the
  reported diagnostic, but did not satisfy the stricter
  $R-1<0.01$ target.

This separation is maintained to make the framework falsifiable,
auditable, and reproducible.

---

# 16. Repository ecosystem

The public GEO research program is distributed across dedicated
repositories so that theoretical development, implementation, and
numerical validation can be inspected separately.

### Main framework

**GEO — Hidden Geometry Framework**

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Framework archive:

https://doi.org/10.5281/zenodo.20225304

### Cosmological MCMC validation

**GEO Cosmology MCMC Validation**

https://github.com/LeoTorreblanca/GEO-Cosmology-MCMC

Archived release:

https://doi.org/10.5281/zenodo.22103137

### CLASS implementation

**CLASS-GEO-Lens**

https://github.com/LeoTorreblanca/CLASS-GEO-Lens

Archived release:

https://doi.org/10.5281/zenodo.20529415

### GEO Launch Kit

https://github.com/LeoTorreblanca/GEO_Launch_Kit

### Exoplanet validation

https://github.com/LeoTorreblanca/GEO-Exoplanets-Validation

### Spanish technical reconstruction

https://github.com/LeoTorreblanca/GEO-Geometria-Oculta-ESP

---

# 17. Official channels

[![X Follow](https://img.shields.io/twitter/follow/GEO_Hidden?style=for-the-badge&logo=x&logoColor=white&color=000000)](https://x.com/GEO_Hidden)

[![OSF Registration](https://img.shields.io/badge/OSF-Registration-blue?style=for-the-badge)](https://osf.io/yhdmz)

---

# 18. Repository structure

```text
scripts/  -> Reproducible GEO scripts
figures/  -> Generated plots and visual outputs
results/  -> Numerical outputs and console logs
pdf/      -> Individual technical reports
paper/    -> GEO manuscript and preprint versions
docs/     -> Mathematical and technical documentation
```

Dedicated large-scale cosmological MCMC products are maintained in
GEO-Cosmology-MCMC rather than duplicated in this repository.

---

# 19. Reproducibility

The GEO project follows a public reproducibility-oriented structure.

The main framework contains the mathematical and experimental
architecture.

Dedicated validation repositories contain the corresponding numerical
implementations, configurations, results, and diagnostic products.

For the cosmological MCMC study, the archived reproducibility package
contains:

- source and configuration hashes;
- environment information;
- dependency freeze;
- chain manifests;
- MCMC diagnostics;
- covariance matrices;
- profile-likelihood source tables;
- publication figures;
- numerical result tables;
- consistency auditing.

The archived cosmological validation release is:

**Torreblanca, Leonel (2026). GEO Cosmology MCMC Validation. Zenodo.**

https://doi.org/10.5281/zenodo.22103137

---

# 20. Citation

When referring to the general GEO framework, use the principal
framework archive and associated paper record.

📄 **Framework / Paper:**

https://doi.org/10.17605/OSF.IO/YHDMZ

💻 **Framework Code:**

https://doi.org/10.5281/zenodo.20225304

When referring specifically to the cosmological MCMC result, cite:

**Torreblanca, Leonel (2026). GEO Cosmology MCMC Validation. Version
1.0.0. Zenodo.**

https://doi.org/10.5281/zenodo.22103137

When referring specifically to the CLASS-GEO-Lens implementation, use:

https://doi.org/10.5281/zenodo.20529415

---

# 21. License

Unless otherwise indicated for third-party materials or external
datasets, the public GEO software and repository materials are released
under the MIT License.

See the corresponding `LICENSE` files in each repository.

External cosmological likelihoods and observational datasets retain
their original licenses, citations, and distribution conditions.

---

# 22. Scientific scope

GEO remains an open exploratory research framework.

The current results establish that the proposed geometric architecture
has generated specific, falsifiable numerical relations that can be
tested with standard cosmological inference tools.

The current cosmological analysis shows that:

$$\eta_{\mathrm{best}}\approx0.59921$$

is numerically close to the canonical

$$\eta_{\mathrm{GEO}}=0.6,$$

and that the Planck/NPIPE primitive posterior

$$H_{0,\mathrm{primitive}}\approx67.72$$

is mapped by the fixed GEO operator to

$$H_{0,\mathrm{GEO}}\approx73.39\;\mathrm{km\,s^{-1}\,Mpc^{-1}}.$$

Within the exact matched likelihood configuration tested so far, the
best sampled GEO realization also gives a lower joint chi-square than
the corresponding $\Lambda$CDM + local-$H_0$ control.

These results warrant further independent testing.

They do not remove the need for stricter convergence, independent
datasets, Bayesian model comparison, theoretical derivation, and
external replication.

---

## Author

**Leonel Hernan Torreblanca**

GEO — Hidden Geometry Framework

2026
