"""
项目1测试代码模板
自动测试学生实现的koch_curve和minkowski_sausage函数。
"""
import unittest
from project1_koch_minkowski import koch_curve, minkowski_sausage

class TestFractalCurves(unittest.TestCase):
    def test_koch_curve_level1(self):
        start = (0, 0)
        end = (1, 0)
        lines = koch_curve(start, end, 1)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 4)
    def test_minkowski_sausage_level1(self):
        start = (0, 0)
        end = (1, 0)
        lines = minkowski_sausage(start, end, 1)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 8)
    # 可添加更多测试用例

if __name__ == "__main__":
    unittest.main()