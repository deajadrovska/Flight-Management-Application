from django.shortcuts import render, redirect

from application.forms import FlightForm
from application.models import Flight


# Create your views here.


def index(request):
    flights = Flight.objects.filter(user=request.user, take_off_airport="Skopje")

    return render(request, 'index.html', {'flights': flights})


def details(request, flight_id):
    flight = Flight.objects.filter(id = flight_id).first()
    return render(request, 'details.html', {'flight': flight})


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
        return redirect('index')

    form = FlightForm()
    return render(request, 'add_flight.html', {'form': form})


def edit_flight(request, flight_id):
    flight = Flight.objects.filter(id = flight_id).first()
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()
        return redirect(index)


    form = FlightForm(instance = flight)
    context = {'form': form , 'flight_id' : flight_id}
    return render(request, 'edit_flight.html', context)