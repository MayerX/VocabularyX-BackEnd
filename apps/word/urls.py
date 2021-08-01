from django.urls import re_path

from . import views

urlpatterns = [
    # path('w/<str:word_id>', views.word_w_view.as_view()),
    re_path('w/(?P<word_id>[a-z0-9]{10})', views.word_w_view.as_view()),
    re_path('ws/(?P<word_spell>\w+)', views.word_ws_view.as_view()),
]
