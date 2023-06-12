from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_bookings_sheet(request):
    items = Item.objects.all()
    sheet = {
        'items': items
    }
    return render(request, 'bookings/bookings_sheet.html', sheet)

def create_a_booking(request):
    if request.method == 'POST':
        name = request.POST.get('booked_name')
        email = request.POST.get('booked_email')
        date = request.POST.get('booked_date')
        time = request.POST.get('booked_time')
        people = request.POST.get('booked_num_of_people')
        tableSize = request.POST.get('booked_table_allocation')
        booked = 'booked_check' in request.POST
        cancel = 'booked_cancel' in request.POST
        Item.objects.create(name=name, email=email, date=date, time=time, people=people, 
                            tableSize=tableSize, booked=booked, cancel=cancel)

        return redirect('get_bookings_sheet')
    form = ItemForm()
    sheet = {
        'form' = form
    }

    return render(request, 'bookings/book_table.html')    
