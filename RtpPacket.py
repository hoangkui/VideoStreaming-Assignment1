import sys
from time import time
HEADER_SIZE = 12


class RtpPacket:
    header = bytearray(HEADER_SIZE)

    def __init__(self):
        pass
        #PART 4 ##################

    def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
        """Encode the RTP packet with header fields and payload."""
        timestamp = int(time())
        header = bytearray(HEADER_SIZE)
        self.header[0] = (version << 6) + (padding << 5) + \
            (extension << 4) + (cc)
        self.header[1] = (marker << 7) + (pt)
        firstByteSeq = seqnum >> 8
        mask = 0xFF
        self.header[2] = firstByteSeq & mask
        self.header[3] = seqnum & mask
        firstByteTime = timestamp >> 24
        secondByteTime = timestamp >> 16
        thirdByteTime = timestamp >> 8
        self.header[4] = firstByteTime & mask
        self.header[5] = secondByteTime & mask
        self.header[6] = thirdByteTime & mask
        self.header[7] = timestamp & mask
        firstByteSSRC = ssrc >> 24
        secondByteSSRC = ssrc >> 16
        thirdByteSSRC = ssrc >> 8
        self.header[8] = firstByteSSRC & mask
        self.header[9] = secondByteSSRC & mask
        self.header[10] = thirdByteSSRC & mask
        self.header[11] = ssrc & mask
        self.payload = payload
        # --------------
        # TO COMPLETE
        # --------------
        # Fill the header bytearray with RTP header fields

        # header[0] = ...
        # ...

        # Get the payload from the argument
        # self.payload = ...

    def decode(self, byteStream):
        """Decode the RTP packet."""
        self.header = bytearray(byteStream[:HEADER_SIZE])
        self.payload = byteStream[HEADER_SIZE:]

    def version(self):
        """Return RTP version."""
        return int(self.header[0] >> 6)

    def seqNum(self):
        """Return sequence (frame) number."""
        seqNum = self.header[2] << 8 | self.header[3]
        return int(seqNum)

    def timestamp(self):
        """Return timestamp."""
        timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
        return int(timestamp)

    def payloadType(self):
        """Return payload type."""
        pt = self.header[1] & 127
        return int(pt)

    def getPayload(self):
        """Return payload."""
        return self.payload

    def getPacket(self):
        """Return RTP packet."""
        return self.header + self.payload
