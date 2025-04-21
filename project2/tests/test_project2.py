"""
项目2测试代码模板
自动测试学生实现的apply_rules和draw_l_system函数。
"""
import unittest
from project2_l_system import apply_rules

class TestLSystem(unittest.TestCase):
    def test_koch_lsystem(self):
        axiom = "F"
        rules = {"F": "F+F--F+F"}
        instr = apply_rules(axiom, rules, 2)
        self.assertIn("+", instr)
        self.assertIn("-", instr)
        self.assertTrue(instr.count("F") > 0)
    def test_tree_lsystem(self):
        axiom = "0"
        rules = {"1": "11", "0": "1[0]0"}
        instr = apply_rules(axiom, rules, 3)
        self.assertIn("[", instr)
        self.assertIn("]", instr)
        self.assertTrue(instr.count("1") > 0)

if __name__ == "__main__":
    unittest.main()