"""
项目4: Mandelbrot与Julia集分形生成模板
请补全下方函数，实现Mandelbrot与Julia集的生成与可视化。
"""
import matplotlib.pyplot as plt
import numpy as np

def mandelbrot_escape_time(c, max_iter):
    """
    计算Mandelbrot集逃逸时间
    :param c: 复数参数
    :param max_iter: 最大迭代次数
    :return: 逃逸时间
    """
    # TODO: 实现Mandelbrot逃逸时间算法
    pass

def julia_escape_time(z0, c, max_iter):
    """
    计算Julia集逃逸时间
    :param z0: 初始复数
    :param c: 参数c
    :param max_iter: 最大迭代次数
    :return: 逃逸时间
    """
    # TODO: 实现Julia逃逸时间算法
    pass

def plot_fractal(data, filename, cmap="viridis"):
    plt.figure(figsize=(6, 6))
    plt.imshow(data, cmap=cmap, origin="lower")
    plt.axis("off")
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.1, dpi=300)
    plt.close()

if __name__ == "__main__":
    # 示例：生成并绘制Mandelbrot集
    width, height = 400, 400
    max_iter = 100
    x_min, x_max = -2, 1
    y_min, y_max = -1.5, 1.5
    xs = np.linspace(x_min, x_max, width)
    ys = np.linspace(y_min, y_max, height)
    mandelbrot = np.zeros((height, width))
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            c = complex(x, y)
            mandelbrot[i, j] = mandelbrot_escape_time(c, max_iter)
    plot_fractal(mandelbrot, "mandelbrot_set.png")

    # 示例：生成并绘制Julia集
    c_list = [complex(-0.8, 0.156), complex(0.285, 0.01), complex(-0.4, 0.6)]
    for idx, c in enumerate(c_list):
        julia = np.zeros((height, width))
        for i, y in enumerate(ys):
            for j, x in enumerate(xs):
                z0 = complex(x, y)
                julia[i, j] = julia_escape_time(z0, c, max_iter)
        plot_fractal(julia, f"julia_set_c{idx+1}.png")