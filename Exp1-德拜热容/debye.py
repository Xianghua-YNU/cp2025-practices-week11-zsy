import numpy as np
import matplotlib.pyplot as plt

# 物理常数
kB = 1.380649e-23  # 玻尔兹曼常数，单位：J/K

# 样本参数
V = 1000e-6  # 体积，1000立方厘米转换为立方米
rho = 6.022e28  # 原子数密度，单位：m^-3
theta_D = 428  # 德拜温度，单位：K

def integrand(x):
    """被积函数：x^4 * e^x / (e^x - 1)^2
    
    参数：
    x : float 或 numpy.ndarray
        积分变量
    
    返回：
    float 或 numpy.ndarray：被积函数的值
    """
    # 在这里实现被积函数
    return x**4 * np.exp(x) / (np.exp(x) - 1)**2

def gauss_quadrature(f, a, b, n):
    """实现高斯-勒让德积分
    
    参数：
    f : callable
        被积函数
    a, b : float
        积分区间的端点
    n : int
        高斯点的数量
    
    返回：
    float：积分结果
    """
    # 在这里实现高斯积分
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5*(x + 1)*(b - a) + a
    return 0.5*(b - a)*np.sum(w * f(t))

def cv(T):
    """计算给定温度T下的热容
    
    参数：
    T : float
        温度，单位：K
    
    返回：
    float：热容值，单位：J/K
    """
    # 在这里实现热容计算
    if T == 0:
        return 0.0
    upper_limit = theta_D / T
    result = gauss_quadrature(integrand, 0, upper_limit, n=50)
    return 9 * V * rho * kB * (T / theta_D)**3 * result

def plot_cv():
    """绘制热容随温度的变化曲线"""
    # 在这里实现绘图功能
    temperatures = np.linspace(5, 500, 200)
    heat_capacities = [cv(T) for T in temperatures]

    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, heat_capacities, label='Debye Model')
    plt.xlabel('Temperature (K)', fontsize=12)
    plt.ylabel('Heat Capacity (J/K)', fontsize=12)
    plt.title('Heat Capacity of Aluminum vs Temperature', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('heat_capacity_curve.png')
    plt.show()

def test_cv():
    """测试热容计算函数"""
    # 测试一些特征温度点的热容值
    test_temperatures = [5, 100, 300, 500]
    print("\n测试不同温度下的热容值：")
    print("-" * 40)
    print("温度 (K)\t热容 (J/K)")
    print("-" * 40)
    for T in test_temperatures:
        result = cv(T)
        print(f"{T:8.1f}\t{result:10.3e}")

def main():
    # 运行测试
    test_cv()
    
    # 绘制热容曲线
    plot_cv()

if __name__ == '__main__':
    main()
