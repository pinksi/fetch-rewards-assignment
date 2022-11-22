import unittest
from fetch_rewards import  find_edge_points, find_pixel_coords

class TestFetchRewards(unittest.TestCase):
    def test_find_edge_points(self):
        corner_points = [(3, 1), (1, 1), (3, 3), (1, 3)]
        res1, res2 = find_edge_points(corner_points)
        self.assertEqual(res1, (1, 1))
        self.assertEqual(res2, (3, 3))

    def test_find_pixel_coords(self):
        img_size = (3, 3)
        corner_points = [(3, 1), (1, 1), (3, 3), (1, 3)]
        result = find_pixel_coords(img_size, corner_points)
        output = [
                    [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
                    [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
                    [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
                ]
        self.assertEqual(result, output)

if __name__=="__main__":
    unittest.main()
    