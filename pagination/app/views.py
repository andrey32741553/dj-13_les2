import math
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


with open("data-398-2018-08-30.csv", encoding='cp1251') as f:
    rows = csv.reader(f, delimiter=",")
    bus_stations_list = list(rows)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    bus_stations_modified_list = []
    current_page = int(request.GET.get('page', 1))
    items_per_page = 10
    total_pages = math.ceil(len(bus_stations_list) / items_per_page)
    if current_page < 1 or current_page > total_pages:
        current_page = 1
    for data in bus_stations_list[1:]:
        item = {'Name': data[1], 'Street': data[4],
                'District': data[6]}
        bus_stations_modified_list.append(item)
    prev_page_url, next_page_url = None, None
    if current_page > 1:
        prev_page_url = urlencode({'page': current_page - 1})
    if current_page * items_per_page < len(bus_stations_list):
        next_page_url = urlencode({'page': current_page + 1})

    return render(request, 'index1.html', context={
        'bus_stations': bus_stations_modified_list[items_per_page * current_page - 10: items_per_page * current_page],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

# def bus_stations(request):
#     bus_stations_show_list = []
#     current_page = int(request.GET.get('page', 1))
#     for data in bus_stations_list[1:]:
#         item = {'Name': data[1], 'Street': data[4],
#                 'District': data[6]}
#         bus_stations_show_list.append(item)
#     paginator = Paginator(bus_stations_show_list, 10)
#     bus_stations_result_list = paginator.get_page(current_page)
#     prev_page_url, next_page_url = None, None
#     if bus_stations_result_list.has_previous():
#         prev_page_url = bus_stations_result_list.previous_page_number()
#     if bus_stations_result_list.has_next():
#         next_page_url = bus_stations_result_list.next_page_number()
#     context = {'bus_stations': bus_stations_result_list,
#                'prev_page_url': prev_page_url,
#                'next_page_url': next_page_url,
#                'current_page': bus_stations_result_list.number
#     }
#     return render(request, 'index.html',
#                   context=context)
