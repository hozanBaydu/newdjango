from django.urls import path
from . import views

app_name='tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), # atilsamancioglu.com/tweetapp/
    path('addtweet/',views.addtweet,name='addtweet'), # atilsamancioglu.com/tweetapp/addtweet/
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'),
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),
    path('signup/',views.SignUpView.as_view(),name='signup'), # Fonksiyon bazlı değil sınıf bazlı ondan as_view koyduk.
    path('deletetweet/<int:id>',views.deletetweet,name='deletetweet'),  # <int:id> list tweette alınıyor zaten (<a href="{% url 'tweetapp:deletetweet' id=tweet.id %}" class="btn btn-danger">Delete</a>)



]