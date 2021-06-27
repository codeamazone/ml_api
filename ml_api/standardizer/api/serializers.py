from rest_framework import serializers


class SensorSerializer(serializers.Serializer):
    sensor_1 = serializers.ListField(child=serializers.FloatField())
    sensor_2 = serializers.ListField(child=serializers.FloatField())
    sensor_3 = serializers.ListField(child=serializers.FloatField())

    def validate(self, data):
        """
        Check if the values in input json object are of eqial length
        """
        expected = len(data["sensor_1"]) == len(data["sensor_2"]) == len(data["sensor_3"])
        if not expected:
            raise serializers.ValidationError("Input lists must be of equal length.")
        return data


class ResultSerializer(serializers.Serializer):
    sensor1 = serializers.ListField(child=serializers.FloatField())
    sensor2 = serializers.ListField(child=serializers.FloatField())
    sensor3 = serializers.ListField(child=serializers.FloatField())


class StandardizeSerializer(serializers.Serializer):
    success = serializers.BooleanField(default=False)
    result = ResultSerializer()


class SampleValueSerializer(serializers.Serializer):
    data_set = serializers.CharField(max_length=11)
    data = SensorSerializer()
