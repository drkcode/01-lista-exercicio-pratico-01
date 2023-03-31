import unittest
from convert_km_to_mile import convert_kilometer_to_mile


class TestConvertKilometersToMiles(unittest.TestCase):
    def test_negative_distance_value(self):
        with self.assertRaises(
            Exception, msg="should throw a exception if distance is a negative value"
        ):
            convert_kilometer_to_mile(-500)

    def test_convert_distance(self):
        sut_1 = convert_kilometer_to_mile(50)
        self.assertEqual(
            sut_1,
            31.056,
            "should return 31.056 miles if distance is equal to 50 kilometers",
        )

        sut_2 = convert_kilometer_to_mile(72)
        self.assertEqual(
            sut_2,
            44.720,
            "should return 44.720 miles if distance is equal to 70 kilometers",
        )
