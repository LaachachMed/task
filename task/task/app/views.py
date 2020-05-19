from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import task_data
from django.http import HttpResponse
import pandas as pd
# Create your views here.

# function to GET data from data base as an API
@api_view(["GET"])
def get_data(request):
    data = list(task_data.objects.values())
    return JsonResponse(data, safe=False)

# function to show data on simple HTML web page from database
def show_data(request):
    data = list(task_data.objects.values())
    # template = loader.get_template('web_app/index.html')
    context = {
        'data': data,
    }
    # print(data)
    print('data is requested')
    return render(request,'web_app/index.html',context)

# function to show data on a simple HTML web page from a csv file 'task_data.csv' directly
def show_data_from_csv(request):
    df = pd.read_csv('task_data.csv')
    df_list = []
    for i in range(len(df['id'])):
        temp = {}
        temp["id"] = df["id"][i]
        temp["timestamp"] = df["timestamp"][i]
        temp["temperature"] = df["temperature"][i]
        temp["duration"] = df["duration"][i]
        df_list.append(temp)

    context = {
        'data': df_list,
    }
    return render(request,'web_app/show_data_from_csv.html', context)