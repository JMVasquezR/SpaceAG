from django.conf.urls import url

from nucleo.views import LoginView, InicioViewSet, LogoutView

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^inicio/', InicioViewSet.as_view(), name='inicio'),
    url(r'^logout/', LogoutView.as_view(), name='salida'),
]
