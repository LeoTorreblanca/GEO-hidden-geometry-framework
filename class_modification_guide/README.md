# GEO CLASS Modification Guide

This folder documents the effective modification used during the GEO exploratory tests.

The current public release does not provide a full independent CLASS fork.

Instead, it documents the effective geometric law and the interpretation of the internal parameters used in the modified CLASS experiments.

---

## Core idea

GEO introduces an effective geometric transfer law for structure growth.

The purpose is not to replace the full Einstein-Boltzmann system, but to test whether observable growth suppression can be described by an effective geometric response.

---

## Main effective quantities

### Active transfer fraction

fc

### Complementary fraction

fout = 1 - fc

### Effective geometric efficiency

eta = fc²

### Effective response law

R = mu^(1/3)

---

## Interpretation

The modification is interpreted phenomenologically as a geometric transfer response.

In the exploratory implementation, the effective growth response is reduced through a geometric coupling parameter.

---

## Important note

This is not yet a full public CLASS fork.

Future versions should include:

- a clean CLASS patch
- exact source-code diff
- input parameter documentation
- reproducible .ini configuration files

---

## Current status

This guide documents the mathematical structure used in the exploratory GEO tests.

The numerical scripts in scripts/ reproduce the current public test series.
