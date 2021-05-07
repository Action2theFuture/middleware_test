from django.urls import path
from demo.views import DemoView

urlpatterns = [
    path('', DemoView.as_view()),
]