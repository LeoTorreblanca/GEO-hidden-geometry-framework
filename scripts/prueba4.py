import math
import numpy as np

from SOP_master_test_v0 import (
    TESTS,
    OMEGA_B,
    fit_model,
    run_class,
    fs8_class,
    S8_val,
)

FC = math.sqrt(3.0 / 5.0)
ETA = FC ** 2
ALPHA = 1.0 / 3.0

ZS = [0.1, 0.3, 0.5, 0.7, 1.0]

print("\n================================================")
print("DCU v2 PREDICTION LAW")
print("fc=sqrt(3/5), eta=3/5, R=mu_eff^(1/3)")
print("================================================")

scores = []

for test in TESTS:
    print("\n\n################################################")
    print("TEST:", test["name"])
    print("################################################")

    lcdm = fit_model("LCDM", test)

    h = lcdm["h"]
    om = lcdm["Omega_m"]
    logA = lcdm["logA"]

    od = om - OMEGA_B

    mu_eff = (OMEGA_B + FC * od) / om
    R_pred = mu_eff ** ALPHA

    lcdm_cosmo, _ = run_class(h, om, logA, 1.0, "LCDM")
    dcu_cosmo, _ = run_class(h, om, logA, FC, "SOP")

    s8_lcdm = S8_val(lcdm_cosmo, om)
    s8_dcu = S8_val(dcu_cosmo, om)

    s8_pred = s8_lcdm * R_pred

    print("\nGEOMETRIA")
    print("fc                  =", FC)
    print("f_out               =", 1.0 - FC)
    print("eta=fc^2            =", ETA)
    print("Omega_m             =", om)
    print("Omega_b             =", OMEGA_B)
    print("Omega_d             =", od)
    print("mu_eff              =", mu_eff)
    print("R_pred=mu^(1/3)     =", R_pred)

    print("\nS8")
    print("S8 LCDM             =", s8_lcdm)
    print("S8 DCU CLASS        =", s8_dcu)
    print("S8 DCU predicho     =", s8_pred)
    print("ratio CLASS         =", s8_dcu / s8_lcdm)
    print("ratio predicho      =", R_pred)
    print("error relativo      =", abs(s8_dcu - s8_pred) / s8_dcu)

    print("\nfσ8 por redshift")
    errors = []

    for z in ZS:
        fs8_lcdm = fs8_class(lcdm_cosmo, z)
        fs8_dcu = fs8_class(dcu_cosmo, z)

        fs8_pred = fs8_lcdm * R_pred

        ratio_class = fs8_dcu / fs8_lcdm
        rel_err = abs(fs8_dcu - fs8_pred) / fs8_dcu
        errors.append(rel_err)

        print(
            f"z={z:.1f}  "
            f"LCDM={fs8_lcdm:.6f}  "
            f"DCU_CLASS={fs8_dcu:.6f}  "
            f"DCU_pred={fs8_pred:.6f}  "
            f"ratio_class={ratio_class:.6f}  "
            f"ratio_pred={R_pred:.6f}  "
            f"err={100*rel_err:.3f}%"
        )

    mean_err = np.mean(errors)
    max_err = np.max(errors)

    s8_err = abs(s8_dcu - s8_pred) / s8_dcu

    total_score = math.exp(-(mean_err + s8_err) / 0.03)

    print("\nRESUMEN TEST")
    print("mean fs8 error       =", mean_err)
    print("max fs8 error        =", max_err)
    print("S8 error             =", s8_err)
    print("prediction score     =", 100 * total_score)

    if total_score > 0.90:
        print("LECTURA: DCU v2 predice muy bien la respuesta CLASS.")
    elif total_score > 0.70:
        print("LECTURA: DCU v2 predice bien, con desviacion menor.")
    elif total_score > 0.50:
        print("LECTURA: DCU v2 predice parcialmente.")
    else:
        print("LECTURA: DCU v2 necesita correccion dinamica.")

    scores.append(total_score)

    lcdm_cosmo.struct_cleanup()
    lcdm_cosmo.empty()
    dcu_cosmo.struct_cleanup()
    dcu_cosmo.empty()

print("\n\n================================================")
print("RESULTADO GLOBAL DCU v2")
print("================================================")
print("score promedio =", 100 * np.mean(scores))
print("score minimo   =", 100 * np.min(scores))
print("score maximo   =", 100 * np.max(scores))

if np.mean(scores) > 0.90:
    print("VEREDICTO: La ley R=mu^(1/3) cierra fuertemente.")
elif np.mean(scores) > 0.70:
    print("VEREDICTO: La ley R=mu^(1/3) es una aproximacion fuerte.")
elif np.mean(scores) > 0.50:
    print("VEREDICTO: La ley tiene señal, pero falta una correccion.")
else:
    print("VEREDICTO: La ley no alcanza.")
# ============================================================
# PRUEBA 4 — GRÁFICOS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi

# ------------------------------------------------------------
# DATOS
# ------------------------------------------------------------

casos = ["case_1", "case_2", "case_3", "case_4", "case_5"]

fc_vals = np.array([
    0.7420,
    0.7740,
    0.7740,
    0.7403,
    0.7740
])
fout_vals = 1.0 - fc_vals

g34 = 3/4
g35 = sqrt(3/5)
gpi4 = pi/4

# ============================================================
# 1 — Predicción geométrica vs observado
# ============================================================

plt.figure(figsize=(10,6))

plt.plot(casos, fc_vals, marker='o', linewidth=3, label='fc observado')

plt.axhline(g34, linestyle='--', label='3/4')
plt.axhline(g35, linestyle='--', label='sqrt(3/5)')
plt.axhline(gpi4, linestyle='--', label='pi/4')

plt.title("PRUEBA 4 — Predicción geométrica efectiva")
plt.ylabel("fc")
plt.legend()

plt.tight_layout()
plt.savefig("results/04_DCU_prediction_law/plots/01_prediction_geometry.png")
plt.show()

# ============================================================
# 2 — Ley cuadrática efectiva
# ============================================================

eta = fc_vals**2

plt.figure(figsize=(10,6))

plt.plot(casos, eta, marker='o', linewidth=3)

plt.axhline(3/5, linestyle='--', label='3/5')

plt.title("PRUEBA 4 — Ley cuadrática eta = fc²")
plt.ylabel("eta")
plt.legend()

plt.tight_layout()
plt.savefig("results/04_DCU_prediction_law/plots/02_eta_law.png")
plt.show()

# ============================================================
# 3 — Transferencia activa/complementaria
# ============================================================

x = np.arange(len(casos))

plt.figure(figsize=(12,6))

plt.bar(x-0.2, fc_vals, width=0.4, label='fc activo')
plt.bar(x+0.2, fout_vals, width=0.4, label='f_out')

plt.xticks(x, casos, rotation=45)

plt.title("PRUEBA 4 — Transferencia activa/complementaria")
plt.ylabel("fracción")
plt.legend()

plt.tight_layout()
plt.savefig("results/04_DCU_prediction_law/plots/03_transfer_partition.png")
plt.show()

# ============================================================
# 4 — Distancia a nodos geométricos
# ============================================================

d34 = np.abs(fc_vals - g34)
d35 = np.abs(fc_vals - g35)
dpi4 = np.abs(fc_vals - gpi4)

plt.figure(figsize=(12,6))

plt.bar(x-0.25, d34, width=0.25, label='distancia 3/4')
plt.bar(x, d35, width=0.25, label='distancia sqrt(3/5)')
plt.bar(x+0.25, dpi4, width=0.25, label='distancia pi/4')

plt.xticks(x, casos, rotation=45)

plt.title("PRUEBA 4 — Distancia geométrica")
plt.ylabel("distancia absoluta")
plt.legend()

plt.tight_layout()
plt.savefig("results/04_DCU_prediction_law/plots/04_distance_nodes.png")
plt.show()

# ============================================================
# 5 — Score arquitectónico
# ============================================================

score = 1.0 - np.minimum.reduce([d34, d35, dpi4])

plt.figure(figsize=(10,6))

plt.plot(casos, score, marker='o', linewidth=3)

plt.title("PRUEBA 4 — Score arquitectónico")
plt.ylabel("score")

plt.tight_layout()
plt.savefig("results/04_DCU_prediction_law/plots/05_architecture_score.png")
plt.show()

print("\nGráficos guardados en:")
print("results/04_DCU_prediction_law/plots/")

