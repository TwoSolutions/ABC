import Book


#This helper class is for adjusting the timings within an audio Track. If you export an audio book fromgoogle play for example, the specified timings on the google site are rounded to seconds. so this tools helps to compensate the offset
class Timer:
    def __init__(self, book: Book, length: int):
        self.book: Book = book
        self.length: int = length
        self.diff: int = self.length - self.book.Duration
        self.dpc: int = 0
        if self.diff < 0:
            self.dpc = -(-(self.diff) // len(self.book.Chapters))
        else:
            self.dpc = self.diff // len(self.book.Chapters)

    def adjustTimings(self):
        print("Diff: %d  Diff per Track: %d", self.diff, self.dpc)
        for chapter in self.book.Chapters:
            chapter.Duration += self.dpc

        self.book.calcDuartion()