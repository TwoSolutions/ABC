class Chapter:
    def __init__(self, Title: str, Duration: int, Start: int):
        self.Title: str = Title
        self.Duration: int = Duration
        self.Start: int = Start

    def setStart(self, Start: int):
        self.Start = Start

    def setDuration(self, Duration: int):
        self.Duration = Duration


class Book:
    def __init__(self, Title: str, Author: str, Chapters: [Chapter]):
        self.Title: str = Title
        self.Author: str = Author
        self.Chapters: [Chapter] = Chapters
        self.Duration = 0;
        self.calcDuartion()

    def setChapters(self, Chapters: [Chapter]):
        self.Chapters = Chapters

    def calcDuartion(self):
        self.Duration = 0
        for chapter in self.Chapters:
            self.Duration += chapter.Duration
