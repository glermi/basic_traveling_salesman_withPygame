from traceback import print_list
import pygame,sys

import time
import random
import os
from points import Point


#uzaklık matrisi tanımlama:
#(excelden veri çekme ile de dinamik yapılabilir, 
# veya pythagorean teoremine göre uzaklık hesaplama fonksyionu yazılabilir
# biz burada distance matrixle yapıyoruz, excel halini de araştır.)
distance_matrix =[[0,2,6,7,8,9,4,7,9,2,],
                  [2,0,4,6,8,2,3,7,8,3,],
                  [6,4,0,4,7,1,9,3,6,2,],
                  [7,6,4,0,9,4,7,1,2,5,],
                  [8,8,7,9,0,8,3,6,8,1,],
                  [9,2,1,4,8,0,6,2,7,3,],
                  [4,3,9,7,3,6,0,2,8,1,],
                  [7,7,3,1,6,2,2,0,3,6,],
                  [9,8,6,2,8,7,8,3,0,7,],
                  [2,3,2,5,1,3,1,6,7,0,],
                 ]
#pygamede ekranı ortalamak için:
os.environ["SDL_VIDEO_CENTERED"]='1'

# açılacak ekran boyutları:
width,height=700,700

#görselleştirme renkleri:
black = ( 0, 0, 0 ) #screen
white = ( 255, 255, 255 ) #lines
green = ( 0, 255, 25 ) #en kısa yolu gösterir

pygame.init()
pygame.display.set_caption("Traveling Salesman Problem") #açılacak ekranın titlei
pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((width,height))

#değişkenlerin tanımlanması:
points = [] #nokta kordinatlarının tutuluduğu array
offset_screen = 50 
smallest_path = []
record_distance = 0 #en kısa yol (integer valued)
number_of_points = 10 #nodesayısı

#rastgele noktaları ekranda gösterme:
for n in range (number_of_points):

    x = random.randint(offset_screen,width-offset_screen) #width
    y = random.randint(offset_screen,height-offset_screen) #height

    point = Point(x,y) #point i diğer points.py den class import!
    points.append(point) 

#noktaların yerlerini karıştırma işlemi:
def shuffle(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

#distance matrixten uzaklıkları alma işlemi yapılır:
def get_distance (point_list, distance_matrix):
    total = 0
    #i = 0 ken a noktası demektir.
    #indislere dikkat ederek distance hesaplanır:
    for i in range (len(point_list)-1):
            for j in range (len(distance_matrix)-1):
                distance = distance_matrix[i][j]
                total += distance
    return total

#başlangıç distancei belirlenir:
dist = get_distance(points,distance_matrix)

#en kısa yol değişkeni
record_distance = dist

smallest_path = points.copy()

#buradan sonra pygame calistirilir:
run  = True
while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #noktaları ve çizgileri çizdiririz: (kooridinatlara göre değişir)        
    for n in range(len(points)):
        pygame.draw.circle(screen, white, (points[n].x , points[n].y) ,10)

    #pointler random alınıyor:
    a=random.randint(0,len(points)-1)
    b=random.randint(0,len(points)-1)

    #pointler shufflelanıyor ve uzaklık hesaplanıyor:
    shuffle (points, a, b)
    dist = get_distance(points, distance_matrix)

    #andaki uzaklık rekordan küçükse uzaklık ve en kısa yol ataması yapılır:
    if dist < record_distance:
        record_distance = dist
        smallest_path =points.copy()

    #çizgiler çizilir:
    for m in range (len(points)-1):
        pygame.draw.line(screen,white, (points[m].x , points[m].y), (points[m+1].x , points[m+1].y) ,3)

    #en kısa yol çizilir:
    for m in range (len(smallest_path)-1):
        pygame.draw.line(screen,green, (smallest_path[m].x , smallest_path[m].y), (smallest_path[m+1].x , smallest_path[m+1].y))

    pygame.display.update()

print("En kısa yol:", record_distance)
pygame.quit()