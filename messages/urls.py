from django.conf.urls import url


from .views import MessageRudView, MessageAPIView

urlpatterns = [
    url(r'^$', MessageAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', MessageRudView.as_view(), name='post-rud')
]
