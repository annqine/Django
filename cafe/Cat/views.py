from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Reservation, Recipe
import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def table_reservation(request):
    dateToday = datetime.datetime.today()
    formatted_date = datetime.datetime.strftime(dateToday, '%Y-%m-%d')
    is_table_available = True

    if request.method == 'POST':
        selected_tables = request.POST.getlist('selected_tables')
        date = request.POST.get('date')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        print(f"selected_tables: {selected_tables}")
        print(f"date: {date}")
        print(f"customer_name: {customer_name}")
        print(f"customer_email: {customer_email}")

        is_table_available = Reservation.objects.filter(table_id__in=selected_tables, date=date).count() == 0

        if is_table_available:
            for table_id in selected_tables:
                Reservation.objects.create(table_id=table_id, date=date, customer_name=customer_name,
                                           customer_email=customer_email)

            subject = 'Подтверждение бронирования стола'

            html_message = render_to_string('email.html', {
                'customer_name': customer_name,
                'date': date,
                'selected_tables': selected_tables,
            })

            try:
                send_mail(subject, strip_tags(html_message), customer_email, [customer_email], fail_silently=False, html_message=html_message)
                print("Sending mail")
                return redirect('success_page')
            except Exception as e:
                print(f"Error sending email: {e}")
                return redirect('table_reservation')

        return redirect('table_reservation')

    tables = Table.objects.order_by('id')
    context = {
        'title': 'Главная страница сайта',
        'tables': tables,
        'dateToday': formatted_date,
        'is_table_available': is_table_available,
    }

    return render(request, 'Cat/table_reservation.html', context)


def success_page(request):
    return render(request, 'Cat/success_page.html')


def menu(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'Cat/menu.html', context)

def menu_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'Cat/menu_recipe.html', {'recipe': recipe})
