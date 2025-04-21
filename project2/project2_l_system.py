"""
项目2: L-System分形生成与绘图模板
请补全下方函数，实现L-System字符串生成与绘图。
"""
import matplotlib.pyplot as plt
import math

def apply_rules(axiom, rules, iterations):
    """
    生成L-System字符串
    :param axiom: 初始字符串
    :param rules: 规则字典，如{"F": "F+F--F+F"}
    :param iterations: 迭代次数
    :return: 最终字符串
    """
    # TODO: 实现L-System字符串生成
    pass

def draw_l_system(instructions, angle, step, start_pos=(0,0), start_angle=0, savefile=None):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串
    :param angle: 转角度数
    :param step: 步长
    :param start_pos: 起始坐标
    :param start_angle: 起始角度
    :param savefile: 保存文件名
    """
    # TODO: 实现L-System绘图
    pass

if __name__ == "__main__":
    # 示例：生成并绘制科赫曲线
    axiom = "F"
    rules = {"F": "F+F--F+F"}
    iterations = 3
    angle = 60
    step = 10
    instr = apply_rules(axiom, rules, iterations)
    draw_l_system(instr, angle, step, savefile="l_system_koch.png")

    # 示例：生成并绘制分形二叉树
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    iterations = 5
    angle = 45
    instr = apply_rules(axiom, rules, iterations)
    draw_l_system(instr, angle, step, savefile="fractal_tree.png")