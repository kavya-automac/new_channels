from django.urls import path
from. import consumers


print("routingggg")
websocket_urlpatterns=[
    path('maithri/ws/sc/',consumers.MySyncConsumer.as_asgi()),
    path('maithri/ws/ac/', consumers.MyAsyncConsumer.as_asgi()),

]