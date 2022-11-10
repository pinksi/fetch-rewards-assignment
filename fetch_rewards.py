import numpy as np
from loguru import logger


img_size = (3, 3) # row, col
corner_points = [ (3, 1), (1, 1), (3, 3), (1, 3)]

# img_size = (10, 12) # row, col
# corner_points = [(4.0, 1.5), (1.5, 1.5),  # (x, y)
#     (4.0, 8.0),(1.5, 8.0),  # (x, y)
#     ]

# determine bottom-left, top-right
def find_edge_points(points):
    x0 = min(list(map(lambda x: x[0], corner_points)))
    y0 = min(list(map(lambda x: x[1], corner_points)))

    x1 = max(list(map(lambda x: x[0], corner_points)))
    y1 = max(list(map(lambda x: x[1], corner_points)))
    bottom_left = (x0, y0)
    top_right = (x1, y1)
    return bottom_left, top_right

def find_pixel_coords(img_size, corner_points): 
    if (img_size and not corner_points):
        logger.error("Error occurred in finding corner points.")
        return []
    if (corner_points and not img_size):
        logger.error("Error occurred in finding image size.")
        return []

    row, col = img_size[0], img_size[1]
    bottom_left, top_right = find_edge_points(corner_points)
    x0, y0 = bottom_left[0], bottom_left[1] # bottom_left
    x1, y1 = top_right[0], top_right[1] # top-right

    # divide x-axis by col-size
    x = [round(i,2) for i in np.linspace(x0, x1, num=col, endpoint=True)]
    # divide y-axis by row-size
    y = [round(i,2) for i in np.linspace(y0, y1, num=row, endpoint=True)]

    pixel_coordinates = []
    for j in y[::-1]:
        new = []
        for i in x:
            new.append([i,j])
        pixel_coordinates.append(new)

    return list(pixel_coordinates)

# if __name__=="__main__":
#     res = find_pixel_coords(img_size, corner_points)
#     print(res)