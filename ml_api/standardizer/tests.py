from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

from .api.serializers import SensorSerializer


class ValidationTestCase(APITestCase):
    def test_validate_wrong_datatype(self):
        """
        Ensure that validation fails when input values are not of type list
        """
        wrong_input = {
            "sensor_1": "Hello",
            "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
            "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
        }
        serializer = SensorSerializer(data=wrong_input)
        self.assertEqual(serializer.is_valid(), False)

    def test_validate_correct_datatype(self):
        """
        Ensure that validation passes when input values are of type list
        """
        correct_input = {
            "sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
            "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
            "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
        }
        serializer = SensorSerializer(data=correct_input)
        self.assertEqual(serializer.is_valid(), True)

    def test_validate_wrong_listlength(self):
        """
        Ensure that validation fails when input lists are of different length
        """
        wrong_input = {
            "sensor_1": [5.44, 3.22, 6.55, 8.54],
            "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
            "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
        }
        serializer = SensorSerializer(data=wrong_input)
        self.assertEqual(serializer.is_valid(), False)

    def test_validate_correct_listlength(self):
        """
        Ensure that validation passes when input lists all have the same length
        """
        correct_input = {
            "sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
            "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
            "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
        }
        serializer = SensorSerializer(data=correct_input)
        self.assertEqual(serializer.is_valid(), True)
