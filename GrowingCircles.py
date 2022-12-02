import sys
import math as m
class Circle():
    def __init__(self,xc,yc,ra):
        self.x = xc
        self.y = yc
        self.r = ra
        self.status = 1
    def set_status_to_zero(self):
        self.status = 0 
    def get_distance(self,other):
        if self.x == other.x:
            distance = abs(self.y-other.y)-self.r-other.r
        elif self.y == other.y:
            distance = abs(self.x-other.x)-self.r-other.r
        else:
            distance = ((self.x-other.x)**2+(self.y-other.y)**2)**0.5 - self.r-other.r
        return round(distance,3)      
def end_of_process(list_of_circles):
    for i in range(len(list_of_circles)):
        if list_of_circles[i].status == 1:
            return 0
    return 1
try:
    print("Input filename")
    name = input()
    file = open(name,"r")
    n = int(file.readline())
    list_of_circles = [Circle(0,0,0) for i in range(n)]
    for i in range(n):
        list_of_circles[i].x,list_of_circles[i].y,list_of_circles[i].r = map(float,file.readline().split())
        if list_of_circles[i].r < 0:
            print("Error! Wrong data")
            sys.exit(1)
        if (list_of_circles[i].x == sys.float_info.max or list_of_circles[i].y == sys.float_info.max or list_of_circles[i].r == sys.float_info.max):
            print("Working with overflowed floats!!!")
    list_of_frozen_pairs = []
    while end_of_process(list_of_circles)!=1:
        list_of_distances=[]
        list_of_indexes = []
        for j in range(n):
            for k in range(j+1,n,1):
                if (j,k) not in list_of_frozen_pairs:
                    list_of_distances.append(list_of_circles[j].get_distance(list_of_circles[k]))
                    list_of_indexes.append([j,k])
        min_dist  = min(list_of_distances)
        ind = list_of_distances.index(min_dist)
        j_f = list_of_indexes[ind][0]
        k_f = list_of_indexes[ind][1]
        if list_of_circles[j_f].status == 0 and list_of_circles[k_f].status!=0:
            list_of_circles[k_f].r += min_dist
            list_of_circles[k_f].status = 0
            for i in range(n):
                if list_of_circles[i].status!=0:
                    list_of_circles[i].r += min_dist
        elif list_of_circles[k_f].status == 0 and list_of_circles[j_f].status!=0:
            list_of_circles[j_f].r += min_dist
            list_of_circles[j_f].status = 0
            for i in range(n):
                if list_of_circles[i].status!=0:
                    list_of_circles[i].r += min_dist
        else:
            list_of_circles[j_f].r += min_dist/2
            list_of_circles[k_f].r += min_dist/2
            list_of_circles[j_f].status = 0
            list_of_circles[k_f].status = 0
            for i in range(n):
                if list_of_circles[i].status!=0:
                    list_of_circles[i].r += min_dist/2
        list_of_frozen_pairs.append((j_f,k_f))
    for i in range(n):
        print("R_",i,"=",round(list_of_circles[i].r,3),sep='')
    file.close()
except IOError:
    print("File is already opened")
