from django.urls import re_path

from . import views

urlpatterns = [
    # path('w/<str:word_id>', views.word_w_view.as_view()),
    re_path('w/', views.wView.as_view()),
    re_path('ws/', views.wsView.as_view()),
    re_path('s/', views.sView.as_view()),
    re_path('wl/', views.wlView.as_view()),
    re_path('wls/', views.wlsView.as_view()),
    re_path('wordbatchView/', views.wordbatchView.as_view()),
    # re_path('wls/')
]
