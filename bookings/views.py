from django.shortcuts import render

# Create your views here.
def get_bookings_sheet(request):
    return render(request, 'bookings/bookings_sheet.html')