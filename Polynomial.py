class Polynomial:
    def __init__(self, coefficients):
        # coefficients 是一个列表，比如 [1, 2, 3] 代表 1 + 2x + 3x^2
        self.coeffs = coefficients 

    def __str__(self):
        # 目标：让它打印出来像数学公式，比如 "1 + 2x + 3x^2"
        # 提示：你可以用循环，把列表里的数字和 x 拼起来
        terms = []
        for i in range(1,len(self.coeffs)+1):
            if i ==1:
                terms.append(f"{self.coeffs[i-1]}")
            elif i ==2:
                terms.append(f"{self.coeffs[i-1]}x")
            else:
                terms.append(f"{self.coeffs[i-1]}x^{i-1}")
        return " + ".join(terms)

    def __add__(self, other):
        # 目标：实现两个多项式相加，返回一个新的 Polynomial 对象
        # 提示：把两个列表的对应位置相加，长度不够的补0
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        if len(self.coeffs) < max_len:
            self.coeffs += [0] * (max_len - len(self.coeffs))
        elif len(other.coeffs) < max_len:
            other.coeffs += [0] * (max_len - len(other.coeffs))
        for j in range(max_len):
            new_coeffs.append(self.coeffs[j] + other.coeffs[j])
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        # 目标：实现两个多项式相减，返回一个新的 Polynomial 对象
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        if len(self.coeffs) < max_len:
            self.coeffs += [0] * (max_len - len(self.coeffs))
        elif len(other.coeffs) < max_len:
            other.coeffs += [0] * (max_len - len(other.coeffs))
        for j in range(max_len):
            new_coeffs.append(self.coeffs[j] - other.coeffs[j])
        return Polynomial(new_coeffs)

    def derivative(self):
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(self.coeffs[i] * i)
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        # 结果的长度是两个多项式长度之和减 1
        new_len = len(self.coeffs) + len(other.coeffs) - 1
        # 先建一个全为 0 的新列表
        new_coeffs = [0] * new_len
        
        # 两个 for 循环遍历所有系数对
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                # i*j 对应的结果，放在 i+j 的位置上
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
                
        return Polynomial(new_coeffs)

# 你的测试代码
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([2, 2, 2])
print(p1)           # 应该输出 1 + 2x + 3x^2
p3 = p1 + p2
print(p3)           # 应该输出 3 + 4x + 5x^2

p = Polynomial([1, 2, 3])
print("原多项式:", p)       # 应该输出 1 + 2x + 3x^2
print("求导后:", p.derivative())  # 应该输出 2 + 6x

p1 = Polynomial([1, 2])      # 1 + 2x
p2 = Polynomial([3, 4])      # 3 + 4x
print("乘法测试:", p1 * p2)   # 看看是不是 3 + 10x + 8x^2