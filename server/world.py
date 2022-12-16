import random
import time
import math
import ship_manager


rooms = []

def clamp(val, minn, maxx):
	return max(minn, min(val, maxx) )

def move_to_val(val, destination, speed):
	return clamp( destination, val - speed, val + speed )

def create_room():
	result = {}
	result["ships"] = []
	for i in range(2):
		result["ships"].append( {"x":random.uniform(0,2000), "y":random.uniform(0,2000)} )

	return result

def get_room_map(map_id):
	result = []
	for x in range(20):
		result.append( [] )
		for y in range(20):
			result[x].append("+")

	for ship in rooms[map_id]["ships"]:
		x = ship["x"]
		y = ship["y"]
		x /= 100
		y /= 100
		x = round(x)
		y = round(y)
		x = clamp(x, 0, 19)
		y = clamp(y, 0, 19)
		result[x][y] = "0"

	for ship in ship_manager.get_ships_in_room(map_id):
		x = ship["x"]
		y = ship["y"]
		x /= 100
		y /= 100
		x = round(x)
		y = round(y)
		x = clamp(x, 0, 19)
		y = clamp(y, 0, 19)
		result[x][y] = ship["id"]

	result_str = ""
	for x in range(20):
		for y in range(20):
			result_str += result[x][y] + " "
		result_str += "\n"
	return result_str

def reload_ship(id):
	ship_manager.reload_ship(id)


def cycle():
	print("cycle started")
	n = 0.1
	while True:
		for room in rooms:
			for ship in room["ships"]:
				ship["x"] = move_to_val(ship["x"], 1000 + math.sin(n)*500, 200)
				ship["y"] = move_to_val(ship["y"], 1000 + math.cos(n)*500, 200)
		
		n+=0.1

		ship_manager.cycle_ships()
		print("cycle passed")
		time.sleep(1)


for i in range(20):
	rooms.append( create_room() )
