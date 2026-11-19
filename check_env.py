# check_env.py -- which of the project's packages are missing from this environment?
import importlib

# import name : name to install with
needed = {
    "numpy": "numpy", "pandas": "pandas", "xarray": "xarray", "netCDF4": "netcdf4",
    "pyproj": "pyproj", "scipy": "scipy", "yaml": "pyyaml", "joblib": "joblib",
    "tqdm": "tqdm", "sklearn": "scikit-learn", "skgstat": "scikit-gstat",
    "gstatsim": "gstatsim (pip)", "properscoring": "properscoring (pip)",
    "torch": "pytorch", "matplotlib": "matplotlib", "pyvista": "pyvista",
    "cartopy": "cartopy", "imageio": "imageio", "pytest": "pytest",
}

missing = []
for mod, pkg in needed.items():
    try:
        m = importlib.import_module(mod)
        print(f"  ok       {mod:14s} {getattr(m, '__version__', '')}")
    except ImportError:
        print(f"  MISSING  {mod:14s} -> install {pkg}")
        missing.append(pkg)

import shutil
print("  ok       ffmpeg" if shutil.which("ffmpeg") else "  MISSING  ffmpeg  -> install imageio-ffmpeg (only for MP4 animations)")

try:
    import torch
    print(f"\nMac GPU (MPS) available: {torch.backends.mps.is_available()}")
except ImportError:
    pass

print("\nNothing missing." if not missing else f"\nTo install: {', '.join(missing)}")