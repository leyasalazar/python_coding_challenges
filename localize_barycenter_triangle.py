#Localize The Barycenter of a Triangle

def bar_triang(point_a=0, point_b=0, point_c=0): 
    x = (point_a[0]+point_b[0]+point_c[0])/3
    
    y = (point_a[1]+point_b[1]+point_c[1])/3
    
    return [round(x, 4), round(y, 4)]