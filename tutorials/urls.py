from django.urls import path
from .views import index, my_list, about_us, contucts, prices, teacher, leadership, profiles, achievements, vacancies


urlpatterns = [
    path('', index),
    path('list/', my_list),
    path('consulting/', about_us),
    path('adress/', contucts),
    path('Our price/', prices),
    path('Our teachers/', teacher),
    path('Leadership/', leadership),
    path('Profile/', profiles),
    path('Achievements/', achievements),
    path('Vacancies/', vacancies)






]