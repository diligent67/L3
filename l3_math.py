#Лаба 3
import math

#  радиус
R_cm = float(input())
R_m = R_cm / 100

#  Длина и площадь окружности
L_cm = 2 * math.pi * R_cm
L_m = 2 * math.pi * R_m

S_cm = math.pi * (R_cm ** 2)
S_m = math.pi * (R_m ** 2)

print(L_cm)
print(L_m)
print(S_cm)
print(S_m)

#  Стороны вписанных фигур (квадрат и равносторонний треугольник)
in_square_cm = R_cm * math.sqrt(2)
in_square_m = R_m * math.sqrt(2)

in_triangle_cm = R_cm * math.sqrt(3)
in_triangle_m = R_m * math.sqrt(3)

print(in_square_cm)
print(in_square_m)
print(in_triangle_cm)
print(in_triangle_m)

#  Стороны описанных фигур (квадрат, равносторонний треугольник и правильный восьмиугольник)
out_square_cm = 2 * R_cm
out_square_m = 2 * R_m

out_triangle_cm = 2 * R_cm * math.sqrt(3)
out_triangle_m = 2 * R_m * math.sqrt(3)

out_octagon_cm = 2 * R_cm * math.tan(math.pi / 8)
out_octagon_m = 2 * R_m * math.tan(math.pi / 8)

print(out_square_cm)
print(out_square_m)
print(out_triangle_cm)
print(out_triangle_m)
print(out_octagon_cm)
print(out_octagon_m)
