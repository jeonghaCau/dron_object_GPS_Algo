import math 

#=============parameter==================
azimuth = 55.8 #example
drone_x_gps = 36.453840100029424
drone_y_gps = 127.44101670000606
object_yolo_loc_x = 1899
object_yolo_loc_y = 821
#========================================


# import math**
#받아오는 인스턴스 값 : 드론 gps x좌표, 드론 gps y좌표, object x좌표, object y좌표, 방위각
# 리스트 형태로 반환


#------------------------------------------

 
def object_gps_location (drone_x_gps, drone_y_gps, object_yolo_loc_x, object_yolo_loc_y, azimuth):
    fov = 37.15            #32.48 #fix
    height = 50
    lon_x_g2m = 0.00000898
    lat_y_g2m = 0.00001119
    object_location_x = object_yolo_loc_x - 1704 
    object_location_y = 1136 - object_yolo_loc_y 

    #--------one pixel distance method -----------
    diagonal = height * math.tan(math.pi *(fov / 180))
    hori = 3 * diagonal 
    half_horizon = hori / 3.61
    #print(half_horizon)
    one_pixel_distance = half_horizon / 1704
    #print(one_pixel_distance)

    # --------- object distance ---------
    pythagoras = object_location_x**2 + object_location_y**2
    object_pixel_distance = pythagoras**(1/2)
    object_distance = object_pixel_distance * one_pixel_distance
    #print(object_distance)

    #---------object location from the center---------
    # solution : object location angle + azimuth angle


    object_radian = math.atan2(object_location_y, object_location_x)
    object_degree = object_radian * 180 / math.pi
    if object_degree < 0:
        object_degree = object_degree + 360
    #print(object_radian)
    #print(object_degree)
    azimuth_object_degree = object_degree - azimuth
    if azimuth_object_degree > 360:
        azimuth_object_degree = azimuth_object_degree - 360

    #print(azimuth_object_degree)

    
    #--------azimuth object location -----------------------

    azimuth_object_x_location = object_pixel_distance * math.sin(math.pi * (azimuth_object_degree / 180))
    azimuth_object_x_distance = azimuth_object_x_location * one_pixel_distance
    azimuth_object_y_location = object_pixel_distance * math.cos(math.pi * (azimuth_object_degree / 180))
    azimuth_object_y_distance = azimuth_object_y_location * one_pixel_distance
    #print(azimuth_object_x_distance)
    #print(azimuth_object_y_distance)



    #--------object gps location ---------------------------

    gps_object_x_location = (lon_x_g2m * azimuth_object_x_distance) + drone_x_gps
    gps_object_y_location = (lat_y_g2m * azimuth_object_y_distance) + drone_y_gps

    object_gps = [gps_object_x_location, gps_object_y_location]



    #print(object_gps)

    return object_gps



