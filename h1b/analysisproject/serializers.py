from rest_framework import serializers

class SummaryStatisticsSerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    mean_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    percentile_25_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    percentile_75_salary = serializers.DecimalField(max_digits=10, decimal_places=2)