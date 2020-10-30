from collections import Counter
from django.shortcuts import render

click_list = []
show_list = []


def index(request):
    if request.GET.get('from-landing'):
        click_list.append('from-landing')
        return render(request, 'index.html')


def landing(request):
    if request.GET.get('ab-test-arg') == 'test':
        show_list.append('landing_alternate.html')
        return render(request, 'landing_alternate.html')
    elif request.GET.get('ab-test-arg') == 'original':
        show_list.append('landing.html')
        return render(request, 'landing.html')


def stats(request):
    try:
        counter_click = Counter(click_list)
        counter_show = Counter(show_list)
        test_conversion = counter_click['from-landing']/counter_show['landing_alternate.html']
        original_conversion = counter_click['from-landing']/counter_show['landing.html']
        return render(request, 'stats.html', context={
            'test_conversion': test_conversion,
            'original_conversion': original_conversion,
        })
    except ZeroDivisionError:
        print('Деление на ноль. Пройдите для успешного теста по обоим страницам')
