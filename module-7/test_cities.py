import unittest
from city_function import city_country


class TestCityCountry(unittest.TestCase):


    def test_city_country(self):
        result = city_country('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_with_population(self):
        result = city_country('Santiago', 'Chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')

    def test_city_country_name_case(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'santiago, chile')

if __name__ == '__main__':
    unittest.main()


