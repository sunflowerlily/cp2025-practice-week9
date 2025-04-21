"""
项目1: 科赫曲线与闵可夫斯基香肠曲线生成模板
请补全下方函数，实现分形曲线的生成与绘图。
"""
import matplotlib.pyplot as plt
import math

def koch_curve(start, end, level):
    """
    递归生成科赫曲线所有线段
    :param start: (x, y) 起点
    :param end: (x, y) 终点
    :param level: 递归层数
    :return: [(x0, y0, x1, y1), ...] 所有线段
    """
    # TODO: 实现科赫曲线生成
    pass

def minkowski_sausage(start, end, level):
    """
    递归生成闵可夫斯基香肠曲线所有线段
    :param start: (x, y) 起点
    :param end: (x, y) 终点
    :param level: 递归层数
    :return: [(x0, y0, x1, y1), ...] 所有线段
    """
    # TODO: 实现闵可夫斯基香肠曲线生成
    pass

def plot_lines(lines, filename):
    plt.figure(figsize=(8, 3))
    for x0, y0, x1, y1 in lines:
        plt.plot([x0, x1], [y0, y1], color="b")
    plt.axis("equal")
    plt.axis("off")
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.1, dpi=300)
    plt.close()

if __name__ == "__main__":
    # 示例：生成并绘制科赫曲线
    start = (0, 0)
    end = (1, 0)
    level = 3  # 可调整
    koch_lines = koch_curve(start, end, level)
    plot_lines(koch_lines, "koch_curve.png")

    # 示例：生成并绘制闵可夫斯基香肠曲线
    minkowski_lines = minkowski_sausage(start, end, 2)
    plot_lines(minkowski_lines, "minkowski_sausage.png")