from django.shortcuts import render, redirect
from .models import Table, Reservation
import datetime

def table_reservation(request):

    dateToday = datetime.datetime.today()
    is_table_available = True

    if request.method == 'POST':
        selected_table = request.POST.get('selected_table')
        date = request.POST.get('date')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        date = datetime.datetime.strptime(date, '%Y-%m-%d')

        if date < dateToday:
            print('Вы выбрали неверную дату')
        # Проверка доступности столика на выбранную дату
        is_table_available = Reservation.objects.filter(table_id=selected_table, date=date).count() == 0

        if is_table_available:
            Reservation.objects.create(table_id=selected_table, date=date, customer_name=customer_name, customer_email=customer_email)
            # Отправка письма с подтверждением заказа (используйте библиотеку для отправки электронной почты, например, Django's send_mail)

            return redirect('success_page')  # Перенаправление на страницу успешного заказа
        else:
            # Обработка случая, когда столик уже занят на выбранную дату
            pass

    # Получение списка столов для отображения на странице
    tables = Table.objects.order_by('id')
    return render(request, 'Cat/table_reservation.html',
                   {'title':'Главная страница сайта',
                    'tables':  tables,
                    'dateToday' : dateToday, 
                    'is_table_available' : is_table_available,
                    })

def success_page(request):
    return render(request, 'Cat/success_page.html')
