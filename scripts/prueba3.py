import math
import numpy as np
from scipy.optimize import differential_evolution

from SOP_master_test_v0 import (
    run_class,
    fit_model,
    TESTS,
    OMEGA_B,
    chi2_bao,
    chi2_sn,
    chi2_fs8,
    chi2_s8,
    chi2_As,
    chi2_rd,
    chi2_ombh2,
    chi2_ommh2,
    S8_val,
    fs8_class,
)

# ==================================================
# CONSTANTES LEO
# ==================================================

FC_BASE = 3.0 / 4.0
FC_NODE = math.sqrt(3.0 / 5.0)
FC_IDEAL = math.pi / 4.0

LEO_MODELS = {
    "LCDM_fc_1": 1.0,
    "LEO_base_3_4": FC_BASE,
    "LEO_node_sqrt_3_5": FC_NODE,
    "LEO_ideal_pi_4": FC_IDEAL,
}

Z_DIAG = [0.1, 0.3, 0.5, 0.7, 1.0]


def classify_delta_bic(x):
    if x < -6:
        return "FUERTE A FAVOR"
    if x < -2:
        return "MODERADO A FAVOR"
    if abs(x) <= 2:
        return "EMPATE TECNICO"
    if x > 6:
        return "FUERTE EN CONTRA"
    return "MODERADO EN CONTRA"


def fixed_fc_fit(fc, test):
    bounds = [
        (0.62, 0.75),  # h
        (0.22, 0.42),  # Omega_m
        (2.8, 3.3),    # logA
    ]

    def obj(x):
        h, om, logA = x

        if om <= OMEGA_B:
            return 1e30

        try:
            cosmo, _ = run_class(h, om, logA, fc, "SOP")

            total = 0.0

            if test["use_bao"]:
                total += chi2_bao(cosmo)

            if test["use_sn"]:
                total += chi2_sn(cosmo)

            if test["use_fs8"]:
                total += chi2_fs8(cosmo)

            if test["use_s8"]:
                total += chi2_s8(cosmo, om, test["s8_obs"], test["s8_err"])

            if test["use_as"]:
                total += chi2_As(logA)

            if test["use_cmb_priors"]:
                chi_rd_val, _ = chi2_rd(cosmo)
                total += chi_rd_val
                total += chi2_ombh2(h)
                total += chi2_ommh2(h, om)

            cosmo.struct_cleanup()
            cosmo.empty()

            return float(total)

        except Exception:
            return 1e30

    res = differential_evolution(
        obj,
        bounds,
        seed=123,
        polish=True,
        tol=1e-4,
        maxiter=test["maxiter"],
        popsize=test["popsize"]
    )

    h, om, logA = res.x
    cosmo, A_s = run_class(h, om, logA, fc, "SOP")

    parts = {}
    parts["BAO"] = chi2_bao(cosmo) if test["use_bao"] else 0.0
    parts["SN"] = chi2_sn(cosmo) if test["use_sn"] else 0.0
    parts["fs8"] = chi2_fs8(cosmo) if test["use_fs8"] else 0.0
    parts["S8"] = chi2_s8(cosmo, om, test["s8_obs"], test["s8_err"]) if test["use_s8"] else 0.0
    parts["As"] = chi2_As(logA) if test["use_as"] else 0.0

    chi_rd_val, rd = chi2_rd(cosmo)
    parts["rd"] = chi_rd_val if test["use_cmb_priors"] else 0.0
    parts["ombh2"] = chi2_ombh2(h) if test["use_cmb_priors"] else 0.0
    parts["ommh2"] = chi2_ommh2(h, om) if test["use_cmb_priors"] else 0.0

    chi_total = sum(parts.values())

    od = om - OMEGA_B
    mu_eff = (OMEGA_B + fc * od) / om
    omega_growth = mu_eff * om

    n = 0
    if test["use_bao"]:
        n += 13
    if test["use_sn"]:
        n += 1701
    if test["use_fs8"]:
        n += 21
    if test["use_s8"]:
        n += 1
    if test["use_as"]:
        n += 1
    if test["use_cmb_priors"]:
        n += 3

    k = 3  # h, Omega_m, logA; fc fijo NO cuenta como parámetro libre
    AIC = chi_total + 2 * k
    BIC = chi_total + k * np.log(max(n, 2))

    fs8_pred = {z: fs8_class(cosmo, z) for z in Z_DIAG}

    result = {
        "fc": float(fc),
        "f_out": float(1.0 - fc),
        "eta": float(fc ** 2),
        "strain_to_node": float(FC_NODE - fc),
        "strain_to_ideal": float(FC_IDEAL - fc),
        "H0": float(100 * h),
        "h": float(h),
        "Omega_m": float(om),
        "Omega_b": float(OMEGA_B),
        "Omega_d": float(od),
        "logA": float(logA),
        "A_s": float(A_s),
        "sigma8": float(cosmo.sigma8()),
        "S8": float(S8_val(cosmo, om)),
        "rd": float(rd),
        "mu_eff": float(mu_eff),
        "Omega_growth": float(omega_growth),
        "chi_total": float(chi_total),
        "AIC": float(AIC),
        "BIC": float(BIC),
        "fs8_pred": fs8_pred,
        **{f"chi_{k}": float(v) for k, v in parts.items()}
    }

    cosmo.struct_cleanup()
    cosmo.empty()

    return result


def print_result(name, r, ref_lcdm=None, ref_sop=None):
    print("\nModelo:", name)
    print("fc                 =", r["fc"])
    print("f_out              =", r["f_out"])
    print("eta=fc^2           =", r["eta"])
    print("strain_to_node     =", r["strain_to_node"])
    print("strain_to_ideal    =", r["strain_to_ideal"])
    print("H0                 =", r["H0"])
    print("Omega_m            =", r["Omega_m"])
    print("Omega_growth       =", r["Omega_growth"])
    print("mu_eff             =", r["mu_eff"])
    print("logA               =", r["logA"])
    print("sigma8             =", r["sigma8"])
    print("S8                 =", r["S8"])
    print("rd                 =", r["rd"])
    print("chi_total          =", r["chi_total"])
    print("chi_BAO            =", r["chi_BAO"])
    print("chi_SN             =", r["chi_SN"])
    print("chi_fs8            =", r["chi_fs8"])
    print("chi_S8             =", r["chi_S8"])
    print("chi_As             =", r["chi_As"])
    print("chi_rd             =", r["chi_rd"])
    print("chi_ombh2          =", r["chi_ombh2"])
    print("chi_ommh2          =", r["chi_ommh2"])
    print("AIC                =", r["AIC"])
    print("BIC                =", r["BIC"])

    if ref_lcdm is not None:
        dbic = r["BIC"] - ref_lcdm["BIC"]
        print("Delta BIC vs LCDM  =", dbic, classify_delta_bic(dbic))

    if ref_sop is not None:
        dbic_sop = r["BIC"] - ref_sop["BIC"]
        print("Delta BIC vs SOP libre =", dbic_sop, classify_delta_bic(dbic_sop))

    print("fσ8 predictions:")
    for z, val in r["fs8_pred"].items():
        print(f"  z={z:.1f}  fσ8={val:.6f}")


print("\n================================================")
print("LEO ARCHITECTURE STRONG TEST")
print("fc fijo geométrico vs SOP libre vs MU libre vs LCDM")
print("================================================")

final_summary = []

for test in TESTS:
    print("\n\n################################################")
    print("TEST:", test["name"])
    print("################################################")

    # Referencias con fc libre / mu libre
    lcdm_free = fit_model("LCDM", test)
    sop_free = fit_model("SOP", test)
    mu_free = fit_model("MU_LIBRE", test)

    fixed = {}
    for name, fc in LEO_MODELS.items():
        print("Corriendo fijo:", name, "fc=", fc)
        fixed[name] = fixed_fc_fit(fc, test)

    best_fixed_name, best_fixed = min(fixed.items(), key=lambda kv: kv[1]["BIC"])

    print("\n==============================")
    print("REFERENCIAS LIBRES")
    print("==============================")
    print("LCDM libre BIC      =", lcdm_free["BIC"])
    print("SOP libre BIC       =", sop_free["BIC"])
    print("SOP libre fc        =", sop_free["fc"])
    print("SOP libre eta       =", sop_free["fc"] ** 2)
    print("MU libre BIC        =", mu_free["BIC"])
    print("MU libre xi_equiv   =", mu_free["xi_equiv"])

    print("\n==============================")
    print("MODELOS LEO FIJOS")
    print("==============================")
    for name, r in fixed.items():
        print_result(name, r, ref_lcdm=fixed["LCDM_fc_1"], ref_sop=sop_free)

    print("\n==============================")
    print("DIAGNOSTICO ARQUITECTONICO")
    print("==============================")
    print("Mejor fijo =", best_fixed_name)
    print("BIC mejor fijo =", best_fixed["BIC"])
    print("Delta BIC mejor fijo vs LCDM fijo =", best_fixed["BIC"] - fixed["LCDM_fc_1"]["BIC"])
    print("Delta BIC mejor fijo vs SOP libre =", best_fixed["BIC"] - sop_free["BIC"])
    print("Delta BIC node vs SOP libre =", fixed["LEO_node_sqrt_3_5"]["BIC"] - sop_free["BIC"])
    print("Delta BIC base vs SOP libre =", fixed["LEO_base_3_4"]["BIC"] - sop_free["BIC"])
    print("Delta BIC ideal vs SOP libre =", fixed["LEO_ideal_pi_4"]["BIC"] - sop_free["BIC"])

    # Ratio de energía: cuánto se acerca eta a 0.6
    node = fixed["LEO_node_sqrt_3_5"]
    print("Node eta error vs 0.6 =", node["eta"] - 0.6)

    # Interpretación del patrón
    if abs(fixed["LEO_node_sqrt_3_5"]["BIC"] - sop_free["BIC"]) <= 2:
        verdict_node = "NODE SOBREVIVE: sqrt(3/5) puede reemplazar a fc libre dentro de empate técnico."
    else:
        verdict_node = "NODE TENSIONADO: sqrt(3/5) pierde contra fc libre."

    if abs(fixed["LEO_base_3_4"]["BIC"] - sop_free["BIC"]) <= 2:
        verdict_base = "BASE SOBREVIVE: 3/4 puede reemplazar a fc libre dentro de empate técnico."
    else:
        verdict_base = "BASE TENSIONADO: 3/4 pierde contra fc libre."

    print(verdict_node)
    print(verdict_base)

    final_summary.append({
        "test": test["name"],
        "sop_fc": sop_free["fc"],
        "sop_eta": sop_free["fc"] ** 2,
        "sop_BIC": sop_free["BIC"],
        "lcdm_fixed_BIC": fixed["LCDM_fc_1"]["BIC"],
        "best_fixed": best_fixed_name,
        "best_fixed_BIC": best_fixed["BIC"],
        "delta_best_fixed_lcdm": best_fixed["BIC"] - fixed["LCDM_fc_1"]["BIC"],
        "delta_node_sop": fixed["LEO_node_sqrt_3_5"]["BIC"] - sop_free["BIC"],
        "delta_base_sop": fixed["LEO_base_3_4"]["BIC"] - sop_free["BIC"],
        "delta_ideal_sop": fixed["LEO_ideal_pi_4"]["BIC"] - sop_free["BIC"],
        "node_S8": fixed["LEO_node_sqrt_3_5"]["S8"],
        "node_mu": fixed["LEO_node_sqrt_3_5"]["mu_eff"],
        "node_Omega_growth": fixed["LEO_node_sqrt_3_5"]["Omega_growth"],
    })


print("\n\n================================================")
print("TABLA FINAL LEO ARCHITECTURE STRONG TEST")
print("================================================")

for s in final_summary:
    print("\nTEST:", s["test"])
    print("SOP libre fc              =", s["sop_fc"])
    print("SOP libre eta             =", s["sop_eta"])
    print("Mejor fijo                =", s["best_fixed"])
    print("Delta BIC mejor fijo-LCDM =", s["delta_best_fixed_lcdm"])
    print("Delta BIC node-SOP libre  =", s["delta_node_sop"])
    print("Delta BIC base-SOP libre  =", s["delta_base_sop"])
    print("Delta BIC ideal-SOP libre =", s["delta_ideal_sop"])
    print("Node S8                   =", s["node_S8"])
    print("Node mu_eff               =", s["node_mu"])
    print("Node Omega_growth         =", s["node_Omega_growth"])

print("\nLECTURA FINAL:")
print("- Si Delta BIC node-SOP libre está entre -2 y +2, LEO_node reemplaza al parámetro libre.")
print("- Si además node mejora a LCDM, hay señal arquitectónica fuerte.")
print("- Si base gana en growth y node gana en full, aparece transición estabilidad-transferencia.")
print("- Si ideal pi/4 pierde pero queda cerca, pi/4 puede ser límite ideal deformado.")
print("- Si todo fijo pierde fuerte, LEO geométrico no alcanza.")
# ==================================================
# PRUEBA 3 — GRAFICOS ARQUITECTURA FUERTE GEO/LEO
# ==================================================

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import math
import os

PLOT_DIR = "results/03_architecture_strong_test/plots"
os.makedirs(PLOT_DIR, exist_ok=True)

print("\n\nGenerando gráficos PRUEBA 3...")

# ==================================================
# RECUPERACION FLEXIBLE DE VARIABLES
# ==================================================

def get_array(possible_names, fallback):
    for name in possible_names:
        if name in globals():
            try:
                return np.array(globals()[name], dtype=float)
            except Exception:
                pass
    return np.array(fallback, dtype=float)

def get_labels():
    for name in ["labels", "test_labels", "names"]:
        if name in globals():
            try:
                return list(globals()[name])
            except Exception:
                pass
    if "rows" in globals():
        try:
            return [str(x.get("label", x.get("test", i))) for i, x in enumerate(rows)]
        except Exception:
            pass
    return ["case_1", "case_2", "case_3", "case_4", "case_5"]

labels_arr = get_labels()

fc_arr = get_array(
    ["fc_values", "fcs", "fc_arr"],
    [0.7420643869843139, 0.7740884146731773, 0.7740884146731773, 0.7403502915720953, 0.7740884146731773]
)

fout_arr = 1.0 - fc_arr

# eta = fc^2
eta_arr = fc_arr ** 2

# candidatos geométricos
fc_geom = math.sqrt(3.0 / 5.0)
eta_geom = 3.0 / 5.0
fc_low = 3.0 / 4.0
fc_pi = math.pi / 4.0

# Si el script define scores/errores propios, los toma; si no, calcula distancias.
score_arr = get_array(
    ["scores", "score_values", "geometry_scores", "leo_scores"],
    1.0 - np.abs(fc_arr - fc_geom)
)

distance_geom = np.abs(fc_arr - fc_geom)
distance_low = np.abs(fc_arr - fc_low)
distance_pi = np.abs(fc_arr - fc_pi)

x = np.arange(len(fc_arr))

# ==================================================
# 1) fc en banda arquitectónica
# ==================================================

plt.figure(figsize=(11, 6))

plt.plot(labels_arr, fc_arr, "o-", linewidth=3, markersize=8, label="fc observado")

plt.axhline(fc_low, linestyle="--", label="3/4")
plt.axhline(fc_geom, linestyle="--", label="sqrt(3/5)")
plt.axhline(fc_pi, linestyle="--", label="pi/4")

plt.fill_between(
    np.arange(len(fc_arr)),
    fc_low,
    fc_geom,
    alpha=0.15,
    label="banda 3/4 → sqrt(3/5)"
)

plt.xticks(rotation=45, ha="right")
plt.ylabel("fc")
plt.title("PRUEBA 3 — Banda arquitectónica de transferencia")

plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "01_fc_architectural_band.png"), dpi=200)
plt.close()


# ==================================================
# 2) eta = fc^2
# ==================================================

plt.figure(figsize=(11, 6))

plt.plot(labels_arr, eta_arr, "o-", linewidth=3, markersize=8, label="eta = fc^2")

plt.axhline(eta_geom, linestyle="--", label="eta geométrica = 3/5")

plt.xticks(rotation=45, ha="right")
plt.ylabel("eta")
plt.title("PRUEBA 3 — Eficiencia geométrica eta = fc²")

plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "02_eta_fc_squared.png"), dpi=200)
plt.close()


# ==================================================
# 3) fc y f_out juntos
# ==================================================

plt.figure(figsize=(11, 6))

plt.bar(x - 0.2, fc_arr, width=0.4, label="fc activo")
plt.bar(x + 0.2, fout_arr, width=0.4, label="f_out complementario")

plt.xticks(x, labels_arr, rotation=45, ha="right")
plt.ylabel("fracción")
plt.title("PRUEBA 3 — Partición activa/complementaria")

plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "03_fc_fout_partition.png"), dpi=200)
plt.close()


# ==================================================
# 4) distancia a nodos
# ==================================================

plt.figure(figsize=(11, 6))

width = 0.25

plt.bar(x - width, distance_low, width=width, label="distancia a 3/4")
plt.bar(x, distance_geom, width=width, label="distancia a sqrt(3/5)")
plt.bar(x + width, distance_pi, width=width, label="distancia a pi/4")

plt.xticks(x, labels_arr, rotation=45, ha="right")
plt.ylabel("distancia absoluta")
plt.title("PRUEBA 3 — Distancia a nodos arquitectónicos")

plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "04_distance_to_nodes.png"), dpi=200)
plt.close()


# ==================================================
# 5) score arquitectónico
# ==================================================

plt.figure(figsize=(11, 6))

plt.plot(labels_arr, score_arr, "o-", linewidth=3, markersize=8)

plt.xticks(rotation=45, ha="right")
plt.ylabel("score")
plt.title("PRUEBA 3 — Score arquitectónico / cercanía geométrica")

plt.tight_layout()

plt.savefig(os.path.join(PLOT_DIR, "05_architecture_score.png"), dpi=200)
plt.close()


print("\nResumen PRUEBA 3")
print("N =", len(fc_arr))
print("fc mean =", float(np.mean(fc_arr)))
print("fc median =", float(np.median(fc_arr)))
print("fc min =", float(np.min(fc_arr)))
print("fc max =", float(np.max(fc_arr)))
print("eta mean =", float(np.mean(eta_arr)))
print("eta median =", float(np.median(eta_arr)))
print("eta geométrica 3/5 =", eta_geom)
print("distancia media a 3/4 =", float(np.mean(distance_low)))
print("distancia media a sqrt(3/5) =", float(np.mean(distance_geom)))
print("distancia media a pi/4 =", float(np.mean(distance_pi)))

print("\nGráficos PRUEBA 3 generados.")
