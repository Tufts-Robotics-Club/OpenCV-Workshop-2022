import cv2

from triangle_finder import find_triangles


def read_from_webcam():
    webcam = cv2.VideoCapture(0)

    while True:
        _, frame = webcam.read()

        frame = find_triangles(frame)

        cv2.imshow('shapes', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_from_webcam()
