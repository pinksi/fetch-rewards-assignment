import ast
from flask import Flask, request, jsonify
from fetch_rewards import find_pixel_coords

app = Flask(__name__)

@app.route("/", methods=["POST"])
def test():
    data = request.get_json()
    img_size = eval(data["img_size"]) # convert string to tuple
    points = ast.literal_eval(data["corner_points"])
    result = find_pixel_coords(img_size, points)
    return jsonify(result)

if __name__=="__main__":
    app.run(host="localhost")