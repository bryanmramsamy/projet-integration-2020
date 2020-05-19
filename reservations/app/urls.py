from django.conf.urls import url
# import of the built-in Django authentication and give it a "auth_views" alias
from django.contrib.auth import views as auth_views

from django.urls import include
from app.feedrss import LastShowFeed, LocationFeed, RepresentationFeed
from app.views import authentication, views, show
from app.views.api import (ArtistApiView, LocationApiView,
                           RepresentationApiView, ShowApiView)
from app.views.locationList import LocationListView
from app.views.locationdetailed import LocationDetailedView
from app.views.showCRUD import CreateShow, DeleteShow, UpdateShow

from app.views.reservation import ReservationView

urlpatterns = [
    # Home page
    url(r'^$', views.home, name='home'),

    # Authentication
    url(r'^register/$', authentication.signup, name='register'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name="app/logout.html"),
        name='logout'),

    # User Profile
    url(r'^profile/$', authentication.ProfileView.as_view(), name='profile'),
    url(r'^profile/update$', authentication.profileUpdate,
        name='profile_update'),

    # Password Change
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(template_name="app/\
            password_change_form.html"), name='password_change_form'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name="app/\
            password_change_done.html"), name='password_change_done'),

    # Password Reset
    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(template_name="app/\
            password_reset_form.html"), name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name="\
            app/password_reset_done.html"), name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name="app/\
            password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name="app/\
            password_reset_complete.html"), name='password_reset_complete'),

    # Shows
    url(r'^show/$', show.show_list, name='show'),
    url(r'^show/(?P<pk>[0-9]+)/$', show.show_detail, name='show_detail_pk'),
    url(r'^show/(?P<slug>[a-zA-Z0-9-]+)/$', show.show_detail_slug,
        name='show_detail_slug'),
    url(r'^show/create/$', CreateShow, name='ShowCrud'),
    url(r'^show/update/(?P<pk>[0-9]+)/$', UpdateShow, name='UpdateShow'),
    url(r'^show/delete/(?P<pk>[0-9]+)/$', DeleteShow, name='DeleteShow'),

    # Locations
    url(r'^location/$', LocationListView, name='LocationListView'),
    url(r'^location/(?P<pk>[0-9]+)/$', LocationDetailedView,
        name='LocationPkView_pk'),
    url(r'^location/(?P<slug>[a-zA-Z0-9-]+)/$', LocationDetailedView,
        name='LocationPkView_slug'),

    # API
    url(r'^api/artist/', ArtistApiView.as_view(), name='api_artist'),
    url(r'^api/show/', ShowApiView.as_view(), name='api_show'),
    url(r'^api/representation/', RepresentationApiView.as_view(),
        name='api_representation'),
    url(r'^api/location/', LocationApiView.as_view(), name='api_location'),

    # RSS Feeds
    url(r'^rss/show/', LastShowFeed(), name='rss_show'),
    url(r'^rss/representation/', RepresentationFeed(),
        name='rss_representation'),
    url(r'^rss/location/', LocationFeed(), name='rss_location'),


    # reservation

    url(r'^reservation/$', ReservationView, name='reservation'),
    url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationView, name='reservation_pk'),
    #Paypal
    url(r'paypal/', include('paypal.standard.ipn.urls')),

]
