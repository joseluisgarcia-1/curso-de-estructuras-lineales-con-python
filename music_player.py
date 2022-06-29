"""
Simulador de playlist musical
"""

from node_based_queue import Queue
from time import sleep
from random import randint

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5,6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)
    
    def play(self):
        print(f"Count: {self.count}")

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}")

            sleep(current_track_node.length)
        

track1 = Track("Wellerman")
track2 = Track("Go")
track3 = Track("Light years")
track4 = Track("Heartbreaker")
track5 = Track("Breath me")
track6 = Track("How to dissappear completely")
media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.add_track(track6)
media_player.play()