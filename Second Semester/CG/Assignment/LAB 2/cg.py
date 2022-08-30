import matplotlib.pyplot as plt


def main():
    print("----- Program runs in sequence from Polygon -> Convex Test -> Turn Test -----\n")
    polygon()


def convexTest(data):
    print("\n------ Convex Test ------\n")
    points = data
    total_points = len(data)
    x = []
    y = []

    result = []
    for i in range(total_points):
      pi = points[i]
      xi = float(pi[0])
      x.append(xi)
      yi = float(pi[1])
      y.append(yi)

    for i in range(total_points):
      if(i == total_points-1):
        crossProduct = ((x[0]-x[i])*(y[1]-y[i]))-((x[1]-x[i])*(y[0]-y[i]))
      if(i == total_points-2):
        crossProduct = ((x[i+1]-x[i])*(y[0]-y[i]))-((x[0]-x[i])*(y[i+1]-y[i]))
      if(i <= total_points-3):
        crossProduct = ((x[i+1]-x[i])*(y[i+2]-y[i]))-((x[i+2]-x[i])*(y[i+1]-y[i]))

      if(crossProduct >= 0):
        result.append("Left Turn")
      else:
        result.append("Not")

    convex = True
    for item in result:
        if(item != "Left Turn"):
            convex = False
            break;
              
    if (convex == True):
      print("The Polygon is convex")
    else:
      print("The Polygon is not convex")

def polygon():
    total_points = int(input("Enter the number of co-ordinates the polygon will have: "))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title("Polygon")
    plt.grid()
     
    point = []
    cx = []
    cy =[]
    PI = []
    for i in range(total_points):
      
      Pi = input("Enter value of coordinate of polygon: ")
      point.append(Pi)

      pi = point[i].split(",")
      xi = float(pi[0])
      yi = float(pi[1])

      PI.append(pi)
      cx.append(xi)
      cy.append(yi)
      plt.scatter(xi, yi)
      plt.text(x=xi, y=yi, s="P" + str(i))
    cx.append(cx[0])
    cy.append(cy[0])
    plt.plot(cx, cy)
    plt.show()

    convexTest(PI)
    turnTest(PI)

def turnTest(data):
    print("\n------ Turn Test ------\n")
    points = data
    total_points = len(data)
    x = []
    y = []

    for i in range(total_points):
      pi = points[i]
      xi = float(pi[0])
      x.append(xi)
      yi = float(pi[1])
      y.append(yi)

    for i in range(total_points):
      if(i == total_points-1):
        print("Area for P"+str(i)+", P0 and P1")
        crossProduct = ((x[0]-x[i])*(y[1]-y[i]))-((x[1]-x[i])*(y[0]-y[i]))
      if(i == total_points-2):
        print("Area for P"+str(i)+", P"+str(i+1) +" and P0")
        crossProduct = ((x[i+1]-x[i])*(y[0]-y[i]))-((x[0]-x[i])*(y[i+1]-y[i]))
      if(i <= total_points-3):
        print("Area for P"+str(i)+", P"+str(i+1)+" and P"+str(i+2))
        crossProduct = ((x[i+1]-x[i])*(y[i+2]-y[i]))-((x[i+2]-x[i])*(y[i+1]-y[i]))

      if(crossProduct > 0):
        print("Left Turn\n")
      elif(crossProduct < 0):
        print("Right Turn\n")
      else:
        print("Collinear\n")

main()
