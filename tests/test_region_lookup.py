from unittest import TestCase
from unittest.mock import patch

import area_code_nanp

class TestRegionLookup(TestCase):

    def test_lookup_by_code(self):
        # invalid codes
        self.assertIsNone(area_code_nanp.get_region(911))
        self.assertIsNone(area_code_nanp.get_region(8675309))
        self.assertIsNone(area_code_nanp.get_region('911'))

        self.assertEqual('Texas', area_code_nanp.get_region(817))

    def test_lookup_by_region(self):
        # invalid regions
        self.assertIsNone(area_code_nanp.get_area_codes(u'德州'))
        self.assertIsNone(area_code_nanp.get_area_codes('Fort Worth'))

        self.assertIn(817, area_code_nanp.get_area_codes('Texas'))
        self.assertIn(817, area_code_nanp.get_area_codes('texas'))
        self.assertIn(817, area_code_nanp.get_area_codes('TEXAS'))
        self.assertIn(817, area_code_nanp.get_area_codes('TeXaS'))

    @patch('area_code_nanp.load', return_value=False)
    def test_load(self, mock_load):
        # gracefully fail when load fails
        self.assertIsNone(area_code_nanp.get_region(911))
        mock_load.assert_called()

        mock_load.reset_mock()
        self.assertIsNone(area_code_nanp.get_area_codes('Reno'))
        mock_load.assert_called()

        # don't call load when data is already in memory
        mock_load.reset_mock()
        with patch.object(area_code_nanp, '_AREA_CODE_REGIONS', {911: 'Reno'}):
            self.assertEqual('Reno', area_code_nanp.get_region(911))
        with patch.object(area_code_nanp, '_REGION_AREA_CODES', {'reno': [911]}):
            self.assertEqual([911], area_code_nanp.get_area_codes('Reno'))
        mock_load.assert_not_called()
