# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula]

x,y,z = [],[],[]
NrDist = []
cord = int(input("Enter the number of co-ordinates: "))

for i in range(cord):
    xi = int(input("Enter the x co-ordinate: "))
    x.append(xi)
    yi = int(input("Enter the y co-ordinate: "))
    y.append(yi)
    zi = int(input("Enter the z co-ordinate: "))
    z.append(zi)
    
for i in range(cord):
    
    j = i + 1
    while j < cord:
        dist = ((x[i] - x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2)**0.5
        NrDist.append(dist)
        j += 1
    
    for k in range(len(NrDist)):
        if NrDist[k] == min(NrDist):
            print("The nearest neighbour of", x[i], y[i], z[i], "is", x[k+i+1], y[k+i+1], z[k+i+1])
            
    NrDist.clear()        