import ntpath

from audioclipextractor.core import AudioClipExtractor
from tinytag import TinyTag

import Book
from Book import Chapter


class Splitter:
    def __init__(self, book: Book, file: str):
        self.file = file
        self.book = book

    def split(self):
        filename = ntpath.basename(self.file)
        filename = filename.split(".")[0::-2][0]
        print(filename.split(".")[0::-2][0])
        f = open(filename + ".txt", "w")
        self.fix_chapters()

        for chapter in self.book.getChapters():
            f.write(str(chapter.Start / 1000) + "  " + str(chapter.Stop / 1000) + "  " + chapter.Title + "\n")
        f.close()
        a = AudioClipExtractor(self.file)

        a.extract_clips(filename + ".txt", "/out")

    def fix_chapters(self):
        tag = TinyTag.get(self.file)
        print(tag.duration)
        if self.book.getChapters()[-1].Stop == -1:
            self.book.getChapters()[-1].setStop(int(tag.duration * 1000))
        if self.book.getChapters()[0].Start != 0:
            temp = Chapter(self.book.Title, 0, self.book.getChapters()[0].Start)
            k = self.book.getChapters()
            k.insert(0, temp)
            self.book.setChapters(k)
