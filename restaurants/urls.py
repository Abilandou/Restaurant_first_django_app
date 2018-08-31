from django.conf.urls import url
#from . import views
from django.views.generic import TemplateView
from restaurants.views import(
    restaurant_listview,
    restaurant_createview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView

)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/create$', restaurant_createview), #RestaurantCreateView.as_view()),
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    #url(r'^asian/$', AsianFusionRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html')),

]