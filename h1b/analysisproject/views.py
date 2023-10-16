from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Percentile
from .models import Application

class SummaryStatisticsView(APIView):
    def get(self, request):
        total_records = Application.objects.count()
        mean_salary = Application.objects.filter(visa_class='R').aggregate(mean_salary=Avg('laborcondition__prevailing_wage'))
        percentile_25 = Application.objects.filter(visa_class='R').aggregate(percentile_25_salary=Percentile('laborcondition__prevailing_wage', 25))
        percentile_75 = Application.objects.filter(visa_class='R').aggregate(percentile_75_salary=Percentile('laborcondition__prevailing_wage', 75))

        data = {
            'total_records': total_records,
            'mean_salary': mean_salary['mean_salary'],
            'percentile_25_salary': percentile_25['percentile_25_salary'],
            'percentile_75_salary': percentile_75['percentile_75_salary'],
        }
        return Response(data)