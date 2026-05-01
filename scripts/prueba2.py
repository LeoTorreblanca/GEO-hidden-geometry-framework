import numpy as np
import math

# ==================================================
# Valores fc obtenidos en tus corridas SOP
# ==================================================

FC_VALUES = [
    0.7420643869843139,   # 01_growth_S8
    0.7740884146731773,   # 02_BAO_SN_full
    0.7740884146731773,   # KiDS_like
    0.7403502915720953,   # DES_HSC_like
    0.7740884146731773,   # DES_Y3_like
]

LABELS = [
    "01_growth_S8",
    "02_BAO_SN_full",
    "KiDS_like",
    "DES_HSC_like",
    "DES_Y3_like",
]

# ==================================================
# Candidatos geométricos / matemáticos
# ==================================================

CANDIDATES = {
    "sqrt(3/5)": math.sqrt(3/5),
    "pi/4": math.pi / 4,
    "3/4": 3/4,
    "cos(30deg)": math.cos(math.radians(30)),
    "sqrt(2/3)": math.sqrt(2/3),
    "1/sqrt(2)": 1 / math.sqrt(2),
    "phi_inv": (math.sqrt(5) - 1) / 2,
    "2/pi": 2 / math.pi,
    "sqrt(pi)/2": math.sqrt(math.pi) / 2,
}

# ==================================================
# Funciones auxiliares
# ==================================================

def angle_from_fraction(fc):
    return 360.0 * fc

def projection_angle(fc, ideal):
    ratio = fc / ideal
    if ratio < -1 or ratio > 1:
        return np.nan
    return math.degrees(math.acos(ratio))

def volume_radius(fc):
    return fc ** (1/3)

def area_radius(fc):
    return math.sqrt(fc)

def score_candidate(values, candidate):
    diffs = np.array(values) - candidate
    abs_diffs = np.abs(diffs)
    rel_diffs = abs_diffs / candidate
    rmse = math.sqrt(np.mean(diffs**2))
    mae = np.mean(abs_diffs)
    maxerr = np.max(abs_diffs)
    return rmse, mae, maxerr, np.mean(rel_diffs)

# ==================================================
# Análisis general
# ==================================================

fc = np.array(FC_VALUES)
fout = 1.0 - fc

print("\n================================================")
print("SOP v2 — Análisis geométrico de fc")
print("================================================")

print("\nValores SOP observados:")
for lab, val in zip(LABELS, FC_VALUES):
    print(f"{lab:20s} fc={val:.15f}  f_out={1-val:.15f}  angle={angle_from_fraction(val):.3f}°")

print("\nResumen estadístico:")
print("N                  =", len(fc))
print("fc mean            =", np.mean(fc))
print("fc median          =", np.median(fc))
print("fc std             =", np.std(fc, ddof=1))
print("fc min             =", np.min(fc))
print("fc max             =", np.max(fc))
print("f_out mean         =", np.mean(fout))
print("f_out min/max      =", np.min(fout), np.max(fout))
print("activo:afuera mean =", np.mean(fc / fout))

# ==================================================
# Comparación con candidatos
# ==================================================

print("\n================================================")
print("Comparación contra candidatos")
print("================================================")

rows = []
for name, cand in CANDIDATES.items():
    rmse, mae, maxerr, mean_rel = score_candidate(fc, cand)
    rows.append((rmse, mae, maxerr, mean_rel, name, cand))

rows.sort(key=lambda x: x[0])

print("Ranking por RMSE:")
print("candidato        valor          RMSE          MAE           max_err       rel_mean")
for rmse, mae, maxerr, mean_rel, name, cand in rows:
    print(f"{name:14s} {cand:.12f}  {rmse:.9f}  {mae:.9f}  {maxerr:.9f}  {mean_rel:.6f}")

# ==================================================
# Comparación específica sqrt(3/5) vs pi/4
# ==================================================

sqrt35 = math.sqrt(3/5)
pi4 = math.pi / 4

print("\n================================================")
print("Foco: sqrt(3/5) vs pi/4")
print("================================================")

for lab, val in zip(LABELS, FC_VALUES):
    d_sqrt = val - sqrt35
    d_pi = val - pi4

    print(f"\n{lab}")
    print(f"fc                   = {val:.15f}")
    print(f"diff vs sqrt(3/5)    = {d_sqrt:+.15f}")
    print(f"abs diff sqrt(3/5)   = {abs(d_sqrt):.15f}")
    print(f"rel diff sqrt(3/5)   = {abs(d_sqrt)/sqrt35:.6%}")
    print(f"diff vs pi/4         = {d_pi:+.15f}")
    print(f"abs diff pi/4        = {abs(d_pi):.15f}")
    print(f"rel diff pi/4        = {abs(d_pi)/pi4:.6%}")

    alpha_pi = projection_angle(val, pi4)
    alpha_sqrt = projection_angle(val, sqrt35)

    print(f"projection angle if ideal=pi/4      = {alpha_pi:.6f}°")
    print(f"projection angle if ideal=sqrt(3/5) = {alpha_sqrt:.6f}°")

# ==================================================
# Geometría derivada: área/radio/volumen
# ==================================================

print("\n================================================")
print("Lecturas geométricas derivadas")
print("================================================")

print("Si fc es fracción de área: r/R = sqrt(fc)")
print("Si fc es fracción de volumen: r/R = fc^(1/3)")
print("Si fc es fracción angular: theta = 360*fc")

for lab, val in zip(LABELS, FC_VALUES):
    print(f"\n{lab}")
    print(f"fc                 = {val:.12f}")
    print(f"theta activo       = {angle_from_fraction(val):.6f}°")
    print(f"theta fuera        = {angle_from_fraction(1-val):.6f}°")
    print(f"r/R area           = {area_radius(val):.9f}")
    print(f"r/R volume         = {volume_radius(val):.9f}")
    print(f"activo/fuera       = {val/(1-val):.9f}")

# ==================================================
# Distinct aproximado
# ==================================================

print("\n================================================")
print("Distinct aproximado")
print("================================================")

rounded = {}
for lab, val in zip(LABELS, FC_VALUES):
    key = round(val, 6)
    rounded.setdefault(key, []).append(lab)

for key, labs in rounded.items():
    print(f"fc≈{key} repeticiones={len(labs)} labels={labs}")

# ==================================================
# Veredicto textual
# ==================================================

best = rows[0]
second = rows[1]

print("\n================================================")
print("Diagnóstico")
print("================================================")

print("Mejor candidato por RMSE:", best[4], "=", best[5])
print("Segundo candidato:", second[4], "=", second[5])
print("RMSE mejor:", best[0])
print("RMSE segundo:", second[0])

print("\nLectura:")
print("- Si sqrt(3/5) queda primero y muy por debajo de pi/4, la pista apunta más a nodo/partición óptima.")
print("- Si pi/4 queda cercano, la intuición círculo/cuadrado/anillo sigue siendo una buena lectura geométrica.")
print("- Si 3/4 queda competitivo, la explicación puede ser simplemente partición 75/25 efectiva.")
print("- Esto no prueba una geometría; ayuda a elegir qué hipótesis geométrica merece test físico posterior.")
# ==================================================
# PRUEBA 2 — GRAFICOS GEOMETRICOS GEO
# ==================================================

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import math
import os

PLOT_DIR = "results/02_geometric_node_analysis/plots"
os.makedirs(PLOT_DIR, exist_ok=True)

print("\n\nGenerando gráficos PRUEBA 2...")


# ==================================================
# RECUPERACION FLEXIBLE VARIABLES
# ==================================================

try:
    fc_arr = np.array(fc_values, dtype=float)
except:
    try:
        fc_arr = np.array(fcs, dtype=float)
    except:
        try:
            fc_arr = np.array([x["fc"] for x in rows], dtype=float)
        except:
            fc_arr = np.array([
                0.7420643869843139,
                0.7740884146731773,
                0.7740884146731773,
                0.7403502915720953,
                0.7740884146731773,
            ])

try:
    labels_arr = list(labels)
except:
    try:
        labels_arr = [x["label"] for x in rows]
    except:
        labels_arr = [
            "growth_S8",
            "BAO_SN",
            "KiDS",
            "DES_HSC",
            "DES_Y3",
        ]


fout_arr = 1.0 - fc_arr

candidates = {
    "3/4": 3.0/4.0,
    "sqrt(3/5)": math.sqrt(3.0/5.0),
    "pi/4": math.pi/4.0
}

x = np.arange(len(fc_arr))


# ==================================================
# 1) fc observado vs candidatos
# ==================================================

plt.figure(figsize=(11,6))

plt.plot(labels_arr, fc_arr, "o-", linewidth=3, markersize=8)

for name, val in candidates.items():
    plt.axhline(val, linestyle="--", label=f"{name} = {val:.6f}")

plt.xticks(rotation=45, ha="right")

plt.ylabel("fc")
plt.title("PRUEBA 2 — fc observado vs candidatos geométricos")

plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "01_fc_vs_candidates.png"), dpi=200)

plt.close()


# ==================================================
# 2) distancia absoluta
# ==================================================

plt.figure(figsize=(11,6))

width = 0.25

for i, (name, val) in enumerate(candidates.items()):

    dist = np.abs(fc_arr - val)

    plt.bar(
        x + (i - 1)*width,
        dist,
        width=width,
        label=name
    )

plt.xticks(x, labels_arr, rotation=45, ha="right")

plt.ylabel("|fc - candidato|")

plt.title("PRUEBA 2 — Distancia absoluta a candidatos")

plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "02_distance_candidates.png"), dpi=200)

plt.close()


# ==================================================
# 3) fc vs f_out
# ==================================================

plt.figure(figsize=(8,6))

plt.scatter(fc_arr, fout_arr, s=100)

for i, lab in enumerate(labels_arr):

    plt.annotate(
        lab,
        (fc_arr[i], fout_arr[i]),
        fontsize=8
    )

plt.xlabel("fc")

plt.ylabel("f_out")

plt.title("PRUEBA 2 — Dualidad activa/complementaria")

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "03_fc_vs_fout.png"), dpi=200)

plt.close()


# ==================================================
# 4) histograma fc
# ==================================================

plt.figure(figsize=(9,6))

plt.hist(fc_arr, bins=5, edgecolor="black")

plt.axvline(3.0/4.0, linestyle="--", label="3/4")
plt.axvline(math.sqrt(3.0/5.0), linestyle="--", label="sqrt(3/5)")
plt.axvline(math.pi/4.0, linestyle="--", label="pi/4")

plt.xlabel("fc")

plt.ylabel("frecuencia")

plt.title("PRUEBA 2 — Distribución geométrica de fc")

plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "04_hist_fc.png"), dpi=200)

plt.close()


# ==================================================
# 5) ranking RMSE candidatos
# ==================================================

names = list(candidates.keys())

rmse_vals = [
    math.sqrt(np.mean((fc_arr - candidates[n])**2))
    for n in names
]

plt.figure(figsize=(8,6))

plt.bar(names, rmse_vals)

plt.ylabel("RMSE")

plt.title("PRUEBA 2 — Ranking geométrico")

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "05_rmse_candidates.png"), dpi=200)

plt.close()


print("\nResumen PRUEBA 2")

print("N =", len(fc_arr))

print("fc mean =", float(np.mean(fc_arr)))
print("fc median =", float(np.median(fc_arr)))
print("fc min =", float(np.min(fc_arr)))
print("fc max =", float(np.max(fc_arr)))

for name, val in candidates.items():

    rmse = math.sqrt(np.mean((fc_arr - val)**2))
    mae  = float(np.mean(np.abs(fc_arr - val)))

    print(f"{name}: valor={val}, RMSE={rmse}, MAE={mae}")

print("\nGráficos PRUEBA 2 generados.")
