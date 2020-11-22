

class Chapter:
    def __init__(self, Title: str, Start: int,Stop: int):
        self.Title: str = Title
        self.Stop: int = Stop
        self.Start: int = Start

    def setStart(self, Start: int):
        self.Start = Start

    def setStop(self, Stop: int):
        self.Stop = Stop


class Book:
    def __init__(self, Title: str, Author: str, Chapters: [Chapter]):
        self.Title: str = Title
        self.Author: str = Author
        self.Chapters: [Chapter] = Chapters

    def setChapters(self, Chapters: [Chapter]):
        self.Chapters = Chapters
    def getChapters(self):
        return self.Chapters
