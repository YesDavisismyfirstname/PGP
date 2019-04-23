from channels.routing import route
from apps.login.consumers import ws_message, ws_add, ws_disconnect, ws_connect



channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.receive", ws_message, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]