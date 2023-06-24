from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Item, Reservation
from .forms import BookingForm
from .admin import Simple
from django.contrib.auth.models import User
from django.contrib import messages



# Acting homepage with all information view.


def get_bookings_sheet(request):
    items = Item.objects.all()
    reservation = Reservation.objects.all()
    appointment = reservation.filter(approve = True).order_by("made_on")
    sheet = {
        'items': items,
        'appointment': appointment
    }

    return render(request, 'bookings/bookings_sheet.html', sheet)


# Create a form to make a booking view.


def create_a_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user
            messages.success(request, "success")
            form.save()
            return redirect(reverse('get_bookings_sheet'))    

    form = BookingForm()
    sheet = {
            'form': form
    }

    return render(request, 'bookings/book_table.html', sheet)


# Edit booking view.


def edit_booking(request, booking_id):
    item = get_object_or_404(Item, id = booking_id)
    #reset = ResetApprove.objects.all()
    if request.method == 'POST':

        # Update instance.
        form = BookingForm(request.POST, instance = item)
        if form.is_valid():
            item.approve = False
            messages.info(request, 
            "Your change is being processed, await approval.")          
            #edit_approve_booking
            #reset.update()
            form.save()
            return redirect('get_bookings_sheet')

    # Prefill form with information from database.
    form = BookingForm(instance = item)
    sheet = {
        'form': form
    }

    return render(request, 'bookings/edit_bookings.html', sheet)    


def cancel_booking(request, booking_id):
    item = get_object_or_404(Item, id = booking_id)
    item.delete()
    messages.error(request, "Your booking has been cancelled!")
    return redirect('get_bookings_sheet')
