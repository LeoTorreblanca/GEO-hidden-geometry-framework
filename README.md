# GEO — Hidden Geometry Framework

## Mathematical origin, geometric architecture, and computational development

**Author:** Leonel Hernán Torreblanca  
**Project:** GEO — Hidden Geometry  
**Repository role:** Historical and architectural root of the GEO research program  
**Status:** Open research and reproducibility framework

---

## 1. Overview

GEO — Hidden Geometry is an exploratory mathematical and computational
research program developed from a question about complementary
representations, conservation, projection, and geometric structure.

The framework did not begin from a cosmological target.

Its origin was a formal mathematical observation: Newtonian gravitation
and Coulomb interaction possess closely related inverse-square forms,

$$
F_G = G\frac{m_1m_2}{r^2},
$$

and

$$
F_C = k\frac{q_1q_2}{r^2},
$$

while their source variables and physical interpretations are different.

This similarity was used only as mathematical inspiration.

GEO does **not** assert that gravity and electromagnetism are the same
interaction, nor that one is derived from the other.

The motivating question was instead:

> Can a scalar description conceal a complementary internal structure
> that becomes visible under a different mathematical representation?

That question initiated a sequence of exploratory models, numerical
experiments, and geometric reformulations that eventually led to the
current GEO architecture.

The historical development can be summarized as

$$
\text{formal inverse-square comparison}
\rightarrow
\text{dual representation}
\rightarrow
\text{active/complementary partition}
\rightarrow
\text{numerical recurrence}
\rightarrow
\text{geometric interpretation}
\rightarrow
\text{GEO}.
$$

### Core result — GEO Geometric Efficiency Law

The central mathematical result of the mature GEO architecture is the
**GEO Geometric Efficiency Law (GEL)**.

GEL organizes the framework as a closed five-stage transformation:

$$
\boxed{
\text{conservative state}
\rightarrow
\text{effective-state geometrization}
\rightarrow
\text{projective/harmonic organization}
\rightarrow
\text{transport and spectral evaluation}
\rightarrow
\text{reconstruction and closure}
}
$$

In executable form, the chain is

$$
(\eta,L,\mu_{\mathrm{eff}})
\rightarrow
R
\rightarrow
\text{geometric state}
\rightarrow
\text{projection}
\rightarrow
M_5
\rightarrow
\Phi
\rightarrow
\alpha
\rightarrow
\text{reconstruction}.
$$

The contribution of GEL is not any individual operation in isolation.
Normalization, orthogonal projection, harmonic identities, eigenvalues,
spectral radius, and inverse reconstruction are established mathematical
tools.

The GEO result is their explicit ordered composition into a conservative
operator chain in which structural, effective-state, projective, transport,
spectral, and reconstructed quantities remain separately identifiable and
the final state can be tested for closure.

The five stages are:

1. **Conservation**
   $$
   A+B+L=1.
   $$

2. **Effective-state geometrization**
   $$
   R^3=\mu_{\mathrm{eff}},
   \qquad
   \mu_{\mathrm{eff}}\neq\eta
   \quad\text{in general}.
   $$

3. **Projective and harmonic organization**
   $$
   \mathbf v'=Q\mathbf v,
   \qquad
   Q^TQ=I,
   $$
   together with the complementary harmonic representation.

4. **Transport and spectral evaluation**
   $$
   \Phi=\rho(M_5),
   \qquad
   \alpha=\frac{\Phi B}{\sqrt2}.
   $$

5. **Reconstruction and closure**
   $$
   \widehat{\mathbf v}=Q^T\mathbf v',
   $$
   with numerical closure evaluated by the difference between the
   reconstructed and supplied states.

The term **Geometric Efficiency Law** refers here to this closed
mathematical transformation internal to GEO. It is not, by itself, a claim
of an empirically established universal law of nature. Any physical
application requires an independently justified mapping to observables and
corresponding empirical tests.
---

## 2. Initial mathematical exploration

The earliest stage of the research was developed through an exploratory
dual representation later referred to as **GDD**.

A representative quantity was written as

$$
I = m^2-\mu^2.
$$

The objective was to investigate whether a quantity normally treated
through one effective component could admit a complementary
representation while preserving a meaningful invariant structure.

The minus sign in this expression belongs to the mathematical
representation.

It does not imply negative physical mass, negative energy, antigravity,
or a repulsive gravitational sector.

The importance of this stage is historical and methodological: it
introduced the complementary-representation question that later evolved
into the GEO framework.

---

## 3. GDDv2 and the active/complementary partition

The initial representation was subsequently simplified and tested
numerically.

In later GDDv2 and SOP investigations, the description was organized
through an active and complementary partition of an effective sector,

$$
\rho_d=\rho_d^{\mathrm{active}}+\rho_d^{\mathrm{comp}},
$$

with

$$\rho_d^{\mathrm{active}}=\xi\rho_d,$$

and

$$\rho_d^{\mathrm{comp}}=(1-\xi)\rho_d.$$

At this stage the effective coupling was not fixed geometrically in
advance.

It was explored numerically.

Several archived configurations repeatedly produced values in narrow
regions approximately around

$$
f_c \simeq 0.740-0.742
$$

and

$$
f_c \simeq 0.774088.
$$

These numerical recurrences motivated a later geometric comparison.

They were not originally introduced as exact constants.

---

## 4. From numerical recurrence to geometric candidates

The recurrent numerical regions were subsequently compared with simple
geometric values.

Three useful reference candidates were

$$
f_c^{\mathrm{base}}=\frac34=0.75,$$

$$
f_c^{\mathrm{node}}=\sqrt{\frac35}=0.774596669241483\ldots,
$$

and

$$
f_c^{\mathrm{ideal}}=\frac{\pi}{4}=0.785398163397448\ldots.
$$

The comparison was retrospective.

It should not be interpreted as an independent statistical discovery of
these constants.

Its role was to identify whether a simple geometric structure could
organize recurrent numerical behavior already observed during the
development of the framework.

The recurrence nearest

$$
\sqrt{\frac35}
$$

motivated the canonical GEO node.

---

## 5. Canonical GEO structural node

The canonical structural relation is

$$
\boxed{\eta=\frac35}
$$

with

$$
\boxed{f_c=\sqrt{\eta}=\sqrt{\frac35}}
$$

and therefore

$$
\eta=0.6,
$$

$$
f_c=0.774596669241483\ldots
$$

The complementary fraction is

$$
B=1-\eta=\frac25=0.4.
$$

Thus the canonical lossless GEO partition is

$$
\boxed{A=\frac{3}{5}}
$$

$$
\boxed{B=\frac{2}{5}}
$$

This structural node became part of the mature mathematical
architecture after the exploratory numerical stage.

---

## 6. Conservative architecture

The general normalized GEO state is written as

$$
\boxed{A+B+L=T}
$$

with

$$
T=1.
$$

Here:

- $A$ is the active/observable contribution;
- $B$ is the complementary contribution;
- $L$ is an explicit latent or loss term when required.

For the lossless case,

$$
L=0,
$$

so that

$$
\boxed{A+B=1.}
$$

For the canonical GEO state,

$$
A=\eta=\frac35,
$$

and

$$
B=1-\eta=\frac25.
$$

This conservative partition is one of the central mathematical elements
of the present framework.

---

## 7. Structural parameter and effective state

A central clarification in the mature GEO architecture is the
distinction between the structural parameter $\eta$ and the
application-dependent effective state $\mu_{\mathrm{eff}}$.

They are not the same mathematical object.

The general effective-state law is

$$
\boxed{R^3=\mu_{\mathrm{eff}}}
$$

or equivalently

$$
\boxed{R=\mu_{\mathrm{eff}}^{1/3}.}
$$

Therefore, in general,

$$
\boxed{\mu_{\mathrm{eff}}\neq\eta.}
$$

A particular application may assign equal numerical values, but such an
assignment belongs to the application.

It is not a universal GEO identity.

---

## 8. Bifocal organization

The conservative state may be represented through two complementary
foci,

$$
F_O=A,
$$

and

$$
F_C=B.
$$

Their total satisfies

$$
F_O+F_C=T-L.
$$

For the lossless state,

$$
F_O+F_C=1.
$$

An admissible redistribution preserves the total,

$$
\delta F_O+\delta F_C=0.
$$

This representation provides the basis for the projective layer of the
framework.

---

## 9. Canonical projective operator

The canonical two-dimensional GEO transformation is represented by the
orthogonal operator

$$
\boxed{Q=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}1 & 1 \cr -1 & 1\end{array}\right]}
$$

It satisfies

$$
Q^TQ=I
$$

and

$$
\det Q=1.
$$

The associated canonical angle is

$$
\boxed{\theta=\frac{\pi}{4}.}
$$

For a conservative vector

$$
\mathbf{v}=(A,B)^T
$$

the projected state is

$$
\mathbf v'=Q\mathbf v.
$$

The first projected coordinate is therefore

$$
A'=\frac{A+B}{\sqrt{2}}
$$

For the lossless normalized state,

$$
A+B=1,
$$

which gives

$$
\boxed{A'=\frac1{\sqrt2}.}
$$

The complete orthogonal transformation preserves norm and admits inverse
reconstruction through

$$
Q^{-1}=Q^T.
$$

---

## 10. Projection and reconstruction

The GEO projective layer distinguishes between a complete transformed
state and a single projected coordinate.

The full projected pair retains the information required for inverse
reconstruction.

The observable projected coordinate alone is not assumed to uniquely
determine the full complementary state.

This distinction is important both mathematically and physically.

The current executable implementation therefore exposes:

- projected observable component;
- projected complementary component;
- latent component when present;
- reconstructed state;
- numerical closure errors.

---

## 11. Harmonic organization

A complementary harmonic representation can be written as

$$
H_O=\cos^2\theta,
$$

and

$$
H_C=\sin^2\theta.
$$

These satisfy

$$
H_O+H_C=1.
$$

At the canonical angle

$$
\theta=\frac{\pi}{4},
$$

the two contributions become

$$
H_O=H_C=\frac12.
$$

Associated quantities include

$$
D_{\mathrm{bal}}=\cos(2\theta),
$$

and

$$
D_{\mathrm{coup}}=\frac14\sin^2(2\theta).
$$

At the canonical state,

$$
D_{\mathrm{bal}}=0,
$$

and

$$
D_{\mathrm{coup}}=\frac14.
$$

These quantities describe the mathematical harmonic layer.

They should not automatically be identified with physical observables.

---

## 12. Higher-dimensional transport

The mature GEO architecture also includes a five-dimensional transport
representation,

$$
M_5.
$$

The mathematical organization is constructed as a $3+2$ structure.

These coordinates are mathematical transport coordinates.

They are not automatically five physical dimensions or five directly
measurable physical quantities.

A spectral quantity is defined by

$$
\boxed{\Phi=\rho(M_5)}
$$

where

$$
\rho(M_5)=\max_i |\lambda_i|.
$$

A related coefficient is

$$
\boxed{\alpha=\frac{\Phi B}{\sqrt2}.}
$$

The detailed realization of $M_5$ belongs to the operator layer and must
be distinguished from the primitive conservation relations.

---

## 13. Formalization of GEO

The mathematical formalization developed after the exploratory and
numerical stages.

This distinction is deliberate.

The historical sequence is not

$$
\text{axioms}\rightarrow\text{prediction}.
$$

It is better represented as

$$
\text{exploration}
\rightarrow
\text{numerical structure}
\rightarrow
\text{geometric interpretation}
\rightarrow
\text{formalization}.
$$

The later GEO-FOUNDATIONS work organizes the mature architecture into
explicit definitions, operators, conservation relations, projection
rules, effective-state relations, and reconstruction procedures.

Later formal definitions should not be projected backward onto the
earliest GDD experiments as though they had existed from the beginning.

---

## 14. Computational development: the original CLASS kit

An important stage in the development of GEO was its implementation in a
modified **CLASS v3.x** environment.

The original computational kit included:

- CLASS source modifications;
- cosmological diagnostic scripts;
- exploratory parameter studies;
- reproducibility material;
- numerical tests of active/complementary behavior.

This stage demonstrated that GEO-inspired constructions could be
implemented inside a standard cosmological numerical environment.

It also provided much of the computational provenance that preceded the
later formal mathematical architecture.

The CLASS implementation is therefore an important historical component
of the project.

It is not the definition of GEO itself.

The mathematical framework can be studied independently of CLASS.

---

## 15. GEO External Operator

The mathematical architecture is also implemented through the public

**GEO External Operator**

repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

The External Operator provides a standalone executable implementation of
the **GEO Geometric Efficiency Law**, preserving its complete five-stage
operator chain.

Its public state is based on explicit inputs such as

$$
(\eta,L,\mu_{\mathrm{eff}}).
$$

The general computational structure is

$$
(\eta,L,\mu_{\mathrm{eff}})
\rightarrow
R
\rightarrow
\text{geometric state}
\rightarrow
\text{projection}
\rightarrow
M_5
\rightarrow
\Phi
\rightarrow
\alpha
\rightarrow
\text{reconstruction}.
$$

This is the executable form of the five-stage Geometric Efficiency Law
defined in the core GEO architecture.

The operator is designed to test mathematical and computational
consistency outside the original CLASS development environment.

Successful execution demonstrates agreement between the declared
equations and their software implementation.

It does not by itself constitute empirical validation of a physical
interpretation.

---

## 16. Research layers

The GEO research program now distinguishes several levels of work.

| Layer | Role |
|---|---|
| GDD | Initial exploratory dual representation |
| GDDv2 | Reduced phenomenological development |
| SOP | Active/complementary numerical exploration |
| GEO | Geometric consolidation |
| GEO-FOUNDATIONS | Formal mathematical architecture |
| GEO / CLASS kit | Historical cosmological implementation |
| GEO External Operator | Standalone executable mathematical operator |
| Application repositories | Physical or observational hypotheses built on top of GEO |
| Statistical inference | Dataset-dependent tests of specific applications |

These layers should not be conflated.

A mathematical identity is not automatically a physical law.

A working software implementation is not automatically empirical
validation.

An application-specific mapping is not automatically a universal
framework identity.

---

## 17. Applications

GEO is intended to support explicitly declared application layers.

An application may specify:

$$
\mu_{\mathrm{eff}},
$$

an observable mapping, an external physical model, and a corresponding
validation strategy.

The general logic is

$$
\text{GEO architecture}
\rightarrow
\text{application mapping}
\rightarrow
\text{derived consequence}
\rightarrow
\text{test}.
$$

The application mapping must be justified independently.

---

## 18. GEO-Hubble geometric projection

One application currently under study is the GEO-Hubble projective
hypothesis.

This application is **not part of the historical origin or mathematical
definition of GEO**.

It asks whether a particular projective relationship derived from the
canonical GEO architecture can be meaningfully applied to a Hubble-scale
observable.

The Hubble project is therefore organized separately from the core
framework.

Its logical role is

$$
\text{GEO architecture}
\rightarrow
\text{Hubble application hypothesis}
\rightarrow
\text{numerical consequence}
\rightarrow
\text{cosmological test}.
$$

Changes to, or rejection of, that application do not alter the general
mathematical definition of the GEO operator.

Historical Hubble-specific constructions remain accessible through the
Git history and archived releases for provenance.

---

## 19. Cosmological inference

GEO has also been evaluated using conventional cosmological numerical
and statistical environments.

These studies include CLASS-based calculations and dedicated
cosmological inference workflows.

Such analyses belong to the application/testing layer.

They do not define the mathematical framework.

In particular, likelihood improvements, posterior constraints, or
parameter fits must be interpreted within the assumptions, priors,
datasets, and convergence properties of the corresponding experiment.

---

## 20. Scientific scope

At its present stage, GEO should be understood as a developing
mathematical and computational framework centered on the
**GEO Geometric Efficiency Law**, a closed five-stage transformation
connecting conservation, effective-state geometrization, projective and
harmonic organization, transport and spectral evaluation, and inverse
reconstruction with closure testing.

The framework supporting this law provides:

- a conservative active/complementary state;
- a canonical structural node;
- an application-dependent effective state;
- a radial relation;
- a bifocal representation;
- an orthogonal projective layer;
- harmonic organization;
- a higher-dimensional transport representation;
- spectral quantities;
- reconstruction and numerical closure tests.

These elements do not by themselves establish a complete theory of
gravity.

The framework does not claim that electromagnetism and gravity are the
same interaction.

It does not require negative physical mass or negative physical energy.

It does not require

$$
\mu_{\mathrm{eff}}=\eta
$$

as a universal identity.

Physical interpretation requires an explicit application layer and
empirical testing.

---

## 21. Reproducibility principle

The project separates five levels:

$$
\boxed{
\text{provenance}
\rightarrow
\text{definition}
\rightarrow
\text{implementation}
\rightarrow
\text{application}
\rightarrow
\text{test}.
}
$$

A reproducible result should make clear:

- which quantities are defined;
- which quantities are supplied;
- which quantities are derived;
- which software version was used;
- which application assumptions were introduced;
- which data or likelihoods were applied;
- which numerical tolerances were accepted.

This separation is intended to make both confirmation and falsification
of individual claims easier.

---

## 22. Repository role

This repository is the historical and architectural root of

**GEO — Hidden Geometry**.

Its purpose is to preserve and document:

1. the original mathematical motivation;
2. the GDD and GDDv2 development;
3. the SOP numerical stage;
4. the emergence of recurrent numerical structure;
5. the transition to a geometric interpretation;
6. the canonical GEO architecture;
7. the original CLASS implementation;
8. the relationship with later formal and application-specific
   repositories.

Historical experiments remain part of the provenance of the project,
but they should not automatically be interpreted as the current
canonical formulation.

---

## 23. Related projects

### GEO External Operator

Standalone executable implementation of the GEO mathematical operator:

**Repository:**  
https://github.com/LeoTorreblanca/GEO-External-Operator

**Archived release:**  
https://doi.org/10.5281/zenodo.22546033

### GEO-FOUNDATIONS

Formal mathematical development of the mature framework.

**Repository:**  
https://github.com/LeoTorreblanca/GEO-FOUNDATIONS

**Archived release:**  
https://doi.org/10.5281/zenodo.21362342

### GEO Cosmology / MCMC

Application-specific cosmological inference and reproducibility work.

**Repository:**  
https://github.com/LeoTorreblanca/GEO-Cosmology-MCMC

**Archived release:**  
https://doi.org/10.5281/zenodo.22103137

### GEO-Hubble Geometric Projection

Dedicated evaluation of a projective Hubble hypothesis derived from the
GEO architecture.

**Repository:**  
https://github.com/LeoTorreblanca/GEO-Hubble-Geometric-Projection

Application repositories are intentionally separated from the core
framework.

---

## 24. Canonical relations

The principal current GEO relations include

$$
\boxed{A+B+L=1}
$$

and, for the lossless state,

$$
\boxed{A+B=1.}
$$

The canonical structural node is

$$
\boxed{\eta=\frac35.}
$$

The associated coupling amplitude is

$$
\boxed{f_c=\sqrt{\eta}=\sqrt{\frac35}.}
$$

The complementary fraction is

$$
\boxed{B=1-\eta=\frac25.}
$$

TThe general effective-state radial law is

$$
\boxed{R^3=\mu_{\mathrm{eff}}}
$$

$$
\boxed{R=\mu_{\mathrm{eff}}^{1/3}}
$$

The canonical projective operator is

$$
\boxed{Q=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}1 & 1 \cr -1 & 1\end{array}\right]}
$$

The spectral definition is

$$
\boxed{\Phi=\rho(M_5)}
$$

A corresponding coefficient is

$$
\boxed{\alpha=\frac{\Phi B}{\sqrt{2}}}
$$

These equations belong to different layers of the architecture and
should be interpreted according to their definitions.

Within GEO, these relations are connected through the
**Geometric Efficiency Law** rather than treated as isolated identities:

$$
\boxed{
\text{conservation}
\rightarrow
\text{geometrization}
\rightarrow
\text{projection}
\rightarrow
\text{transport/spectral evaluation}
\rightarrow
\text{reconstruction/closure}
}
$$

---

## 25. Historical provenance

GEO evolved through multiple exploratory and formal stages.

For this reason, historical versions may contain:

- provisional notation;
- application-specific assumptions;
- earlier software interfaces;
- superseded physical mappings;
- exploratory numerical interpretations.

Those materials remain valuable as scientific provenance.

They should not replace the current mathematical definitions.

Version-specific citation is therefore strongly recommended.

---

## 26. Citation

Author:

**Leonel Hernán Torreblanca**  
Independent Researcher  
Buenos Aires, Argentina

Framework:

**GEO — Hidden Geometry**

Main framework archive:

https://doi.org/10.5281/zenodo.20225304

When citing a specialized GEO result, please cite the corresponding
repository or archived release associated with that result.

---

## 27. License and research status

The software components of the GEO project are released according to the
licenses included in their respective repositories.

GEO remains an open research program.

The framework is intended to make its assumptions, mathematical
relations, computational implementations, and application boundaries
explicit and reproducible.

---

## 28. Summary

GEO began from a mathematical question about whether complementary
structure could exist behind an apparently scalar representation.

That question led to exploratory dual models.

Those models evolved into active/complementary numerical experiments.

Recurring numerical regions motivated comparison with simple geometric
structures.

That process led to the canonical structural node

$$
\boxed{\eta=\frac35.}
$$

The mature architecture now distinguishes that structural parameter from
the general effective state,

$$
\boxed{R^3=\mu_{\mathrm{eff}}.}
$$

The framework develops conservative, projective, harmonic, transport,
spectral, and reconstruction layers around that distinction.

The original CLASS kit records an important computational stage.

The GEO External Operator provides a standalone executable realization
of the current mathematical architecture.

Physical applications, including GEO-Hubble, are treated separately as
explicit hypotheses to be tested rather than as definitions of the
framework itself.

The current organizational principle is therefore

$$
\boxed{\text{origin}\rightarrow\text{exploration}\rightarrow\text{geometry}\rightarrow\text{formalization}\rightarrow\text{implementation}\rightarrow\text{application}\rightarrow\text{test}.}
$$

The central mathematical result emerging from this development is the
**GEO Geometric Efficiency Law**:

$$
\boxed{
\text{conservative state}
\rightarrow
\text{effective-state geometrization}
\rightarrow
\text{projective/harmonic organization}
\rightarrow
\text{transport and spectral evaluation}
\rightarrow
\text{reconstruction and closure}
}
$$

Thus, the mature GEO framework is not defined by any one of its
mathematical relations in isolation. Its central object is the closed
operator chain connecting these stages while preserving explicit
distinctions between structural parameters, effective states, transformed
states, derived spectral quantities, and reconstructed states.

This closed chain is the **Geometric Efficiency Law of GEO**.
