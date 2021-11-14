import cv2


def getInfo(filename):
    video = cv2.VideoCapture(filename)
    total = count_frames_manual(video)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    video.release()
    return total, fps


def count_frames_manual(video):
    total = 0
    while True:
        (grabbed, frame) = video.read()
        if not grabbed:
            break
        total += 1
    return total


class VideoStream:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, 'rb')
        except:
            raise IOError
        self.frameNum = 0
        self.totalFrame, self.fps = getInfo(filename)

    def nextFrame(self):
        """Get next frame."""
        data = self.file.read(5)  # Get the framelength from the first 5 bits
        if data:
            framelength = int(data)

            # Read the current frame
            data = self.file.read(framelength)
            self.frameNum += 1
        return data

    def frameNbr(self):
        """Get frame number."""
        return self.frameNum

    def getTotalFrame(self):
        return self.totalFrame

    def getFps(self):
        return self.fps

    def moveToFrame(self, newFrameNum):
        if newFrameNum > self.frameNum:
            while self.frameNum < newFrameNum:
                data = self.nextFrame()
        elif newFrameNum < self.frameNum:
            # self.file.close()
            self.file = open(self.filename, 'rb')
            self.frameNum = 0
            self.moveToFrame(newFrameNum)
