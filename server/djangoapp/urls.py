from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL patterns
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='about', view=views.about, name='about'),
    # path for contact us view
    path(route='contact', view=views.contact, name='contact'),
    # path for registrations
    path(route='registration', view=views.registration_request, name='registration'),
    # path for logins
    path(route='login', view=views.login_request, name='login'), 
    # path for logouts
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    
    path('dealer/<int:dealer_id>/<str:dealer_name>/', views.get_dealer_details, name='dealer_details'),
    # path for add a review view
     path('dealer/<int:dealer_id>/<str:dealer_name>/addreview/', views.add_review, name='add_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)