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

# 你的测试代码
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([2, 2, 2])
print(p1)           # 应该输出 1 + 2x + 3x^2
p3 = p1 + p2
print(p3)           # 应该输出 3 + 4x + 5x^2