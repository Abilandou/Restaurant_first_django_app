# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            #customize
            #like a pre_save
            instance.owner = request.user
            instance.save()
            #like a post_save
            #form.save()
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

    template_name = 'form.html'
    context = {
        "form": form,
        "errors": errors
    }
    return render(request, template_name, context)

def restaurant_listview(request,):
    template_name = 'restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def restaurant_detailview(request, slug):
    template_name = 'restaurantlocations_detail.html'
    obj= RestaurantLocation.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)



class RestaurantListView(ListView):
    template_name = 'restaurantlocation_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )

        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    template_name = 'restaurantlocations_detail.html'
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "form.html"
    success_url = "/restaurants/"