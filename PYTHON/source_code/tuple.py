def show_coordinates(coords):

    if not isinstance(coords, tuple):
        print("Invalid coordinates")
        return

    print(f"X Coordinate: {coords[0]}")
    print(f"Y Coordinate: {coords[1]}")


coordinates = (10, 20)

show_coordinates(coordinates)