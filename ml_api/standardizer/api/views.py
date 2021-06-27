import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.preprocessing import StandardScaler

from .serializers import SensorSerializer, StandardizeSerializer
from .serializers import SampleValueSerializer


class StandardizeData(APIView):
    allowed_methods = ("POST", "GET")

    def post(self, request, format=None):
        # Validate the incoming input
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve sensor data object from input
        request_data = serializer.validated_data

        # Call method to standardize the input data
        standardized_data = self.standardize(request_data)

        # Define response data
        response_data = {
            "success": True,
            "result": {
                "sensor1": standardized_data[0],
                "sensor2": standardized_data[1],
                "sensor3": standardized_data[2]
            }}

        # Validate and serve response data
        serializer = StandardizeSerializer(data=response_data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        return Response(response_data, status=status.HTTP_200_OK)

    def get(self, format=None):
        response_data = {
            "data_set": "sample data",
            "data": {
                "sensor_1": [1.3, 3.4, 5.6],
                "sensor_2": [4.5, 6.7, 8.9],
                "sensor_3": [0.9, 9.8, 8.7]
            }}

        serializer = SampleValueSerializer(data=response_data)

        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        return Response(response_data, status=status.HTTP_200_OK)

    def standardize(self, data_object: dict):
        """
        Standardize the input data by means of scikitk-learn StandardScaler funcionality
        TODO: Clarify issue with sensor3 data (differ from task description)
        """
        # Load data object into a dataframe
        data = pd.DataFrame(data_object)

        # Define scaler
        scaler = StandardScaler()
        # Standardize data
        scaler.fit(data)
        standardized = scaler.transform(data)
        # Convert standardized data to original shape (2D matrix with 3 elements of len(sensor) elements)
        standardized = standardized.tolist()
        output = [[item[i] for item in standardized] for i in range(3)]
        return output
