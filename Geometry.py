import math
import sys
import unittest

class Point (object):

    #constructor
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    
    # get dist to another point object
    def distance(self, other):
        #distance formula
        return math.sqrt(((self.x - other.x)**2)+ ((self.y - other.y)**2) + ((self.z - other.z)**2))

    #string representation of a Point object
    def __str__ (self):

         return '(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', '+ str(float(self.z))+ ')'


    #test for equality
    def __eq__ (self,other):

        tol = 1.0e-6
        return ((abs(self.x - other.x))< tol) and ((abs(self.y - other.y))< tol) and ((abs(self.z - other.z))< tol)



class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x,y,z)
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center: '+ self.center.__str__()+', '+ 'Radius: '+ str(float(self.radius))


    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return 4*math.pi*(self.radius**2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return (4/3)*(math.pi)*(self.radius**3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p)<self.radius


    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        return (self.center.distance(other.center) + other.radius) <self.radius


    # determine if another Sphere is strictly outside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_outside_sphere (self, other):
        return (self.center.distance(other.center) - other.radius) >self.radius



    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):

        yes = True
        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        half_s = (a_cube.side/2)


        p = [Point(x+half_s, y+half_s, z+half_s), #top left corner of upper face of other cube
        Point(x-half_s, y+half_s, z+half_s), #top right corner of upper face of other cube
        Point(x-half_s, y-half_s, z+half_s), # bottom left corner of upper face of other cube
        Point(x+half_s, y-half_s, z+half_s), # bottom right corner of upper face of other cube
        Point(x-half_s, y+half_s, z-half_s), #top left corner of lower face of other cube
        Point(x+half_s, y-half_s, z-half_s), #bottom right corner of lower face of other cube
        Point(x-half_s, y-half_s, z-half_s), #bottom left corner of lower face of other cube
        Point(x+half_s, y+half_s, z-half_s)] # top right corner of lower face of other cube

        #loops through all corners and invokes is_inside_point method for each one to check if all are in sphere
        for point in p:
            if (not self.is_inside_point(point)):
                yes = False

        return yes



    # determine if a Cube is strictly outside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # outside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_outside_cube (self, a_cube):

        yes = True
        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        half_s = (a_cube.side/2)

        p = [Point(x+half_s, y+half_s, z+half_s), #top left corner of upper face of other cube
        Point(x-half_s, y+half_s, z+half_s), #top right corner of upper face of other cube
        Point(x-half_s, y-half_s, z+half_s), # bottom left corner of upper face of other cube
        Point(x+half_s, y-half_s, z+half_s), # bottom right corner of upper face of other cube
        Point(x-half_s, y+half_s, z-half_s), #top left corner of lower face of other cube
        Point(x+half_s, y-half_s, z-half_s), #bottom right corner of lower face of other cube
        Point(x-half_s, y-half_s, z-half_s), #bottom left corner of lower face of other cube
        Point(x+half_s, y+half_s, z-half_s)] # top right corner of lower face of other cube

        #loops through all corners and invokes opposite of is_inside_point method for each one to check if all are not in sphere
        for point in p:
            if (self.is_inside_point(point)):
                yes = False
        

        return yes


    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):

        yes = True

        #fills list with all extreme points of cylinder
        p = [Point(a_cyl.x+a_cyl.radius, a_cyl.y, a_cyl.z-(a_cyl.height-2)), #bottom east point
        Point(a_cyl.x, a_cyl.y+a_cyl.radius, a_cyl.z-(a_cyl.height-2)), # bottom north point
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom north east
        Point(a_cyl.x-a_cyl.radius, a_cyl.y, a_cyl.z-(a_cyl.height-2)), # bottom west point
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom north west
        Point(a_cyl.x, a_cyl.y-a_cyl.radius, a_cyl.z-(a_cyl.height-2)), # bottom south point
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom south west
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom south east
        Point(a_cyl.x+a_cyl.radius,a_cyl.y,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x,a_cyl.y+a_cyl.radius,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x-a_cyl.radius,a_cyl.y,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x,a_cyl.y-a_cyl.radius,a_cyl.z+(a_cyl.height-2)),
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top north east
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top north west
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top south west
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)) #top south east
        ]

        #loops through list of extreme points, and sees if each one is within the sphere
        for extreme in p:
            if (not self.is_inside_point(extreme)):
                yes = False

        return yes


    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean

    def does_intersect_sphere (self, other):
        return (not self.is_inside_sphere(other)) and (not self.is_outside_sphere(other))



    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):


        #returns boolean True if both methods are False
        return (not self.is_inside_cube(a_cube)) and (not self.is_outside_cube(a_cube))



    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        
        #returns a cube with diagonal equal to the radius of the sphere.
        return Cube(self.x,self.y,self.z,((2*self.radius)/math.sqrt(3))) 










class Cube (object):

    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):

        self.center = Point(x,y,z)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):

        return 'Center: '+ self.center.__str__()+', '+ 'Side: '+ str(float(self.side))


    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):

        return 6*(self.side**2)

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):

        return (self.side**3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):

        x_cen = self.x
        y_cen = self.y
        z_cen = self.z
        half_s = (self.side/2)
        

        #defines critical points of the cube
        xmax,xmin = x_cen+half_s, x_cen-half_s
        ymax,ymin = y_cen+half_s, y_cen-half_s
        zmax,zmin = z_cen+half_s, z_cen-half_s

        px = p.x
        py = p.y
        pz = p.z 

        #returns true if all points of P lie within the cube's critical points
        return ((xmin<px<xmax) and (ymin<py<ymax) and (zmin<pz<zmax))

 
        

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):

        yes = True

        sx_cen = a_sphere.x
        sy_cen = a_sphere.y
        sz_cen = a_sphere.z
        r = a_sphere.radius

        #creates list of all extreme points in sphere
        extremes = [Point(sx_cen, sy_cen + r, sz_cen),
        Point(sx_cen, sy_cen - r, sz_cen),
        Point(sx_cen - r, sy_cen, sz_cen),
        Point(sx_cen + r , sy_cen, sz_cen),
        Point(sx_cen,sy_cen, sz_cen +r),
        Point(sx_cen, sy_cen, sz_cen - r)]

        #loops through list to see if any of the extremes are outside the cube
        for point in extremes:
            if (not self.is_inside_point(point)):
                yes = False

        return yes
            

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        yes = True
        x = other.x
        y = other.y
        z = other.z
        half_s = (other.side/2)

        p = [Point(x+half_s, y+half_s, z+half_s), #top left corner of upper face of other cube
        Point(x-half_s, y+half_s, z+half_s), #top right corner of upper face of other cube
        Point(x-half_s, y-half_s, z+half_s), # bottom left corner of upper face of other cube
        Point(x+half_s, y-half_s, z+half_s), # bottom right corner of upper face of other cube
        Point(x-half_s, y+half_s, z-half_s), #top left corner of lower face of other cube
        Point(x+half_s, y-half_s, z-half_s), #bottom right corner of lower face of other cube
        Point(x-half_s, y-half_s, z-half_s), #bottom left corner of lower face of other cube
        Point(x+half_s, y+half_s, z-half_s)] # top right corner of lower face of other cube
      
      
        #loops through list to see if any of the extremes are outside the cube
        for point in p:
            if (not self.is_inside_point(point)):
                yes = False

        return yes

    # determine if another Cube is strictly outside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_outside_cube (self, other):

        yes = True
        x = other.x
        y = other.y
        z = other.z
        half_s = (other.side/2)

        p = [Point(x+half_s, y+half_s, z+half_s), #top left corner of upper face of other cube
        Point(x-half_s, y+half_s, z+half_s), #top right corner of upper face of other cube
        Point(x-half_s, y-half_s, z+half_s), # bottom left corner of upper face of other cube
        Point(x+half_s, y-half_s, z+half_s), # bottom right corner of upper face of other cube
        Point(x-half_s, y+half_s, z-half_s), #top left corner of lower face of other cube
        Point(x+half_s, y-half_s, z-half_s), #bottom right corner of lower face of other cube
        Point(x-half_s, y-half_s, z-half_s), #bottom left corner of lower face of other cube
        Point(x+half_s, y+half_s, z-half_s)] # top right corner of lower face of other cube


        #loops through list to see if any of the extremes are inside the cube
        for point in p:
            if self.is_inside_point(point):
                yes = False

        return yes

    

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):

        yes = True

        #fills list with all extreme points of cylinder
        p = [Point(a_cyl.x+a_cyl.radius, a_cyl.y, a_cyl.z-(a_cyl.height-2)), #bottom east point
        Point(a_cyl.x, a_cyl.y+a_cyl.radius, a_cyl.z-(a_cyl.height-2)), # bottom north point
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom north east
        Point(a_cyl.x-a_cyl.radius, a_cyl.y, a_cyl.z-(a_cyl.height-2)), # bottom west point
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom north west
        Point(a_cyl.x, a_cyl.y-a_cyl.radius, a_cyl.z-(a_cyl.height-2)), # bottom south point
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom south west
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z-(a_cyl.height-2)), #bottom south east
        Point(a_cyl.x+a_cyl.radius,a_cyl.y,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x,a_cyl.y+a_cyl.radius,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x-a_cyl.radius,a_cyl.y,a_cyl.z+(a_cyl.height-2)),
        Point(a_cyl.x,a_cyl.y-a_cyl.radius,a_cyl.z+(a_cyl.height-2)),
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top north east
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y+a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top north west
        Point(((a_cyl.x-a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)), #top south west
        Point(((a_cyl.x+a_cyl.radius+a_cyl.x)/2)+(a_cyl.radius/2), ((a_cyl.y-a_cyl.radius+a_cyl.y)/2)+(a_cyl.radius/2),a_cyl.z+(a_cyl.height-2)) #top south east
        ]

        #loops through list of extreme points, and sees if each one is within the sphere
        for extreme in p:
            if (not self.is_inside_point(extreme)):
                yes = False

        return yes

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        
        return ((not self.is_outside_cube(other)) and (not self.is_inside_cube(other))) or ((not other.is_outside_cube(self)) and (not other.is_inside_cube(self)))

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):

        volume = 0.0

        if self.does_intersect_cube(other):
            inter_lenx = 0
            inter_leny = 0
            inter_lenz = 0

            #sets critical values of cube a (self)
            A_zmax = self.z+(self.side/2)
            A_zmin = self.z-(self.side/2)
            A_xmax = self.x+(self.side/2)
            A_xmin = self.x-(self.side/2)
            A_ymax = self.y+(self.side/2)
            A_ymin = self.y-(self.side/2)    

            #sets critical values of cube b (other)
            B_zmax = other.z+(other.side/2)
            B_zmin = other.z-(other.side/2)
            B_xmax = other.x+(other.side/2)
            B_xmin = other.x-(other.side/2)
            B_ymax = other.y+(other.side/2)
            B_ymin = other.y-(other.side/2) 


            #compares critical values in all axises to determine dimensions of intersectional volume
            if B_xmin<A_xmax<B_xmax:
                inter_lenx = A_xmax-B_xmin

            if A_xmin<B_xmax<A_xmax:
                inter_lenx = B_xmax-A_xmin

            if B_zmin<A_zmax<B_zmax:
                inter_lenz = A_zmax-B_zmin

            if A_zmin<B_zmax<A_zmax:
                inter_lenz = B_zmax-A_zmin

            if B_ymin<A_ymax<B_ymax:
                inter_leny = A_ymax-B_ymin

            if A_ymin<B_ymax<A_ymax:
                inter_leny = B_ymax-A_ymin

            #computes volume given intersectional dimensions
            volume = (inter_lenx)*(inter_leny)*(inter_lenz)
    
        return volume

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):

        return Sphere(self.x,self.y,self.z, (self.side/2))


class Cylinder (object):

    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x,y,z)
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
        
    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):

        return 'Center: '+ self.center.__str__()+', '+ 'Radius: '+ str(float(self.radius))+', '+ 'Height: '+ str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        return ((2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius**2)))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        return (math.pi*(self.radius**2)*self.height)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):

        yes = True
        zmin = self.z-(self.height/2)
        zmax = self.z+(self.height/2)

        
        if  (Point(p.x,p.y,self.z).distance(self.center)<self.radius):
            if not (zmin<p.z<zmax):
                yes = False
        else:
            yes = False

        return yes
        

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        yes = True

        sx_cen = a_sphere.x
        sy_cen = a_sphere.y
        sz_cen = a_sphere.z
        r = a_sphere.radius

        #list of extreme values 
        extremes = [Point(sx_cen, sy_cen + r, sz_cen),
        Point(sx_cen, sy_cen - r, sz_cen),
        Point(sx_cen - r, sy_cen, sz_cen),
        Point(sx_cen + r , sy_cen, sz_cen),
        Point(sx_cen,sy_cen, sz_cen +r),
        Point(sx_cen, sy_cen, sz_cen - r)]

        #loops through list to see if they are contained
        for point in extremes:
            if (not self.is_inside_point(point)):
                yes = False

        return yes


    

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):

        yes = True

        x = a_cube.x
        y = a_cube.y
        z = a_cube.z
        half_s = (a_cube.side/2)

        p = [Point(x+half_s, y+half_s, z+half_s), #top left corner of upper face of other cube
        Point(x-half_s, y+half_s, z+half_s), #top right corner of upper face of other cube
        Point(x-half_s, y-half_s, z+half_s), # bottom left corner of upper face of other cube
        Point(x+half_s, y-half_s, z+half_s), # bottom right corner of upper face of other cube
        Point(x-half_s, y+half_s, z-half_s), #top left corner of lower face of other cube
        Point(x+half_s, y-half_s, z-half_s), #bottom right corner of lower face of other cube
        Point(x-half_s, y-half_s, z-half_s), #bottom left corner of lower face of other cube
        Point(x+half_s, y+half_s, z-half_s)] # top right corner of lower face of other cube

        for point in p:
            if (not self.is_inside_point(point)):
                yes = False

        return yes

        

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        yes = False
        zmin = self.z-(self.height/2)
        zmax = self.z+(self.height/2)

        # checks if other is contained within the Z min and maxes, as well as if the 
        # 2d cross-section of other at self.z is inside the range of self's radius.
        if (Point(other.x,other.y,self.z).distance(self.center) + other.radius) < self.radius:
            if (zmin<(other.z-(other.height/2))) and ((other.z+(other.height/2))<zmax):
                yes = True

        return yes



    # determine if another Cylinder is strictly outside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_outside_cylinder (self, other):

        zmin = self.z-(self.height/2)
        zmax = self.z+(self.height/2)

        other_zmin = other.z-(other.height/2)
        other_zmax = other.z+(other.height/2)

        # returns opposite conditions of inside method above
        return ((Point(other.x,other.y,self.z).distance(self.center) - other.radius) > self.radius) or (other_zmin>zmax) or (other_zmax<zmin)


    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):

        return ((not self.is_inside_cylinder(other)) and (not self.is_outside_cylinder(other)))

    

def main():

    
    f = sys.stdin.readlines()


    p = f[0].strip().split(' ')
    q = f[1].strip().split(' ')

    sA = f[2].strip().split(' ')
    sB = f[3].strip().split(' ')

    cA = f[4].strip().split(' ')
    cB = f[5].strip().split(' ')

    cyA = f[6].strip().split(' ')
    cyB = f[7].strip().split(' ')


    P = Point(float(p[0]), float(p[1]), float(p[2]))
    Q = Point(float(q[0]), float(q[1]), float(q[2]))
    origin = Point(0,0,0)

    sphere_A = Sphere(float(sA[0]), float(sA[1]), float(sA[2]), float(sA[3]))
    sphere_B = Sphere(float(sB[0]), float(sB[1]), float(sB[2]), float(sB[3]))

    cube_A = Cube(float(cA[0]), float(cA[1]), float(cA[2]), float(cA[3]))
    cube_B = Cube(float(cB[0]), float(cB[1]), float(cB[2]), float(cB[3]))

    cyl_A = Cylinder(float(cyA[0]), float(cyA[1]), float(cyA[2]), float(cyA[3]), float(cyA[4]))
    cyl_B = Cylinder(float(cyB[0]), float(cyB[1]), float(cyB[2]), float(cyB[3]), float(cyB[4]))



    if P.distance(origin)>Q.distance(origin):
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')


    if sphere_A.is_inside_point(P):
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')


    if sphere_A.is_inside_sphere(sphere_B):
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')


    if sphere_A.is_inside_cube(cube_A):
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')


    if sphere_A.is_inside_cyl(cyl_A):
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

    
    if sphere_B.does_intersect_sphere(sphere_A):
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')

    
    if sphere_B.does_intersect_cube(cube_B):
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')
    

    if sphere_A.circumscribe_cube().volume() > cyl_A.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA') 
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')


    if cube_A.is_inside_point(P):
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')


    if cube_A.is_inside_sphere(sphere_A):
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')
    

    if cube_A.is_inside_cube(cube_B):
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')


    if cube_A.is_inside_cylinder(cyl_A):
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')

    
    if cube_B.does_intersect_cube(cube_A):
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')


    if cube_B.intersection_volume(cube_A) > sphere_A.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')


    if cube_A.inscribe_sphere().area()> cyl_A.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
    

    if cyl_A.is_inside_point(P):
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')
    

    if cyl_A.is_inside_sphere(sphere_A):
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')
    

    if cyl_A.is_inside_cube(cube_A):
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')
    

    if cyl_A.is_inside_cylinder(cyl_B):
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')


    if cyl_A.does_intersect_cylinder(cyl_B):
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()