import argparse
import cv2

from triangle_finder import find_triangles


def read_from_static_image():
    parser = argparse.ArgumentParser()
    parser.add_argument('img_path', type=str)
    args = parser.parse_args()

    img = cv2.imread(args.img_path)

    img = find_triangles(img)

    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_from_static_image()
