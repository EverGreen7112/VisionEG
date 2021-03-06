import math
import cv2 as cv
from VisionEG.draw_on_frame import get_rectangle_value


def find_distance_from_objecet(focal_length: float, area: int, known_area: float) -> float:
    """
    Calculates the distance between the center of the object and the camera
    :param focal_lenght: Focal lenght of the camera - need calibration
    :param area: The area of the object (pixels^2)
    :param known_area: The known area of the object (m^2)
    """
    if area == 0:
        return -1
    return focal_length * math.sqrt(known_area / area)

def find_distance_new_function(object_height: float, camera_height: float, camera_vertical_angle: float, vertical_angle_from_object: float) -> float:
    """
    Calculates the norm verctor (closest distanc) from the object
    :param object_height: The height of the object in meters
    :praram camera_height: The height of the camera in meters
    :param camera_vertical_angle: The vertical angle of the camera
    :param vertical_angle_from_object: The angle between the camera and the object
    """
    return (object_height - camera_height) / (math.tan(math.radians(vertical_angle_from_object + camera_vertical_angle)))

def find_angle(distance_from_center: float, camera_fov: float, image_total_pixels: int) -> float:
    """
    Calculates the angle between the camera and the center of the object
    :param distance_from_center: The distance between the center of the object to the center of the picture (in pixels)
    :param camera_fov: The camera's fov
    :param image_total_pixels: image total pixels
    """
    return (distance_from_center * camera_fov) / image_total_pixels

def find_vertical_angle(distance_from_center: float, camera_horizontal_fov: float, image_total_horizontal_pixels: int) -> float:
    """
    Calculates the vertical angle between the camera and the center of the object
    :param distance_from_center: The distance between the center of the object to the center of the picture (in pixels)
    :param camera_horizontal_fov: The camera's fov
    :param image_total_horizontal_pixels: image total pixels
    """
    return (distance_from_center * camera_horizontal_fov) / image_total_horizontal_pixels

def middle_of_rect(point1: tuple, point2: tuple) -> tuple:
    """
    Returns a tuple that represents the midle of the rect coordinate (x,y)
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    """
    mid_x = int((point1[0] + point2[0])/2)
    mid_y = int((point1[1] + point2[1])/2)
    return (mid_x, mid_y)


def distance_from_center(center_of_object: tuple, center_of_image: tuple) -> int:
    """
    Returns the distance from the center_of_image (x,y) to the center of the object (x,y)
    :param center_of_object: Center of the object tuple (x,y)
    :param center_of_image: Center of the image tuple (x,y)
    """
    obj_mid_x = center_of_object[0]
    img_mid_x = center_of_image[0]
    return img_mid_x - obj_mid_x

def vertical_distance_from_center(center_of_object: tuple, center_of_image: tuple) -> int:
    obj_mid_y = center_of_object[1]
    img_mid_y = center_of_image[1]
    return img_mid_y - obj_mid_y

def distance_from_center__rect(point1: tuple, point2: tuple, center_of_image: tuple) -> int:
    """
    Returns the distance between the center of the rect to the center of the image
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    :param center_of_image: Center of the image tuple (x,y)
    """
    rect_mid = middle_of_rect(point1, point2)
    return distance_from_center(rect_mid, center_of_image)

def vertical_distance_from_center__rect(point1: tuple, point2: tuple, center_of_image: tuple):
    rect_mid = middle_of_rect(point1, point2)
    return vertical_distance_from_center(center_of_object, center_of_image)

def get_circle_area(radius) -> float:
    """
    Returns the area of the circle (radius^2 * pi)
    :param radius: The radius of the circle
    """
    return radius*radius*math.pi


def get_rect_area(point1, point2) -> float:
    """
    Retues the area of the circle
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    """
    width = abs(point1[0] - point2[0])
    height = abs(point1[1] - point2[1])
    return width * height


def get_shape_center(contour) -> tuple:
    """
    Retuns the center of the contour by building a counding rect and calculating his center
    :param contour: The contour
    """
    point1, point2 = get_rectangle_value(contour)
    return middle_of_rect(point1, point2)


def get_shape_area(contour) -> float:
    """
    Simple function that returns the area of the contour
    :param contour: The contour
    """
    return cv.contourArea(contour)