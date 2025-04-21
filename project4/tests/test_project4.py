"""
项目4测试代码模板
自动测试学生实现的mandelbrot_escape_time和julia_escape_time函数。
"""
import unittest
from project4_mandelbrot_julia import mandelbrot_escape_time, julia_escape_time

class TestFractalDynamics(unittest.TestCase):
    def test_mandelbrot_escape(self):
        c_in = complex(0, 0)
        c_out = complex(2, 2)
        max_iter = 50
        self.assertEqual(mandelbrot_escape_time(c_in, max_iter), max_iter)
        self.assertTrue(mandelbrot_escape_time(c_out, max_iter) < max_iter)
    def test_julia_escape(self):
        z0 = complex(0, 0)
        c = complex(-0.8, 0.156)
        max_iter = 50
        self.assertTrue(julia_escape_time(z0, c, max_iter) > 0)
        self.assertTrue(julia_escape_time(complex(2, 2), c, max_iter) < max_iter)

if __name__ == "__main__":
    unittest.main()