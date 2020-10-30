import datetime
import os
from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    filenames = os.listdir(settings.FILES_PATH)
    files = []
    for name in filenames:
        file_date_info = os.stat(os.path.abspath(f'files/{name}'))
        ctime = datetime.datetime.fromtimestamp(file_date_info[8])
        mtime = datetime.datetime.fromtimestamp(file_date_info[9])
        fileinfo = {'name': name, 'ctime': ctime,
                    'mtime': mtime}
        if date:
            if date.date() == ctime.date():
                files.append(fileinfo)
        else:
            files.append(fileinfo)
    context = {
        'files': files,
        'date': date
    }
    return render(request, template_name, context)


def file_content(request, name):
    with open(os.path.abspath(f'files/{name}'), encoding='utf-8') as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
