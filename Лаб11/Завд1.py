def find_points_on_curve(a, b, p):
    points = []
    for x in range(p):
        y_squared = (x**3 + a*x + b) % p
        for y in range(p):
            if (y * y) % p == y_squared:
                points.append((x, y))
    return points
# Параметри кривої
a = 1
b = 1
p = 23
# Знаходження всіх точок
points = find_points_on_curve(a, b, p)
print("Всі точки на кривій:")
print(points)