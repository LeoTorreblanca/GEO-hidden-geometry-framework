# GEO Release Notes

## Historical note

Earlier GEO development releases included a Hubble-specific construction
that reproduced

\[
H_0 = 73.04\ {\rm km\,s^{-1}\,Mpc^{-1}}
\]

through a realization in which the effective radial state was identified
with the canonical architectural parameter.

That realization is retained in the Git history and historical release
tags for provenance, but it is no longer part of the canonical GEO
formulation.

The general radial law is

\[
R^3=\mu_{\rm eff},
\]

or equivalently

\[
R=\mu_{\rm eff}^{1/3},
\]

where \(\mu_{\rm eff}\) is distinct from the canonical parameter
\(\eta\).

The identity

\[
\mu_{\rm eff}=\eta
\]

is therefore not a universal GEO law.

The current main branch documents the corrected framework architecture.
A dedicated corrected GEO-Hubble geometric-projection application is
maintained separately from the core framework.

Historical versions remain available through the repository Git history
and release tags.
