# fetch-rewards-assignment

This program calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface.

### Input Specifications
The program will take two inputs:

#### 1. Image dimensions
This will be a tuple defining the height and width of the image in terms of pixel counts.

For example, an input for this parameter of (3, 3) means that the image has 3 rows and 3 columns.

#### 2. Corner Points
This will be a list of two-element tuples defining the x and y coordinates of the image corner points of the displayed image. It consists of four (x, y) pairs.
 
The specification will follow the following example format:

```
corner_points = [
    (1, 1), # (x, y)
    (3, 1), 
    (1, 3), 
    (3, 3)]  
```

### Output Specifications
This program return the x and y coordinates at which to plot each pixel in the input image such that the pixels are evenly spaced within the rectangle defined by the corner points.

```
Output:
{"pixel_coordinates":[
    [[1.0,3.0],[2.0,3.0],[3.0,3.0]],
    [[1.0,2.0],[2.0,2.0],[3.0,2.0]],
    [[1.0,1.0],[2.0,1.0],[3.0,1.0]]
    ]}
```

### Setup
Requirements:
- virtualenv
- python3.8.2

Setup:
- clone this repo
- make a virtualenv inside it e.g. virtualenv fetchr_env
- activate the venv e.g. source fetchr_env/bin/activate
- install the requirements pip install -r requirements.txt
- run the app e.g. `python app.py`
- app should be available at http://127.0.0.1:5000
### How to run this api
1. Use this curl command to get the pixel coordinates for the input:
```bash
curl --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "img_size": "(3, 3)",
    "corner_points": "[(3, 1), (1, 1), (3, 3), (1, 3)]"
}'
```
- "img_size" denotes the (1) Image dimensions 
- "corner_points" denotes (2) Corner Points.

### How to build docker image
Requirements:
- Docker

Build docker image: 
```bash
docker build -t fetch_reward .
```

Run docker image:
```bash
docker run -it -p 5000:5000 fetch_reward
```



