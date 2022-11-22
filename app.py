import ast
from flask import Flask, request, jsonify, abort
from loguru import logger
from fetch_rewards import find_pixel_coords

app = Flask(__name__)

@app.route("/", methods=["POST"])
def pixel_coordinate_calculator():
    data = request.get_json()
    img_size = eval(data["img_size"]) # convert string to tuple
    points = ast.literal_eval(data["corner_points"])

    # check if there are rows and cols value in img_size
    if not isinstance(img_size, tuple):# and len(img_size) != 2:
        logger.error("Incorrect image size given.")
        abort(422, description="Incorrect image size given.")
        
    # check if there are 4 corner points or not
    if len(points) != 4:
        logger.error("Insufficient corner points given.")
        abort(422, description="Insufficient corner points given.")

    try:
        result = find_pixel_coords(img_size, points)
        return jsonify({"pixel_coordinates":  result})
    except Exception as e:
        logger.error(f"Could not process the request. Exception {e} occurred.")
        abort(500)


if __name__=="__main__":
    app.run(host="localhost")