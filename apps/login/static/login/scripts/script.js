	$(function () {
		// Correctly decide between ws:// and wss://
		var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
		var ws_path = ws_scheme + '://' + window.location.host + "/chat/stream/";
		console.log("Connecting to " + ws_path);
		var socket = new ReconnectingWebSocket(ws_path);

		// Helpful debugging
		socket.onopen = function () {
			console.log("Connected to chat socket");
		};
		socket.onclose = function () {
			console.log("Disconnected from chat socket");
		};

		socket.onmessage = function (message) {
			// Decode the JSON
			console.log("Got websocket message " + message.data);
			var data = JSON.parse(message.data);
			// Handle errors
			if (data.error) {
				console.log("error")
				alert(data.error);
				return;
			}
			// Handle joining
			if (data.join) {
				console.log("jr")
				console.log("Joining room " + data.join);
				var roomdiv = $(
					"<div class='room' id='room-" + data.join + "'>" +
					"<h2>" + data.title + "</h2>" +
					"<div class='messages'></div>" +
					"<input><button>Send</button>" +
					"</div>"
				);
				$("#chats").append(roomdiv);
				roomdiv.find("button").on("click", function () {
					socket.send(JSON.stringify({
						"command": "send",
						"room": data.join,
						"message": roomdiv.find("input").val()
					}));
					roomdiv.find("input").val("");
				});
				// Handle leaving
			} else if (data.leave) {
				console.log("Leaving room " + data.leave);
				$("#room-" + data.leave).remove();
			} else if (data.message || data.msg_type != 0) {
				var msgdiv = $("#room-" + data.room + " .messages");
				var ok_msg = "";
				// msg types are defined in chat/settings.py
				// Only for demo purposes is hardcoded, in production scenarios, consider call a service.
				switch (data.msg_type) {
					case 0:
						// Message
						ok_msg = "<div class='message'>" +
							"<span class='username'>" + data.username + "</span>" +
							"<span class='body'>" + data.message + "</span>" +
							"</div>";
						break;
					case 1:
						// Warning/Advice messages
						ok_msg = "<div class='contextual-message text-warning'>" + data.message + "</div>";
						break;
					case 2:
						// Alert/Danger messages
						ok_msg = "<div class='contextual-message text-danger'>" + data.message + "</div>";
						break;
					case 3:
						// "Muted" messages
						ok_msg = "<div class='contextual-message text-muted'>" + data.message + "</div>";
						break;
					case 4:
						// User joined room
						ok_msg = "<div class='contextual-message text-muted'>" + data.username + " joined the room!" + "</div>";
						break;
					case 5:
						// User left room
						ok_msg = "<div class='contextual-message text-muted'>" + data.username + " left the room!" + "</div>";
						break;
					default:
						console.log("Unsupported message type!");
						return;
				}
				msgdiv.append(ok_msg);
				msgdiv.scrollTop(msgdiv.prop("scrollHeight"));
			} else {
				console.log("Cannot handle message!");
			}
		};

		// Says if we joined a room or not by if there's a div for it
		function inRoom(roomId) {
			console.log(roomId)
			return $("#room-" + roomId).length > 0;
		};

		// Room join/leave
		$("li.room-link").click(function () {
			roomId = $(this).attr("data-room-id");
			console.log("click")
			if (inRoom(roomId)) {
				// Leave room
				$(this).removeClass("joined");
				socket.send(JSON.stringify({
					"command": "leave",  // determines which handler will be used (see chat/routing.py)
					"room": roomId
				}));
			} else {
				// Join room
				console.log("hereere")
				$(this).addClass("joined");
				socket.send(JSON.stringify({
					"command": "join",
					"room": roomId
				}));
			}
		});
	});
/*

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
var loader = new THREE.OBJLoader()
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 10;
camera.position.y = 5;
var light = new THREE.DirectionalLight( 0xffffff, 1, 100 );
light.position.set( -5, 5, 10 );
scene.add( light)
loader.load("../static/images/models/bulbasaur/bulbasaur.obj",
        // onLoad callback
	// Here the loaded data is assumed to be an object
	function ( object ) {

		scene.add( object );

	},
	// called when loading is in progresses
	function ( xhr ) {

		console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

	},
	// called when loading has errors
	function ( error ) {

		console.log( 'An error happened' );

	}
);
function animate() {
    requestAnimationFrame( animate );
    cube.rotation.x += 0.01;
cube.rotation.y += 0.01;
	renderer.render( scene, camera );
}
animate()*/