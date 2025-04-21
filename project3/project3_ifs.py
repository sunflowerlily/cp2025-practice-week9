"""
项目3: 概率性迭代函数系统（IFS）分形生成模板
请补全下方函数，实现IFS分形生成与绘图。
"""
import matplotlib.pyplot as plt
import random

def apply_ifs_transform(point, transforms, probs):
    """
    随机选择并应用IFS仿射变换
    :param point: (x, y) 当前点
    :param transforms: [(a, b, c, d, e, f), ...] 仿射参数
    :param probs: [p1, p2, ...] 概率
    :return: 新点 (x, y)
    """
    # TODO: 实现仿射变换选择与应用
    pass

def generate_ifs_points(start, transforms, probs, n_iter=50000, skip=100):
    """
    生成IFS分形点集
    :param start: (x, y) 初始点
    :param transforms: 仿射参数列表
    :param probs: 概率列表
    :param n_iter: 总迭代次数
    :param skip: 跳过前skip个点
    :return: (xs, ys) 所有点坐标
    """
    # TODO: 实现IFS点集生成
    pass

def plot_ifs(xs, ys, filename):
    plt.figure(figsize=(5, 7))
    plt.scatter(xs, ys, s=0.1, alpha=0.6, color="g")
    plt.axis("equal")
    plt.axis("off")
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.1, dpi=300)
    plt.close()

if __name__ == "__main__":
    # 示例：生成并绘制巴恩斯利蕨
    fern_transforms = [
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.6),
        (0.2, -0.26, 0.23, 0.22, 0, 1.6),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    ]
    fern_probs = [0.01, 0.85, 0.07, 0.07]
    xs, ys = generate_ifs_points((0.5, 0), fern_transforms, fern_probs)
    plot_ifs(xs, ys, "barnsley_fern.png")

    # 示例：生成并绘制概率树（参数可自定义）
    tree_transforms = [
        (0.05, 0, 0, 0.6, 0, 0),
        (0.05, 0, 0, -0.5, 0, 1),
        (0.46, -0.32, 0.39, 0.38, 0, 0.6),
        (0.47, -0.15, 0.17, 0.42, 0, 1.1)
    ]
    tree_probs = [0.25, 0.25, 0.25, 0.25]
    xs, ys = generate_ifs_points((0.5, 0), tree_transforms, tree_probs)
    plot_ifs(xs, ys, "probability_tree.png")