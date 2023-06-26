from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Item, Reservation
from .forms import BookingForm
from .admin import Simple
from django.contrib.auth.models import User
from django.contrib import messages



# View to get and show your booking/reservation details.


def get_bookings_sheet(request):
    # Get all objects in class Item()
    items = Item.objects.all()
    # Get all objects in class Reservation()
    reservation = Reservation.objects.all()
    # Order and show bookings in order "made_on".
    appointment = reservation.filter(approve = True).order_by("made_on")
    # Show objects on rendered html page.
    sheet = {
        'items': items,
        'appointment': appointment,
    }

    return render(request, 'bookings/bookings_sheet.html', sheet)


# View on which to create a form to make a 'booking' view.


def create_a_booking(request):
    # POST form with method = 'POST'
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get username on registation(.user) and prefill field on 'name' in form.
            form.instance.name = request.user
            # Success Message Tags.
            messages.success(request, "success")
            # Save information in form.
            form.save()
            # Redirect to get_bookings_sheet render request page.
            return redirect(reverse('get_bookings_sheet'))    

    # Create form from model in BookingForm()
    form = BookingForm()
    sheet = {
            'form': form
    }

    return render(request, 'bookings/book_table.html', sheet)


# Edit booking view.


def edit_booking(request, booking_id):
    # Create instance
    item = get_object_or_404(Item, id = booking_id)
    # Change form with method = 'POST'.
    if request.method == 'POST':

        # Update instance.
        form = BookingForm(request.POST, instance = item)
        if form.is_valid():
            # Resets item.approve equal to false
            item.approve = False
            messages.info(request, 
            "Your change is being processed, await approval.")          
            #edit_approve_booking and save form
            form.save()
            # redirect back to function input.
            return redirect('get_bookings_sheet')
        else:
            print(form.errors)

    # Prefill form with information from database.
    form = BookingForm(instance = item)
    sheet = {
        'form': form
    }

    return render(request, 'bookings/edit_bookings.html', sheet)    

#Cancel your booking and it removed from 'Administraion' page.

def cancel_booking(request, booking_id):
    # Create Instance
    item = get_object_or_404(Item, id = booking_id)
    # Delete said item.
    item.delete()
    # Message Tags
    messages.error(request, "Your booking has been cancelled!")
    # redirect back to function input.
    return redirect('get_bookings_sheet')
