"""
项目3测试代码模板
自动测试学生实现的apply_ifs_transform和generate_ifs_points函数。
"""
import unittest
from project3_ifs import apply_ifs_transform, generate_ifs_points

class TestIFS(unittest.TestCase):
    def test_apply_ifs_transform(self):
        point = (0.5, 0)
        transforms = [
            (0, 0, 0, 0.16, 0, 0),
            (0.85, 0.04, -0.04, 0.85, 0, 1.6)
        ]
        probs = [0.2, 0.8]
        new_point = apply_ifs_transform(point, transforms, probs)
        self.assertIsInstance(new_point, tuple)
        self.assertEqual(len(new_point), 2)
    def test_generate_ifs_points(self):
        transforms = [
            (0, 0, 0, 0.16, 0, 0),
            (0.85, 0.04, -0.04, 0.85, 0, 1.6)
        ]
        probs = [0.2, 0.8]
        xs, ys = generate_ifs_points((0.5, 0), transforms, probs, n_iter=200, skip=10)
        self.assertEqual(len(xs), len(ys))
        self.assertTrue(len(xs) > 0)

if __name__ == "__main__":
    unittest.main()