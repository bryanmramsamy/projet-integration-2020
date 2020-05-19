from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse

def reservationview(request):

    reservation = Reservation.objects.all() [0]
    context = {"reservation": reservation}
    template = "app/reservationview.html"
    return render(request, template, context, "app/reservationview.html")

def updatepricereservation (request):
    reservation = Reservation.objects.all() [0]
    reservation.price = reservation.seats * reservation.representation.show.price