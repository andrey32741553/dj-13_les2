from django.urls import path, register_converter
from file_server.app.views import file_list, file_content
from .converters import DateConverter

register_converter(DateConverter, 'DC')


urlpatterns = [
    path('', file_list, name='file_list'),
    path('<DC:date>', file_list, name='file_list'),
    path('file_content/<name>', file_content, name='file_content'),
]
