# NAME: triangle_finder.py
# PURPOSE: Functions for recognizing and outlining triangles in an image
# AUTHOR: Emma Bethel

import cv2


# PURPOSE: finds and outlines triangles in a given image
# PARAMETERS: image - the image, as a 3D matrix of R/G/B values
# RETURNS: a tuple in which the first element is the same image, now with
#          triangles outlined, and the second element is an integer representing
#          the number of triangles found
def find_triangles(image):
    # finding contours (edges of shapes) in image
    edges = cv2.Canny(image, 30, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # deciding which contours are triangular and drawing them on the image
    triangle_count = 0
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        if len(approx) == 3:
            triangle_count += 1
            cv2.drawContours(image, [contour], -1, (255, 0, 0), 3)

    return image, triangle_count
