from classy import Class
import numpy as np
import os, re, glob
from scipy.optimize import differential_evolution
from scipy.linalg import cho_factor, cho_solve

# ==================================================
# CONFIG
# ==================================================

GDD_ROOT = "/mnt/c/Users/leone/Desktop/GDD"
BAO_ROOT = os.path.join(GDD_ROOT, "bao_data-master")
SN_FILE = os.path.join(GDD_ROOT, "Pantheon+SH0ES.dat")
SN_COV_FILE = os.path.join(GDD_ROOT, "Pantheon+SH0ES_STAT+SYS.cov")

OMEGA_B = 0.05

S8_BASE_OBS, S8_BASE_ERR = 0.776, 0.0325
RD_OBS, RD_ERR = 147.1, 0.3
OMBH2_OBS, OMBH2_ERR = 0.0224, 0.0001
OMMH2_OBS, OMMH2_ERR = 0.143, 0.002
LOGA_OBS, LOGA_ERR = 3.044, 0.014

# Priors comprimidos weak lensing aproximados
WL_PRIORS = {
    "KiDS_like": (0.776, 0.0325),
    "DES_HSC_like": (0.759, 0.024),
    "DES_Y3_like": (0.776, 0.032),
}

FS8_DATA = [
    (0.02, 0.360, 0.040), (0.067, 0.423, 0.055),
    (0.10, 0.370, 0.130), (0.15, 0.490, 0.050),
    (0.17, 0.510, 0.060), (0.22, 0.420, 0.070),
    (0.25, 0.351, 0.058), (0.32, 0.384, 0.095),
    (0.37, 0.460, 0.038), (0.38, 0.430, 0.054),
    (0.44, 0.413, 0.080), (0.51, 0.452, 0.057),
    (0.57, 0.444, 0.038), (0.60, 0.390, 0.063),
    (0.61, 0.457, 0.052), (0.73, 0.437, 0.072),
    (0.80, 0.470, 0.080), (0.86, 0.400, 0.110),
    (1.40, 0.482, 0.116), (1.52, 0.426, 0.077),
    (1.944, 0.364, 0.106)
]

z_fs8 = np.array([x[0] for x in FS8_DATA])
fs8_obs = np.array([x[1] for x in FS8_DATA])
fs8_err = np.array([x[2] for x in FS8_DATA])


# ==================================================
# DATA LOADERS
# ==================================================

def load_pantheon():
    data = np.genfromtxt(SN_FILE, names=True, dtype=None, encoding=None)
    names = data.dtype.names

    z_col = "zHD" if "zHD" in names else ("zcmb" if "zcmb" in names else names[1])

    if "m_b_corr" in names:
        mag_col = "m_b_corr"
    elif "MU_SH0ES" in names:
        mag_col = "MU_SH0ES"
    elif "MU" in names:
        mag_col = "MU"
    else:
        raise ValueError("No encuentro columna MU/magnitud en Pantheon")

    z = np.array(data[z_col], dtype=float)
    m = np.array(data[mag_col], dtype=float)

    raw = np.loadtxt(SN_COV_FILE)
    if raw.ndim == 1:
        if int(raw[0]) == len(z):
            cov = raw[1:].reshape(len(z), len(z))
        else:
            cov = raw.reshape(len(z), len(z))
    else:
        cov = raw

    cho = cho_factor(cov, lower=True, check_finite=False)
    ones = np.ones(len(z))
    print("Pantheon cargado:", len(z))

    return z, m, cho, ones


z_sn, m_sn, cov_sn_cho, ones_sn = load_pantheon()


def read_numbers(path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.strip().startswith("#"):
                continue
            nums = re.findall(
                r"[-+]?\d*\.\d+(?:[eE][-+]?\d+)?|[-+]?\d+(?:[eE][-+]?\d+)?",
                line
            )
            if nums:
                rows.append([float(x) for x in nums])

    if not rows:
        raise ValueError("sin numeros")

    lens = [len(r) for r in rows]
    if len(set(lens)) == 1:
        arr = np.array(rows)
        if arr.shape[1] == 1:
            return arr[:, 0]
        return arr

    return np.array([x for r in rows for x in r])


def infer_z(path, mean_raw=None):
    name = os.path.basename(path).lower()
    arr = np.asarray(mean_raw) if mean_raw is not None else None

    if arr is not None and arr.ndim == 1 and len(arr) == 2:
        if 0.01 < arr[0] < 4:
            return float(arr[0])

    if arr is not None and arr.ndim == 2 and arr.shape[1] >= 2:
        z_col = arr[:, 0]
        if np.all((z_col > 0.01) & (z_col < 4)):
            return float(np.mean(z_col))

    if "bgs" in name:
        return 0.295
    if "lrg+elg" in name:
        return 0.934
    if "elg" in name:
        return 1.321
    if "qso" in name:
        return 1.484
    if "lya" in name:
        return 2.33

    return None


def parse_bao_pair(mean_path, cov_path):
    mean_raw = read_numbers(mean_path)
    cov_raw = read_numbers(cov_path)

    name = os.path.basename(mean_path).lower()
    z = infer_z(mean_path, mean_raw)

    mean_arr = np.asarray(mean_raw)
    cov_arr = np.asarray(cov_raw)

    if mean_arr.ndim == 1 and len(mean_arr) == 2 and cov_arr.ndim == 1 and len(cov_arr) == 1:
        return {
            "z": z,
            "obs": ["DV"],
            "mean": np.array([mean_arr[1]]),
            "cov": np.array([[cov_arr[0]]]),
            "name": os.path.basename(mean_path)
        }

    if mean_arr.ndim == 2 and mean_arr.shape[1] >= 2:
        mean_vec = mean_arr[:, -1]
    else:
        mean_vec = mean_arr.flatten()

    if cov_arr.ndim == 1:
        if len(cov_arr) == len(mean_vec):
            cov = np.diag(cov_arr)
        elif len(cov_arr) == len(mean_vec) ** 2:
            cov = cov_arr.reshape(len(mean_vec), len(mean_vec))
        else:
            raise ValueError("cov incompatible")
    else:
        cov = cov_arr

    if "lya" in name:
        obs = ["DH", "DM"]
    elif len(mean_vec) == 2:
        obs = ["DM", "DH"]
    elif len(mean_vec) == 1:
        obs = ["DV"]
    else:
        raise ValueError("obs no interpretable")

    return {
        "z": z,
        "obs": obs,
        "mean": mean_vec,
        "cov": cov,
        "name": os.path.basename(mean_path)
    }


def load_bao(token="desi_gaussian_bao"):
    files = glob.glob(os.path.join(BAO_ROOT, "**", "*"), recursive=True)
    files = [f for f in files if os.path.isfile(f)]

    means = [f for f in files if f.lower().endswith("_mean.txt") or f.lower().endswith("_mean")]
    covs = [f for f in files if f.lower().endswith("_cov.txt") or f.lower().endswith("_cov")]

    entries = []

    for mf in means:
        low = mf.lower()
        if token not in low:
            continue
        if "all_gccomb" in low:
            continue

        base_m = re.sub(r"_mean(\.txt)?$", "", mf, flags=re.I)

        for cf in covs:
            base_c = re.sub(r"_cov(\.txt)?$", "", cf, flags=re.I)
            if os.path.normcase(base_m) == os.path.normcase(base_c):
                try:
                    entries.append(parse_bao_pair(mf, cf))
                except Exception as e:
                    print("SKIP BAO:", os.path.basename(mf), e)
                break

    return entries


BAO = load_bao()
print("BAO DR2 puntos:", sum(len(e["mean"]) for e in BAO))


# ==================================================
# COSMO + LIKELIHOODS
# ==================================================

def run_class(h, omega_m, logA, param, model):
    A_s = np.exp(logA) / 1e10
    omega_b = OMEGA_B * h**2
    omega_cdm = (omega_m - OMEGA_B) * h**2

    if omega_cdm <= 0:
        raise ValueError("omega_cdm <= 0")

    if model == "LCDM":
        xi_gdd = 1.0
        mu_gdd = 1.0
        gdd_mode = 0
    elif model == "SOP":
        xi_gdd = param
        mu_gdd = 1.0
        gdd_mode = 0
    elif model == "MU_LIBRE":
        xi_gdd = 1.0
        mu_gdd = param
        gdd_mode = 1
    else:
        raise ValueError(model)

    cosmo = Class()
    cosmo.set({
        "h": h,
        "omega_b": omega_b,
        "omega_cdm": omega_cdm,
        "A_s": A_s,
        "n_s": 0.965,
        "tau_reio": 0.054,
        "output": "mPk",
        "P_k_max_1/Mpc": 2.0,
        "z_max_pk": 2.5,
        "xi_gdd": xi_gdd,
        "mu_gdd": mu_gdd,
        "gdd_mode": gdd_mode
    })
    cosmo.compute()
    return cosmo, A_s


def fs8_class(cosmo, z):
    return (
        cosmo.scale_independent_growth_factor_f(z)
        * cosmo.sigma8()
        * cosmo.scale_independent_growth_factor(z)
    )


def chi2_fs8(cosmo):
    pred = np.array([fs8_class(cosmo, z) for z in z_fs8])
    return float(np.sum(((fs8_obs - pred) / fs8_err) ** 2))


def S8_val(cosmo, omega_m):
    return float(cosmo.sigma8() * np.sqrt(omega_m / 0.3))


def chi2_s8(cosmo, omega_m, s8_obs, s8_err):
    return float(((S8_val(cosmo, omega_m) - s8_obs) / s8_err) ** 2)


def chi2_rd(cosmo):
    try:
        rd = float(cosmo.rs_drag())
    except Exception:
        rd = RD_OBS
    return float(((rd - RD_OBS) / RD_ERR) ** 2), rd


def chi2_ombh2(h):
    return float(((OMEGA_B * h**2 - OMBH2_OBS) / OMBH2_ERR) ** 2)


def chi2_ommh2(h, omega_m):
    return float(((omega_m * h**2 - OMMH2_OBS) / OMMH2_ERR) ** 2)


def chi2_As(logA):
    return float(((logA - LOGA_OBS) / LOGA_ERR) ** 2)


def chi2_sn(cosmo):
    dl = np.array([cosmo.luminosity_distance(float(z)) for z in z_sn])
    mu_th = 5.0 * np.log10(dl) + 25.0

    diff = m_sn - mu_th

    Cinv_d = cho_solve(cov_sn_cho, diff, check_finite=False)
    Cinv_1 = cho_solve(cov_sn_cho, ones_sn, check_finite=False)

    a = float(diff @ Cinv_d)
    b = float(diff @ Cinv_1)
    cval = float(ones_sn @ Cinv_1)

    return a - b * b / cval


def bao_predict(cosmo, z, obs, rd):
    DM = (1.0 + z) * cosmo.angular_distance(z)
    DH = 1.0 / cosmo.Hubble(z)
    DV = (z * DM * DM * DH) ** (1.0 / 3.0)

    if obs == "DM":
        return DM / rd
    if obs == "DH":
        return DH / rd
    if obs == "DV":
        return DV / rd
    raise ValueError(obs)


def chi2_bao(cosmo):
    try:
        rd = float(cosmo.rs_drag())
    except Exception:
        rd = RD_OBS

    total = 0.0
    for e in BAO:
        pred = np.array([bao_predict(cosmo, e["z"], ob, rd) for ob in e["obs"]])
        diff = e["mean"] - pred
        inv = np.linalg.pinv(e["cov"])
        total += float(diff.T @ inv @ diff)

    return total


def xi_equiv_from_mu(mu_eff, omega_m):
    od = omega_m - OMEGA_B
    if od <= 0:
        return np.nan
    return (mu_eff * omega_m - OMEGA_B) / od


# ==================================================
# FIT ENGINE
# ==================================================

def fit_model(model, test_config):
    s8_obs = test_config["s8_obs"]
    s8_err = test_config["s8_err"]

    use_bao = test_config["use_bao"]
    use_sn = test_config["use_sn"]
    use_fs8 = test_config["use_fs8"]
    use_s8 = test_config["use_s8"]
    use_as = test_config["use_as"]
    use_cmb_priors = test_config["use_cmb_priors"]

    if model == "LCDM":
        bounds = [(0.62, 0.75), (0.22, 0.42), (2.8, 3.3)]
        k = 3
    elif model == "SOP":
        bounds = [(0.62, 0.75), (0.22, 0.42), (2.8, 3.3), (0.0, 1.0)]
        k = 4
    elif model == "MU_LIBRE":
        bounds = [(0.62, 0.75), (0.22, 0.42), (2.8, 3.3), (0.0, 1.5)]
        k = 4
    else:
        raise ValueError(model)

    def unpack(x):
        if model == "LCDM":
            h, om, logA = x
            param = 1.0
        else:
            h, om, logA, param = x
        return h, om, logA, param

    def obj(x):
        h, om, logA, param = unpack(x)
        if om <= OMEGA_B:
            return 1e30

        try:
            cosmo, _ = run_class(h, om, logA, param, model)

            total = 0.0

            if use_bao:
                total += chi2_bao(cosmo)

            if use_sn:
                total += chi2_sn(cosmo)

            if use_fs8:
                total += chi2_fs8(cosmo)

            if use_s8:
                total += chi2_s8(cosmo, om, s8_obs, s8_err)

            if use_as:
                total += chi2_As(logA)

            if use_cmb_priors:
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
        maxiter=test_config["maxiter"],
        popsize=test_config["popsize"]
    )

    h, om, logA, param = unpack(res.x)
    cosmo, A_s = run_class(h, om, logA, param, model)

    parts = {}
    parts["BAO"] = chi2_bao(cosmo) if use_bao else 0.0
    parts["SN"] = chi2_sn(cosmo) if use_sn else 0.0
    parts["fs8"] = chi2_fs8(cosmo) if use_fs8 else 0.0
    parts["S8"] = chi2_s8(cosmo, om, s8_obs, s8_err) if use_s8 else 0.0
    parts["As"] = chi2_As(logA) if use_as else 0.0

    chi_rd_val, rd = chi2_rd(cosmo)
    parts["rd"] = chi_rd_val if use_cmb_priors else 0.0
    parts["ombh2"] = chi2_ombh2(h) if use_cmb_priors else 0.0
    parts["ommh2"] = chi2_ommh2(h, om) if use_cmb_priors else 0.0

    chi_total = sum(parts.values())

    if model == "LCDM":
        fc = 1.0
        mu_eff = 1.0
        xi_equiv = 1.0
    elif model == "SOP":
        fc = param
        mu_eff = (OMEGA_B + fc * (om - OMEGA_B)) / om
        xi_equiv = fc
    else:
        fc = 1.0
        mu_eff = param
        xi_equiv = xi_equiv_from_mu(mu_eff, om)

    n = 0
    if use_bao:
        n += sum(len(e["mean"]) for e in BAO)
    if use_sn:
        n += len(z_sn)
    if use_fs8:
        n += len(FS8_DATA)
    if use_s8:
        n += 1
    if use_as:
        n += 1
    if use_cmb_priors:
        n += 3

    AIC = chi_total + 2 * k
    BIC = chi_total + k * np.log(max(n, 2))

    result = {
        "model": model,
        "H0": float(100 * h),
        "h": float(h),
        "Omega_m": float(om),
        "Omega_b": float(OMEGA_B),
        "Omega_d": float(om - OMEGA_B),
        "logA": float(logA),
        "A_s": float(A_s),
        "sigma8": float(cosmo.sigma8()),
        "S8": S8_val(cosmo, om),
        "rd": float(rd),
        "fc": float(fc),
        "f_out": float(1.0 - fc) if model == "SOP" else 0.0,
        "mu_eff": float(mu_eff),
        "xi_equiv": float(xi_equiv),
        "Omega_growth": float(mu_eff * om),
        "chi_total": float(chi_total),
        "AIC": float(AIC),
        "BIC": float(BIC),
        **{f"chi_{k}": float(v) for k, v in parts.items()}
    }

    cosmo.struct_cleanup()
    cosmo.empty()

    return result


# ==================================================
# TEST CONFIGS
# ==================================================

TESTS = [
    {
        "name": "01_growth_S8",
        "use_bao": False,
        "use_sn": False,
        "use_fs8": True,
        "use_s8": True,
        "use_as": True,
        "use_cmb_priors": True,
        "s8_obs": S8_BASE_OBS,
        "s8_err": S8_BASE_ERR,
        "maxiter": 45,
        "popsize": 8,
    },
    {
        "name": "02_BAO_SN_full",
        "use_bao": True,
        "use_sn": True,
        "use_fs8": True,
        "use_s8": True,
        "use_as": True,
        "use_cmb_priors": True,
        "s8_obs": S8_BASE_OBS,
        "s8_err": S8_BASE_ERR,
        "maxiter": 35,
        "popsize": 7,
    },
]

for wl_name, (s8obs, s8err) in WL_PRIORS.items():
    TESTS.append({
        "name": f"04_weak_lensing_prior_{wl_name}",
        "use_bao": True,
        "use_sn": True,
        "use_fs8": True,
        "use_s8": True,
        "use_as": True,
        "use_cmb_priors": True,
        "s8_obs": s8obs,
        "s8_err": s8err,
        "maxiter": 30,
        "popsize": 7,
    })


# ==================================================
# MAIN
# ==================================================

print("\n================================================")
print("SOP MASTER TEST v0")
print("LCDM vs SOP-min vs MU_LIBRE")
print("================================================")

summary = []

for test in TESTS:
    print("\n\n################################################")
    print("TEST:", test["name"])
    print("################################################")

    results = [
        fit_model("LCDM", test),
        fit_model("SOP", test),
        fit_model("MU_LIBRE", test),
    ]

    lcdm = results[0]
    sop = results[1]
    mu = results[2]
    best = min(results, key=lambda x: x["BIC"])

    for r in results:
        print("\nModelo:", r["model"])
        print("H0            =", r["H0"])
        print("Omega_m       =", r["Omega_m"])
        print("logA          =", r["logA"])
        print("sigma8        =", r["sigma8"])
        print("S8            =", r["S8"])
        print("rd            =", r["rd"])
        print("fc            =", r["fc"])
        print("f_out         =", r["f_out"])
        print("mu_eff        =", r["mu_eff"])
        print("xi_equiv      =", r["xi_equiv"])
        print("Omega_growth  =", r["Omega_growth"])
        print("chi_total     =", r["chi_total"])
        print("chi_BAO       =", r["chi_BAO"])
        print("chi_SN        =", r["chi_SN"])
        print("chi_fs8       =", r["chi_fs8"])
        print("chi_S8        =", r["chi_S8"])
        print("chi_As        =", r["chi_As"])
        print("chi_rd        =", r["chi_rd"])
        print("chi_ombh2     =", r["chi_ombh2"])
        print("chi_ommh2     =", r["chi_ommh2"])
        print("AIC           =", r["AIC"])
        print("BIC           =", r["BIC"])

    print("\n==============================")
    print("RESUMEN TEST:", test["name"])
    print("==============================")
    print("Mejor BIC =", best["model"])
    print("Delta BIC SOP - LCDM =", sop["BIC"] - lcdm["BIC"])
    print("Delta BIC MU  - LCDM =", mu["BIC"] - lcdm["BIC"])
    print("Delta BIC MU  - SOP  =", mu["BIC"] - sop["BIC"])
    print("SOP fc =", sop["fc"])
    print("SOP f_out =", sop["f_out"])
    print("SOP mu_eff =", sop["mu_eff"])
    print("MU xi_equiv =", mu["xi_equiv"])
    print("MU físico SOP? =", 0.0 <= mu["xi_equiv"] <= 1.0)

    summary.append({
        "test": test["name"],
        "best": best["model"],
        "Delta_BIC_SOP_LCDM": sop["BIC"] - lcdm["BIC"],
        "Delta_BIC_MU_LCDM": mu["BIC"] - lcdm["BIC"],
        "Delta_BIC_MU_SOP": mu["BIC"] - sop["BIC"],
        "SOP_fc": sop["fc"],
        "SOP_f_out": sop["f_out"],
        "SOP_mu_eff": sop["mu_eff"],
        "SOP_S8": sop["S8"],
        "SOP_Omega_growth": sop["Omega_growth"],
        "MU_xi_equiv": mu["xi_equiv"],
        "MU_physical_SOP": 0.0 <= mu["xi_equiv"] <= 1.0,
    })


print("\n\n================================================")
print("TABLA FINAL SOP MASTER TEST")
print("================================================")

for s in summary:
    print("\nTEST:", s["test"])
    print("Mejor BIC             =", s["best"])
    print("Delta BIC SOP-LCDM    =", s["Delta_BIC_SOP_LCDM"])
    print("Delta BIC MU-LCDM     =", s["Delta_BIC_MU_LCDM"])
    print("Delta BIC MU-SOP      =", s["Delta_BIC_MU_SOP"])
    print("SOP fc                =", s["SOP_fc"])
    print("SOP f_out             =", s["SOP_f_out"])
    print("SOP mu_eff            =", s["SOP_mu_eff"])
    print("SOP S8                =", s["SOP_S8"])
    print("SOP Omega_growth      =", s["SOP_Omega_growth"])
    print("MU xi_equiv           =", s["MU_xi_equiv"])
    print("MU físico como SOP?   =", s["MU_physical_SOP"])

print("\nLectura:")
print("- SOP fuerte: Delta BIC SOP-LCDM < -2 y fc estable.")
print("- SOP empate: |Delta BIC| < 2.")
print("- SOP tensionada: Delta BIC > 2.")
print("- Si MU_LIBRE empata y xi_equiv es físico, MU no destrona SOP: describe la misma supresión.")
# ==================================================
# GRAFICOS PRUEBA 1 — SOP MASTER TEST v0
# ==================================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

PLOT_DIR = "results/01_SOP_master_test_v0/plots"
os.makedirs(PLOT_DIR, exist_ok=True)

print("\n\nGenerando gráficos PRUEBA 1...")

tests = [s["test"] for s in summary]

delta_bic_sop = [s["Delta_BIC_SOP_LCDM"] for s in summary]
delta_bic_mu  = [s["Delta_BIC_MU_LCDM"] for s in summary]

s8_sop = [s["SOP_S8"] for s in summary]
fc_vals = [s["SOP_fc"] for s in summary]
fout_vals = [s["SOP_f_out"] for s in summary]
omega_growth = [s["SOP_Omega_growth"] for s in summary]

x = np.arange(len(tests))

# 1) Delta BIC
plt.figure(figsize=(11, 6))
plt.bar(x - 0.2, delta_bic_sop, width=0.4, label="SOP - LCDM")
plt.bar(x + 0.2, delta_bic_mu, width=0.4, label="MU_LIBRE - LCDM")
plt.axhline(0)
plt.xticks(x, tests, rotation=45, ha="right")
plt.ylabel("Delta BIC")
plt.title("PRUEBA 1 — Delta BIC: LCDM vs SOP vs MU_LIBRE")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "01_delta_bic.png"), dpi=200); 
plt.close()

# 2) S8 SOP
plt.figure(figsize=(11, 6))
plt.plot(tests, s8_sop, "o-")
plt.xticks(rotation=45, ha="right")
plt.ylabel("S8")
plt.title("PRUEBA 1 — S8 efectivo SOP")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "02_s8_sop.png"), dpi=200); 
plt.close()

# 3) fc activo
plt.figure(figsize=(11, 6))
plt.bar(tests, fc_vals)
plt.axhline(np.sqrt(3/5), linestyle="--", label="sqrt(3/5)")
plt.axhline(3/4, linestyle="--", label="3/4")
plt.axhline(np.pi/4, linestyle="--", label="pi/4")
plt.xticks(rotation=45, ha="right")
plt.ylabel("fc")
plt.title("PRUEBA 1 — Fracción activa fc por test")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "03_fc.png"), dpi=200); plt.close()

# 4) f_out complementario
plt.figure(figsize=(11, 6))
plt.bar(tests, fout_vals)
plt.xticks(rotation=45, ha="right")
plt.ylabel("f_out")
plt.title("PRUEBA 1 — Fracción complementaria f_out")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "04_f_out.png"), dpi=200); 
plt.close()

# 5) Omega_growth
plt.figure(figsize=(11, 6))
plt.plot(tests, omega_growth, "o-")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Omega_growth")
plt.title("PRUEBA 1 — Fuente efectiva de crecimiento")
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, "05_omega_growth.png"), dpi=200); 
plt.close()

print("\nGráficos PRUEBA 1 generados.")
