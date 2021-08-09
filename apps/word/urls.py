from django.urls import re_path

from . import views

urlpatterns = [
    # path('w/<str:word_id>', views.word_w_view.as_view()),
    re_path('w/(?P<word_id>[a-z0-9]{10})', views.wView.as_view()),
    re_path('ws/(?P<word_spell>\w+)', views.wsView.as_view()),
    re_path('s/(?P<fragment>\w+)', views.sView.as_view()),
    re_path('wl/', views.wlView.as_view()),
    re_path('wls/', views.wlsView.as_view()),
    re_path('wordbatchView/', views.wordbatchView.as_view()),
    # re_path('wls/')
]
