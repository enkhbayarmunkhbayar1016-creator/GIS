# ==========================================
# Section 3.8: Hands-On Experience with Python
# Code 3.18: Sum-up calculations
# ==========================================

# 1. 1-ээс 100 хүртэлх тооны нийлбэр (for давталт)
numbers = range(1, 101, 1)
sum1, sum2, sum3 = 0, 0, 0

for i in numbers:
    sum1 = sum1 + i

print("sum1:", sum1)

# 2. 1-ээс 100 хүртэлх тэгш тоонуудын нийлбэр (while давталт)
i = 0
while i < 101:
    if i % 2 == 0:
        sum2 = sum2 + i
    i += 1

print("sum2:", sum2)

# 3. 0-ээс 99 хүртэлх сондгой тоонуудын нийлбэр (for давталт)
for i in range(100):
    if i % 2 == 1:
        sum3 += i

print("sum3:", sum3)
