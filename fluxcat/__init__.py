"""Catalog the measured flux densities of astronomical sources.

Any catalog can be accessed using :py:meth:`fluxcat.catalogs.load`,
which takes a catalog name and returns a dict containing the parsed
JSON representation of the catalog:

    >>> import fluxcat.catalogs
    >>> fluxcat.catalogs.list()
    ['atnf_psrcat', 'hfb_target_list', 'primary_calibrators_perley2016',
     'specfind_v2_5Jy_vollmer2009']
    >>> perley2016 = fluxcat.catalogs.load('primary_calibrators_perley2016')
    >>> perley2016["CAS_A"]["ra"]
    350.86642

Catalogs can also be loaded into the global namespace as a `FluxCatalog` instance:

    >>> from fluxcat import FluxCatalog, catalogs
    >>> FluxCatalog.load_dict(catalogs.load(col), col)

Submodules
==========

.. autosummary::
    :toctree: _autosummary

    catalogs
"""

__all__ = ["FluxCatalog", "__version__", "catalogs"]

from importlib.metadata import PackageNotFoundError, version

from .core import FluxCatalog as FluxCatalog
from . import catalogs as catalogs

try:
    __version__ = version("fluxcat")
except PackageNotFoundError:
    # package is not installed
    pass

del version, PackageNotFoundError
