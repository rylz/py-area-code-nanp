import json
import os

from collections import defaultdict

_AREA_CODE_REGIONS = None
_REGION_AREA_CODES = None

def load():
    """Load the dataset from disk.

    Can be called explicitly in order to control when this occurs. If not called
    explicitly, this work will be done the first time one of the lookup
    functions is called.
    """
    global _AREA_CODE_REGIONS, _REGION_AREA_CODES
    try:
        nanp_path = os.path.join(os.path.dirname(__file__), "data/nanp.json")
        with open(nanp_path, "r") as f:
            data = json.load(f)
        _AREA_CODE_REGIONS = {
            int(area_code): region
            for area_code, region in data.items()
        }
        _REGION_AREA_CODES = defaultdict(list)
        for area_code, region in _AREA_CODE_REGIONS.items():
            _REGION_AREA_CODES[region.lower()].append(area_code)
        return True
    except:
        return False


def get_region(area_code):
    """Lookup the region covered by an area code.

    area_code should be provided as in integer.

    Returns a string that typically represents a US State, Canadian Province,
    or a nation or territory, or None if the area code is not defined.
    """
    if _AREA_CODE_REGIONS is None:
        # attempt to load from disk, gracefully fail
        if not load():
            return
    return _AREA_CODE_REGIONS.get(area_code)


def get_area_codes(region):
    """Lookup a list of area codes for a region.

    region should be a string that represents a US State, Canadian Province,
    or a nation or territory. The lookup will be case-insensitive, but is
    sensitive to spacing.

    Returns a list of integer area codes, or None if the region was not found.
    """
    if _REGION_AREA_CODES is None:
        # attempt to load from disk, gracefully fail
        if not load():
            return
    return _REGION_AREA_CODES.get(region.lower())
