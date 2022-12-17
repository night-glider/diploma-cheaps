import random
from flask import Flask, request, jsonify
import threading
import os

import world

app = Flask(__name__, static_url_path='', static_folder='static')

@app.get("/maps")
def get_map():
	room_id = int( request.args.get('id') )
	return jsonify(world.get_room_map(room_id))

@app.get("/tick_data")
def get_tick_data():
	return jsonify(world.get_tick_data())

@app.get("/ship_code")
def get_ship_code():
	ship_id = ( request.args.get("id") )
	with open("ship_script_" + ship_id + ".py", "r") as f:
		data = f.read()

	return (data)

@app.post("/ship_code")
def post_ship_code():
	ship_id = ( request.args.get("id") )
	code = request.data.decode("utf-8")
	with open("ship_script_" + ship_id + ".py", "w") as f:
		data = f.write(code)

	world.reload_ship(ship_id)

	return "ok"




world_thread = threading.Thread(target=world.cycle)
world_thread.start()

# Bind to PORT if defined, otherwise default to 5000.
port = int( os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)