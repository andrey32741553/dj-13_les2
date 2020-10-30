from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
click_list = []
show_list = []


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.GET.get('from-landing'):
        click_list.append('from-landing')
        print(Counter(click_list))
        return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    if request.GET.get('ab-test-arg') == 'test':
        show_list.append('landing_alternate.html')
        print(Counter(show_list))
        return render(request, 'landing_alternate.html')
    elif request.GET.get('ab-test-arg') == 'original':
        show_list.append('landing.html')
        print(Counter(show_list))
        return render(request, 'landing.html')


def stats(request):
    try:
        counter_click = Counter(click_list)
        counter_show = Counter(show_list)
        test_conversion = counter_click['from-landing']/counter_show['landing_alternate.html']
        original_conversion = counter_click['from-landing']/counter_show['landing.html']
        # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
        # Для вывода результат передайте в следующем формате:
        return render(request, 'stats.html', context={
            'test_conversion': test_conversion,
            'original_conversion': original_conversion,
        })
    except ZeroDivisionError:
        print('Деление на ноль. Пройдите для успешного теста по обоим страницам')
