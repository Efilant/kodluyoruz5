
import math
def euclideanDistance(point1,point2):
    x1,y1=point1 #ilk noktayı tanımlıyoruz
    x2,y2= point2 #ikinci noktayı tanımlıyoruz
    distance= math.sqrt((x2-x1)**2+(y2-y1)**2) #mesafeyi buluyoruz

points=[(3,4),(5,6),(7,10),(9,8)] #rastgele noktalar belirledik
distances=[] #bu listeye mesafeler eklenecek
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j]) #fonksiyonu çağırıyoruz
        distances.append(distance) #mesafeyi listeye ekliyoruz

min_distance = min(distances) # min olanı buluyoruz
print("Minimum mesafe:",min_distance)

