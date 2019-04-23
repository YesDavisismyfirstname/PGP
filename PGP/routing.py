#from channels.routing import route
#from apps.login.consumers import ws_connect, ws_disconnect, ws_receive
#from channels import include

#def message_handler(message):
#    print(message['text'])

#channel_routing = [
    #route("websocket.receive",message_handler),
    #route('websocket.connect', ws_connect),
    #route('websocket.disconnect', ws_disconnect),
#    include("apps.gamelobby.routing.websocket_routing", path=r"^/chat/stream"),
#    include("apps.gamelobby.routing.custom_routing"),
#]
from channels import include
from channels import route

def message_handler(message):
    print("here")
    print(message['text'])

channel_routing = [
    # Include sub-routing from an app.
    #route("websocket.receive", message_handler),
    include("apps.gamelobby.routing.websocket_routing", path=r"^/chat/stream"),

    include("apps.gamelobby.routing.custom_routing"),

]