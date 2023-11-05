"""
URL configuration for edtechapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import IndexView, PuzzlesView, InformationView, PaintOnlineView, PuzzleKidsView, ColoringView, SimonMemorizeView
from useraccounts.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path('', IndexView, name="home"),
    path('puzzles/', PuzzlesView, name="home"),
    path('information/', InformationView, name="home"),
    path("puzzles/paintonline/", PaintOnlineView, name="paintonline"),
    path("puzzles/puzzlekids/", PuzzleKidsView, name="puzzlekids"),
    path("puzzles/coloringview/", ColoringView, name="coloringview"),
    path("puzzles/simon/", SimonMemorizeView, name="simon"),
    
    path("signup/", SignUpView.as_view(), name="signup"),
]
