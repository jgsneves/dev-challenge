from django.contrib import admin
from django.urls import path
from api.views import get_single_employer

urlpatterns = [
    #admin route
    path('admin/', admin.site.urls),

    #employers routes
    path('/employer/<int:employer_code>', get_single_employer, name='single_employer'),

    #medical license routes
    
]
