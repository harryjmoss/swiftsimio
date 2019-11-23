"""
Contains unit systems that may be useful to astronomers. In particular,
it contains the cosmo_units which can be considered Gadget-oid default units,
with

+ Unit length = Mpc
+ Unit velocity = km/s
+ Unit mass = 10^10 Msun
+ Unit temperature = K
"""

import unyt


try:
    # Need to do this first otherwise the `unyt` system freaks out about
    # us upgrading msun from a symbol
    cosmo_units = unyt.UnitSystem(
        "cosmological",
        unyt.Mpc,
        1e10 * unyt.msun,
        (1.0 * unyt.s * unyt.Mpc / unyt.km).to(unyt.Gyr),
    )

    # We need to upgrade msun from a symbol to a first class unit. This allows
    # people to do .convert_to_units("msun") and have it actually work.
    unyt.define_unit("msun", unyt.msun, tex_repr=r"M_\odot")
except RuntimeError:
    # We've already done that, oops.
    cosmo_units = unyt.unit_systems.cosmological
    pass
