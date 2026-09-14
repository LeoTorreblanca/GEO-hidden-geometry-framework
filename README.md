# GEO — Hidden Geometry Framework

## Historical framework, mathematical architecture, and computational provenance

**Author:** Leonel Hernán Torreblanca  
**Project:** GEO — Hidden Geometry  
**Repository role:** Historical and architectural root of the GEO research program  
**Status:** Research / open reproducibility framework

---

# 1. Overview

GEO (Hidden Geometry) is an exploratory mathematical and computational
framework developed to investigate whether apparently scalar physical
descriptions can admit a deeper complementary, conservative, and
projective organization.

The project did not originate from the Hubble tension.

Its earliest motivation was a mathematical observation concerning the
formal similarity of two inverse-square interactions,

\[
F_C = k\frac{q_1q_2}{r^2},
\]

and

\[
F_G = G\frac{m_1m_2}{r^2},
\]

together with their different algebraic and physical behavior.

This comparison was never intended to assert an equivalence between
electromagnetism and gravity.

It instead motivated a narrower mathematical question:

> Can a quantity normally represented by a single scalar component
> conceal a complementary internal structure that becomes visible under
> a different mathematical representation?

That question initiated a sequence of exploratory models that eventually
led to the present GEO architecture.

The historical path can be summarized as

\[
\text{inverse-square-law curiosity}
\rightarrow
\text{dual representation}
\rightarrow
\text{active/complementary partition}
\rightarrow
\text{numerical recurrence}
\rightarrow
\text{geometric node}
\rightarrow
\text{GEO architecture}.
\]

This sequence records the provenance of the framework.

It is **not** a derivation of gravity from electromagnetism and should
not be interpreted as one.

---

# 2. Historical origin

## 2.1 Initial algebraic motivation

The earliest exploratory stage was developed under the name **GDD**
(*Geometría de Firma Dual Dinámica*).

A two-component algebraic representation was introduced schematically
through

\[
I = m^2-\mu^2.
\]

The purpose of this representation was exploratory.

The minus sign belongs to the mathematical representation and does not
imply negative physical mass, negative energy, antigravity, or a
repulsive gravitational sector.

GDD asked whether complementary components could reveal mathematical
structure hidden by a one-component description.

Several reformulations followed.

The importance of this stage to the current GEO project is therefore
primarily historical: it established the dual-representation question
from which the later conservative architecture developed.

---

# 3. From GDD to an active/complementary description

A later stage, developed through **GDDv2** and subsequently the
**SOP** investigations, replaced the original exploratory
representation with a simpler active/complementary partition.

Schematically,

\[
\rho_d
=
\rho_d^{\mathrm{active}}
+
\rho_d^{\mathrm{comp}},
\]

with

\[
\rho_d^{\mathrm{active}}=\xi\rho_d,
\qquad
\rho_d^{\mathrm{comp}}=(1-\xi)\rho_d.
\]

At this stage the effective coupling was treated as a quantity to be
tested numerically rather than fixed in advance.

Across several archived exploratory configurations, free fits repeatedly
occupied two numerical regions approximately around

\[
f_c \simeq 0.740-0.742
\]

and

\[
f_c \simeq 0.774088.
\]

These values preceded the later GEO-Hubble construction.

They were subsequently compared with simple geometric candidates,

\[
f_c^{\mathrm{base}}=\frac34=0.75,
\]

\[
f_c^{\mathrm{node}}=\sqrt{\frac35}
=0.774596669241483\ldots,
\]

and

\[
f_c^{\mathrm{ideal}}=\frac{\pi}{4}
=0.785398163397448\ldots.
\]

These comparisons were retrospective.

They should not be interpreted as independent out-of-sample predictions
or as measurements of fundamental constants.

Their role was to identify simple geometric structures capable of
organizing recurrent numerical behavior observed during development.

---

# 4. Canonical GEO node

The numerical recurrence near

\[
f_c\simeq0.774088
\]

motivated closer examination of

\[
f_c=\sqrt{\frac35}.
\]

The corresponding structural quantity is

\[
\boxed{
\eta=f_c^2=\frac35
}
\]

and therefore

\[
\boxed{
f_c=\sqrt{\eta}
=\sqrt{\frac35}
}.
\]

The canonical GEO structural node is consequently

\[
\eta=0.6,
\qquad
f_c=0.774596669241483\ldots
\]

with complementary fraction

\[
B=1-\eta=\frac25=0.4.
\]

An important historical distinction must be maintained:

> The value \(\eta=3/5\) was not obtained by fitting a later Hubble
> projection to a desired value of \(H_0\).

The Hubble application belongs to a later layer of the research program.

---

# 5. Current GEO mathematical architecture

The mature GEO formulation separates historical motivation,
mathematical definition, executable implementation, application
hypotheses, and empirical tests.

These levels should not be conflated.

The general conservative state is written

\[
\boxed{
A+B+L=T
}
\]

with normalized total

\[
T=1.
\]

Here:

- \(A\) denotes the active/observable partition;
- \(B\) denotes the complementary partition;
- \(L\) represents an explicit latent or loss contribution when required.

For the canonical lossless state,

\[
L=0,
\]

so that

\[
A+B=1.
\]

The canonical structural assignment is

\[
A=\eta=\frac35,
\]

\[
B=1-\eta=\frac25.
\]

Thus,

\[
\boxed{
A=\frac35,\qquad B=\frac25
}
\]

for the canonical conservative state.

---

# 6. Structural parameter and effective state are distinct

One of the most important clarifications in the current GEO
architecture is the distinction between the structural parameter
\(\eta\) and an application-dependent effective state
\(\mu_{\mathrm{eff}}\).

The general radial/effective-state relation is

\[
\boxed{
R^3=\mu_{\mathrm{eff}}
}
\]

or equivalently

\[
\boxed{
R=\mu_{\mathrm{eff}}^{1/3}.
}
\]

This is the canonical radial law used by the current framework.

In general,

\[
\boxed{
\mu_{\mathrm{eff}}\neq\eta
}
\]

unless a particular application explicitly introduces that
identification.

Therefore the expression

\[
R=\eta^{1/3}
\]

must **not** be treated as a universal GEO identity.

The structural node

\[
\eta=\frac35
\]

and the application state

\[
\mu_{\mathrm{eff}}
\]

belong to different conceptual layers.

---

# 7. Bifocal conservative organization

The conservative GEO state can be represented through two complementary
foci,

\[
F_O=A,
\]

\[
F_C=B.
\]

Their total satisfies

\[
F_O+F_C=T-L.
\]

In the lossless state,

\[
F_O+F_C=1.
\]

An admissible tangent redistribution preserves the total:

\[
\delta F_O+\delta F_C=0.
\]

The purpose of this construction is to represent complementary
organization without violating the declared conservation relation.

---

# 8. Orthogonal projective layer

The canonical two-dimensional projective transformation is represented
by

\[
\boxed{
Q=
\frac{1}{\sqrt2}
\begin{pmatrix}
1 & 1\\
-1 & 1
\end{pmatrix}
}
\]

with

\[
Q^TQ=I,
\]

and

\[
\det Q=1.
\]

The associated angle is

\[
\boxed{
\theta=\frac{\pi}{4}
}.
\]

Because \(Q\) is orthogonal, the full transformed state preserves the
Euclidean norm and admits inverse reconstruction through

\[
Q^{-1}=Q^T.
\]

This does not imply that a complete original state can be reconstructed
from one projected coordinate alone.

The distinction between complete transformed information and a single
observable projection is essential.

---

# 9. Harmonic duality

The projective layer admits the complementary harmonic pair

\[
H_O=\cos^2\theta,
\]

\[
H_C=\sin^2\theta,
\]

with

\[
H_O+H_C=1.
\]

At the canonical angle

\[
\theta=\frac{\pi}{4},
\]

one obtains

\[
H_O=H_C=\frac12.
\]

Two useful derived quantities are

\[
D_{\mathrm{bal}}=\cos(2\theta)
\]

and

\[
D_{\mathrm{coup}}
=
\frac14\sin^2(2\theta).
\]

At the canonical state,

\[
D_{\mathrm{bal}}=0,
\]

\[
D_{\mathrm{coup}}=\frac14.
\]

These quantities describe the mathematical projective/harmonic
organization of the framework.

They should not automatically be identified with physical observables.

---

# 10. Higher-dimensional transport representation

The mature GEO architecture also studies a five-dimensional transport
representation,

\[
M_5,
\]

organized mathematically as a \(3+2\) block structure.

The five coordinates are mathematical transport coordinates.

They are **not automatically five physical dimensions or five specific
physical observables**.

Any physical interpretation requires an explicit application layer.

A spectral quantity associated with the transport operator is defined by

\[
\boxed{
\Phi=\rho(M_5)
}
\]

where

\[
\rho(M_5)=\max_i|\lambda_i|
\]

is the spectral radius.

A related projection coefficient can then be constructed as

\[
\boxed{
\alpha=\frac{\Phi B}{\sqrt2}.
}
\]

The detailed closure used to construct a particular \(M_5\), including
residual-memory variables, belongs to the executable realization of the
operator and should be distinguished from the primitive conservation
identities of the framework.

---

# 11. What is structural and what is application-dependent

The following distinction is central to GEO.

## Structural definitions

Examples include

\[
A+B+L=T,
\]

\[
T=1,
\]

\[
\eta=\frac35,
\]

\[
f_c=\sqrt{\eta},
\]

the orthogonal operator \(Q\), and the spectral definition

\[
\Phi=\rho(M_5).
\]

## General response law

The effective-state relation is

\[
R^3=\mu_{\mathrm{eff}}.
\]

The value of \(\mu_{\mathrm{eff}}\) must be supplied by an application
or model layer.

## Application hypotheses

A physical application may propose a specific identification of
\(\mu_{\mathrm{eff}}\), a projected coordinate, or another GEO quantity
with a physical observable.

Such an identification is an **application hypothesis**.

It is not automatically a universal mathematical identity of GEO.

This separation is used throughout the current research program.

---

# 12. Historical computational implementation: GEO / CLASS kit

An important stage in the development of GEO was its implementation as
a modified **CLASS v3.x** computational environment.

This repository historically served as the public entry point for that
work.

The initial GEO computational kit included source modifications,
diagnostic scripts, numerical experiments, and reproducibility material
designed to explore the consequences of GEO-inspired modifications in a
standard cosmological code base.

That implementation played two important roles:

1. it provided a concrete numerical environment in which exploratory GEO
   hypotheses could be tested; and

2. it supplied numerical provenance for the transition from the earlier
   GDD/GDDv2/SOP investigations toward the later mathematical
   formalization.

The CLASS-based implementation should therefore be understood as a
historical and computational layer of the GEO research program.

It is not the definition of GEO itself.

The mathematical architecture can be studied independently of CLASS,
while cosmological applications may continue to use CLASS or other
numerical environments as explicit application layers.

Historical numerical outputs contained in earlier releases should also
not be interpreted automatically as current canonical GEO predictions.

---

# 13. GEO External Operator

The mathematical architecture has subsequently been implemented in a
separate executable project:

**GEO External Operator**

Repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

The External Operator is intended to provide a compact executable
realization of the GEO mathematical chain outside the original
cosmological development environment.

Conceptually, the implemented chain follows the structure

\[
T
\rightarrow
(A,B,L)
\rightarrow
(\eta,f_c)
\rightarrow
\mu_{\mathrm{eff}}
\rightarrow
R
\rightarrow
\text{bifocal state}
\rightarrow
Q
\rightarrow
\text{harmonic layer}
\rightarrow
M_5
\rightarrow
\Phi
\rightarrow
\alpha.
\]

Its purpose is reproducibility and mathematical auditing.

For declared inputs it can test, among other properties,

- conservation;
- the canonical coupling relation;
- the effective-state radial law;
- orthogonality;
- harmonic closure;
- norm preservation;
- inverse reconstruction;
- transport construction;
- spectral evaluation.

Successful numerical closure demonstrates consistency between the
declared equations and their executable implementation.

It does **not**, by itself, establish that a physical system must obey
the GEO mapping.

The External Operator should therefore be regarded as an executable
reference layer of the framework rather than as independent empirical
evidence for GEO.

---

# 14. GEO-Hubble as a separate application

The Hubble problem is not part of the historical origin of GEO and is
not used here to define its canonical mathematical architecture.

It is treated as a separate physical application.

The dedicated **GEO-Hubble Geometric Projection** work evaluates a
specific projective hypothesis constructed from the canonical GEO
architecture.

That separation is deliberate:

\[
\text{GEO architecture}
\rightarrow
\text{application adapter}
\rightarrow
\text{Hubble hypothesis}
\rightarrow
\text{cosmological test}.
\]

The general GEO relation remains

\[
R^3=\mu_{\mathrm{eff}},
\]

whereas a Hubble application must explicitly state whatever
application-specific effective state it proposes.

Consequently, no Hubble-channel identification should be promoted to a
universal GEO identity.

The purpose of the dedicated Hubble project is to determine what follows
when a declared projective mapping is applied and tested under specified
cosmological assumptions.

It should therefore be read as an **evaluation of a GEO projective
hypothesis**, not as the definition of the GEO framework itself.

Historical Hubble calculations previously included directly in this
repository belong to the provenance of the research program and should
not be interpreted as the current canonical formulation.

---

# 15. Separation of research layers

For clarity, the GEO research program distinguishes the following
levels.

| Layer | Role |
|---|---|
| GDD | Initial exploratory dual representation |
| GDDv2 | Reduced phenomenological representation |
| SOP | Active/complementary numerical exploration |
| GEO | Geometric consolidation and canonical structural node |
| GEO-FOUNDATIONS | Formal mathematical architecture |
| GEO / CLASS kit | Historical cosmological implementation and numerical test environment |
| GEO External Operator | Separate executable realization of the mathematical operator chain |
| GEO-Hubble | Application-specific evaluation of a projective Hubble hypothesis |
| Cosmological inference | Statistical tests performed under explicitly declared datasets, likelihoods, and priors |

These layers are related historically and computationally, but they are
not interchangeable.

In particular:

- historical numerical recurrence is not a mathematical proof;
- a mathematical definition is not empirical validation;
- executable closure is not physical confirmation;
- an application hypothesis is not a universal identity;
- a deterministic consequence of an application is not statistical
  evidence by itself;
- a likelihood improvement is not automatically a fundamental physical
  explanation.

---

# 16. Scientific interpretation

GEO should presently be understood as a developing mathematical and
computational framework.

The current architecture provides:

- a conservative active/complementary state;
- a canonical structural node;
- a general effective-state radial relation;
- bifocal organization;
- an orthogonal projective layer;
- harmonic duality;
- a higher-dimensional transport representation;
- spectral invariants;
- executable reconstruction and closure tests;
- explicit boundaries between mathematical structure and physical
  application.

The framework does not, merely from these definitions, establish a
complete theory of gravity.

It does not derive electromagnetism and gravity from one another.

It does not require negative physical mass or negative physical energy.

It does not imply that every effective state satisfies

\[
\mu_{\mathrm{eff}}=\eta.
\]

It does not identify the coordinates of the mathematical transport
operator automatically with physical observables.

Those questions require additional physical models and empirical tests.

---

# 17. Provenance and non-retroactive interpretation

GEO has evolved through several conceptual and computational stages.

For this reason, equations appearing in historical releases should be
interpreted in the context in which they were introduced.

Later mathematical definitions must not be projected backward onto
GDD or GDDv2 as though they had been present from the beginning.

Likewise, historical exploratory numerical results must not be promoted
retroactively to independent predictions.

The canonical node

\[
\eta=\frac35
\]

was motivated through the historical numerical and geometric sequence
described above and was subsequently incorporated into the mature GEO
architecture.

The current mathematical framework then gives that node a structural
role independent of any particular Hubble likelihood calculation.

This repository preserves that developmental provenance while directing
current mathematical and application-specific work to their appropriate
layers.

---

# 18. Reproducibility philosophy

The GEO project follows a separation between:

\[
\text{provenance},
\]

\[
\text{definition},
\]

\[
\text{implementation},
\]

\[
\text{application},
\]

and

\[
\text{empirical inference}.
\]

A reproducible implementation should make it possible to determine
exactly which layer a reported result belongs to.

Where possible, computational releases should therefore provide:

- explicit equations;
- fixed numerical inputs;
- source-code provenance;
- versioned dependencies;
- deterministic regression tests;
- generated numerical outputs;
- clear application assumptions;
- separation between fitted and fixed quantities.

This structure is intended to make both confirmation and falsification
of individual GEO claims easier.

---

# 19. Repository role

This repository is the **historical root repository of GEO — Hidden
Geometry**.

Its purpose is to preserve and document:

1. the origin of the research question;
2. the GDD/GDDv2/SOP developmental path;
3. the numerical provenance of the canonical GEO node;
4. the transition to the current geometric architecture;
5. the original CLASS-based computational implementation;
6. the relationship between the original framework and later,
   more specialized GEO repositories.

The repository should not be interpreted as a container in which every
historical experiment represents the current canonical theory.

Specialized later work is maintained separately so that mathematical
architecture, executable implementation, and physical applications can
be audited without conflating their evidential roles.

---

# 20. Related GEO projects

## GEO-FOUNDATIONS

Formal mathematical development of the mature GEO architecture,
including conservation, effective-state structure, projective geometry,
transport operators, and mathematical closure.

## GEO External Operator

Separate executable implementation of the GEO operator architecture:

https://github.com/LeoTorreblanca/GEO-External-Operator

Its role is mathematical and computational reproducibility.

## GEO-Hubble Geometric Projection

Dedicated evaluation of a Hubble-channel projective hypothesis derived
from a declared GEO application adapter.

This project is intentionally separated from the root framework so that
the general GEO architecture does not depend on the validity of one
cosmological application.

## GEO cosmological / MCMC work

Dedicated cosmological environments test declared GEO realizations using
standard numerical and statistical tools such as CLASS and Cobaya.

These calculations constitute application-level tests rather than
definitions of the underlying mathematical framework.

---

# 21. Canonical relations at a glance

The principal relations of the current framework include

\[
\boxed{
A+B+L=T,\qquad T=1
}
\]

and, for the canonical lossless state,

\[
\boxed{
A=\eta=\frac35,
\qquad
B=1-\eta=\frac25,
\qquad
L=0.
}
\]

The canonical coupling factor is

\[
\boxed{
f_c=\sqrt{\eta}
=\sqrt{\frac35}.
}
\]

The general effective-state law is

\[
\boxed{
R^3=\mu_{\mathrm{eff}},
\qquad
R=\mu_{\mathrm{eff}}^{1/3}.
}
\]

The canonical projective operator is

\[
\boxed{
Q=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix},
\qquad
Q^TQ=I.
}
\]

The harmonic pair satisfies

\[
\boxed{
H_O=\cos^2\theta,
\qquad
H_C=\sin^2\theta,
\qquad
H_O+H_C=1.
}
\]

At

\[
\theta=\frac{\pi}{4},
\]

\[
H_O=H_C=\frac12.
\]

For the declared higher-dimensional transport operator,

\[
\boxed{
\Phi=\rho(M_5)=\max_i|\lambda_i|
}
\]

and a corresponding projection coefficient may be defined as

\[
\boxed{
\alpha=\frac{\Phi B}{\sqrt2}.
}
\]

These equations belong to different structural levels and should be
interpreted according to the definitions given above.

---

# 22. Important radial-law clarification

For avoidance of ambiguity, the current canonical radial relation is

\[
\boxed{
R=\mu_{\mathrm{eff}}^{1/3}.
}
\]

The expression

\[
R=\eta^{1/3}
\]

is not a universal GEO law.

It can occur only when a particular application explicitly chooses

\[
\mu_{\mathrm{eff}}=\eta.
\]

This distinction should be preserved in future documentation,
implementations, and application repositories.

---

# 23. Research status

GEO remains an open research program.

The mathematical architecture can be tested for internal consistency.

Its executable realizations can be tested for reproducibility.

Individual physical adapters can be tested against observations.

Those are distinct questions.

A failure of a particular application does not by itself invalidate a
mathematical identity, just as successful numerical closure of the
mathematics does not by itself establish a physical law.

The objective of the project is therefore not to collapse these levels
into a single claim, but to expose them clearly enough that each can be
examined independently.

---

# 24. Citation and historical versions

When citing GEO results, please identify the specific repository,
release, or archived version from which the result was obtained.

Because the framework has undergone substantial development, historical
releases may contain exploratory equations, numerical experiments, or
application-specific assumptions that are no longer part of the current
canonical architecture.

Version-specific citation is therefore strongly recommended.

Historical artifacts should be retained for provenance when appropriate,
but they should not be used as substitutes for the current definitions.

---

# 25. Author

**Leonel Hernán Torreblanca**  
Independent Researcher  
Buenos Aires, Argentina

GEO — Hidden Geometry

---

# 26. Summary

GEO began with a mathematical question inspired by the differing
structure of formally similar inverse-square laws.

That question produced an exploratory dual representation.

The dual representation evolved into an active/complementary numerical
framework.

Recurring numerical regions motivated comparison with simple geometric
structures.

That process led to the canonical structural node

\[
\boxed{
\eta=\frac35.
}
\]

The mature framework now separates the structural node from the general
effective state,

\[
\boxed{
R^3=\mu_{\mathrm{eff}},
}
\]

and develops conservative, projective, harmonic, and transport
operators around that distinction.

The original CLASS-based kit records an important computational stage of
this development.

The GEO External Operator provides a separate executable realization of
the mathematical architecture.

GEO-Hubble is treated separately as an evaluation of a specific
projective application hypothesis.

This separation —

\[
\boxed{
\text{history}
\rightarrow
\text{mathematics}
\rightarrow
\text{implementation}
\rightarrow
\text{application}
\rightarrow
\text{test}
}
\]

— defines the current organization of the GEO research program.
