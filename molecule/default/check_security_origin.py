"""Exit 0 if unattended-upgrades allows at least one security origin from the apt cache."""
import importlib.machinery
import importlib.util
import sys

import apt
import apt_pkg

loader = importlib.machinery.SourceFileLoader("uu", "/usr/bin/unattended-upgrade")
spec = importlib.util.spec_from_loader("uu", loader)
uu = importlib.util.module_from_spec(spec)
loader.exec_module(uu)

apt_pkg.init_config()
allowed = uu.get_allowed_origins()
print("allowed origins:", allowed)

security = {}
for pkg in apt.Cache():
    for ver in pkg.versions:
        for o in ver.origins:
            if "security" in (o.archive or "") or "Security" in (o.label or ""):
                security[(o.origin, o.archive, o.codename, o.label)] = o
if not security:
    sys.exit("no security origin found in apt cache")
ok = False
for key, o in security.items():
    match = uu.is_allowed_origin(o, allowed)
    print("security origin", key, "allowed:", match)
    ok = ok or match
sys.exit(0 if ok else 1)
