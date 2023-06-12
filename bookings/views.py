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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_bookings_sheet')
    form = ItemForm()
    sheet = {
        'form': form
    }

    return render(request, 'bookings/book_table.html', sheet)

def edit_booking(request, item_id):
    return render(request, 'bookings/edit_bookings.html')    
