import cv2


def find_triangles(image):
    edged = cv2.Canny(image, 30, 200)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    triangle_count = 0
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        if len(approx) == 3:
            triangle_count += 1
            cv2.drawContours(image, [contour], -1, (255, 0, 0), 3)

    return image
