#!/usr/bin/env python3

import os
import cv2

ADDRESS = os.environ.get("FEED_ADDRESS","localhost")
PORT = os.environ.get("FEED_PORT", 9000)

FREQUENCY = 2

def read_from_feed():
    stream = cv2.VideoCapture(f'tcp://{ADDRESS}:{PORT}')

    while True:
        _, frame = stream.read()

        # your image processing code here

        cv2.imshow('Video Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_from_feed()
