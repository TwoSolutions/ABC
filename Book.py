

class Chapter:
    """Chapter class with Tilte of Chapter,Start,Stop"""
    def __init__(self, Title: str, Start: int,Stop: int):
        self.Title: str = Title
        self.Stop: int = Stop
        self.Start: int = Start

    def setStart(self, Start: int):
        self.Start = Start

    def setStop(self, Stop: int):
        self.Stop = Stop


class Book:
    """Book Class with Title,Author,ListOfChapters and FilePath of AudioFile"""
    def __init__(self, Title: str, Author: str, Chapters: [Chapter],file:str):
        self.File : str = file
        self.Title: str = Title
        self.Author: str = Author
        self.Chapters: [Chapter] = Chapters

    def setChapters(self, Chapters: [Chapter]):
        self.Chapters = Chapters
    def getChapters(self):
        return self.Chapters
