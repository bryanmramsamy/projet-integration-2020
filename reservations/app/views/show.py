from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from django.urls import reverse
import requests

from app.models.show import Show, Representation


def show_list(request):
    """Render list of shows"""

    query = request.GET.get("query", None)  # use get GET.get to prevent error
    shows = Show.objects.all()

    if query is not None:  # if my query is not empty i change the way how the queryset is set
        shows = Show.objects.filter(title__icontains=query)

    # function about pagination i chose to put a default value directly with GEt.get method
    paginator = Paginator(shows, 16)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'shows': page
    }

    return render(request, 'app/show_list.html', context)


def show_detail(request, pk):
    """Display details of one selected show based on its pk"""

    show = Show.objects.get(pk=pk)
    representations = Representation.objects.filter(show=pk)

    # print(show)

    context = {
        'show': show,
        'representations': representations
    }

    return render(request, 'app/show_detail.html', context)


def show_detail_slug(request, slug):
    """Display details of one selected show based on its slug"""
    # TODO: Function has been duplicated for slug support, must be merged

    show = Show.objects.get(slug=slug)
    representations = Representation.objects.filter(show=show.pk)

    # print(show)

    context = {
        'show': show,
        'representations': representations
    }

    return render(request, 'app/show_detail.html', context)

def show_external_api(request):

    api_url = "http://127.0.0.1:8000/external-api/show/"
    r = requests.get(api_url, timeout=10)
    data = r.json()

    context = {
        'data' : data
    }

    return render(request, 'app/external_api_show.html', context)

def update_show_external_api(request):

    api_url = "http://127.0.0.1:8000/external-api/show/"
    r = requests.get(api_url, timeout=10)
    data = r.json()
    data_to_create = []
    data_to_update = []

    for show in data:
        if show['description'] == None:
            show['description'] = 'Pas de description'
        new_show = Show(
            title = show['title'],
            description = show['description'],
            poster = show['poster'],
            bookable = show['bookable'],
            price = show['price'],
        )

        if not Show.objects.filter(title=show['title']):
            data_to_create.append(new_show)
            new_show.save()
        else:
            data_to_update.append(show)
            Show.objects.filter(title=show['title']).update(
                title = show['title'],
                description = show['description'],
                poster = show['poster'],
                bookable = show['bookable'],
                price = show['price'],
            )
    
    context = {
        'data_to_create' : data_to_create,
        'data_to_update' : data_to_update,
    }

    return render(request, 'app/update_show.html', context)

    
        