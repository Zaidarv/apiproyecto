from django.urls import path 
from .views import TutorView

urlpatterns=[
    path('tutores/', TutorView.as_view(), name='tutores_list'),
    path('tutores/<int:id>', TutorView.as_view(), name='tutores_process')
]