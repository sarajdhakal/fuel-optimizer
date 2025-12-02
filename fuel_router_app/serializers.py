from rest_framework import serializers


class RouteResponseSerializer(serializers.Serializer):
    start = serializers.CharField()
    end = serializers.CharField()
    start_lat = serializers.FloatField()
    start_lon = serializers.FloatField()
    end_lat = serializers.FloatField()
    end_lon = serializers.FloatField()
    fuel_stops = serializers.ListField()
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=4)
    total_distance = serializers.FloatField()
    map_url = serializers.CharField()


class RouteRequestSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=255)
    end = serializers.CharField(max_length=255)
