from django.urls import path

from . import views

app_name = "polls"


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("test", views.test_view, name="test_view"),
    

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("<int:question_id>/addchoice/", views.addchoice, name="addchoice"),
    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),
    path("<int:question_id>/resetvote/", views.resetvote, name="resetvote"),
    path("addques/", views.addques, name="addques"),
    path("newques/", views.newques, name="newques"),

]