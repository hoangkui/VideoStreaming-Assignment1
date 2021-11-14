import cv2


def count_frames(filename):
    video = cv2.VideoCapture(filename)
    total = count_frames_manual(video)
    video.release()
    return total


def count_frames_manual(video):
    total = 0
    while True:
        (grabbed, frame) = video.read()
        if not grabbed:
            break
        total += 1
    return total


print(count_frames('movie.Mjpeg'))
