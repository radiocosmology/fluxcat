"""Test the `FluxCatalog` class."""

import importlib
import pytest

import fluxcat.core

DEFAULT_COLLECTIONS = ["atnf_psrcat"]


@pytest.fixture(autouse=True)
def reload_import():
    # Reload the fluxcat module to reset any previously
    # loaded catalogs. We also have to reset this module
    # attribute, which doesn't get reloaded by importlib
    fluxcat.core.__defaults_loaded = False
    globals()["__defaults_loaded"] = False
    importlib.reload(fluxcat.core)


def test_defaults_loaded():
    """Test that default collections are lazily loaded."""

    assert len(fluxcat.core.FluxCatalog._collections) == 0

    # Trigger loading the catalog by interacting in some way
    fluxcat.core.FluxCatalog.sort()

    # Check that default collections have been loaded
    for name in fluxcat.core.DEFAULT_COLLECTIONS:
        assert name in fluxcat.core.FluxCatalog._collections


def test_subclass():
    """Test that a subclass of `FluxCatalog` won't inherit defaults."""

    class SubCatalog(fluxcat.core.FluxCatalog): ...

    # Nothing has been loaded yet
    assert len(SubCatalog._collections) == 0

    # Trigger loading the default catalog for `SubCatalog`
    SubCatalog.sort()
    loaded_collections = SubCatalog._collections.copy()

    for name in DEFAULT_COLLECTIONS:
        assert name in loaded_collections

    # Trigger loading the default catalogs for `FluxCatalog`
    # and check that each class has it's own catalogs
    fluxcat.core.FluxCatalog.sort()

    # Check that default collections still exist
    for name in fluxcat.core.DEFAULT_COLLECTIONS:
        assert name in fluxcat.core.FluxCatalog._collections

    assert SubCatalog._collections == loaded_collections
