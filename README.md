# py-area-code-nanp

Information about phone area codes in the North American Numbering Plan.

This package provides a simple lookup table from area code to region, and from region to list of area codes. Area code data was most recently retrieved from Wikipedia in October 2020.

Example usage:
```
>>> import area_code_nanp
>>> area_code_nanp.get_area_codes('Texas')
[210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 945, 956, 972, 979]
>>> area_code_nanp.get_region(817)
'Texas'
>>> 
```
