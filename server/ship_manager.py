import importlib
import glob

ships = []

def load_ships():
	for element in glob.glob("ship_script_*.py"):
		element = element.removesuffix(".py")
		module = importlib.import_module(element)
		ship_id = element.split("ship_script_")[1]

		ships.append( {
			"id": ship_id,
			"x": 0, 
			"y": 0, 
			"room_id": 0,
			"script": module,
			} )
		

def reload_ship(ship_id):
	for ship in ships:
		if ship["id"] == ship_id:
			importlib.reload( ship["script"] )

def cycle_ships():
	for ship in ships:
		new_coords = ship["script"].cycle()
		ship["x"] = new_coords["x"]
		ship["y"] = new_coords["y"]


def get_ships_in_room(room_id):
	result = []
	for ship in ships:
		if ship["room_id"] == room_id:
			result.append(ship)
	return result


load_ships()