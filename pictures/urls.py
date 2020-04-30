from django.urls import path


from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:picture_id>/like/', views.like, name="like"),
    path('<int:picture_id>/dislike/', views.dislike, name="dislike"),
    path('like/', views.mlike, name="mlike"),
    path('dislike/', views.mdislike, name="mdislike"),
    path('like/?mlike', views.HomePageView.as_view(), name="mlike"),
    
]
