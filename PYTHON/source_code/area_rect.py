def rectangle_area(length, width):
   
    if length <= 0 or width <= 0:
        return "Invalid input"
    
    area = length * width
    return area


print(rectangle_area(5, 3))