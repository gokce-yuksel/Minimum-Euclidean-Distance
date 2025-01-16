import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (7, 1), (3, 5)]

# 2. Öklid Mesafesi Fonksiyonunun Tanımlanması
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların Yazdırılması
print("Points:", points)
print("Distances:", distances)
print("Minimum Distance:", min_distance)
