import ntpath

from audioclipextractor.core import AudioClipExtractor
from tinytag import TinyTag
import os
import Book
from Book import Chapter
import subprocess


class Splitter:
    """This is the Splitter Class.It takes a parameter of Type Book.It handles all Splitting related interactions."""

    def __init__(self, book: Book):
        self.book = book
        self.file: str = self.book.File

    def split(self):
        """Performs the acutal Splitting of the audiofile."""
        filename = ntpath.basename(self.file)
        filename = filename.split(".")[0::-2][0]
        print(filename.split(".")[0::-2][0])
        f = open(filename + ".txt", "w")
        self.fix_chapters()

        for chapter in self.book.getChapters():
            f.write(str(chapter.Start / 1000) + "  " + str(chapter.Stop / 1000) + "  " + chapter.Title + "\n")
        f.close()
        a = AudioClipExtractor(self.file)
        outdir = os.sep.join(self.file.split(os.sep)[:-1]) + os.sep + "out" + os.sep
        os.system("mkdir \"%s\"" % outdir)
        a.extract_clips(filename + ".txt", outdir)

    # This method is used to fix the duration of the last chapter
    def fix_chapters(self):
        """Fixes the duration of the last chapter.Sets the start for the first \"invisible\" chapter to 0 and titles
        it with the name of the book
        """
        tag = TinyTag.get(self.file)  # getting the tags of the original file
        # print(tag.duration)
        if self.book.getChapters()[-1].Stop == -1:  #If the duration hasnt been set (it hasnt if it was parsed with google)
            if tag.duration * 1000 > self.book.getChapters()[-1].Start:  # if the complete duration of the tag is greater
                                                                         # then the start of the chapter it is prbly correct.
                                                                         # (Google tags correct if you download there)
                self.book.getChapters()[-1].setStop(int(tag.duration * 1000))  # Set the End for the last chapter
            else:  # get duration from bitrate
                pathwithoutfile = os.sep.join(self.file.split(os.sep)[:-1]) + os.sep  # get the path to the file
                filename = self.file.split(os.sep)[-1]  # get the file name
                stdout = subprocess.check_output(
                    # run ffprobe ( comes with ffmpeg) to get the duration from the bitrate
                    "cd %s && ffprobe -i %s -show_entries format=duration -v quiet -of csv=\"p=0\"" % (
                        "\"" + pathwithoutfile + "\"", "\"" + filename + "\""), shell=True)
                self.book.getChapters()[-1].setStop(
                    int(float(stdout.decode("utf-8").replace("\n", "")) * 1000))  # convert the duration
                # from bytestring to integer and set the stop for the last chapter

        if self.book.getChapters()[0].Start != 0:
            temp = Chapter(self.book.Title, 0, self.book.getChapters()[0].Start)
            k = self.book.getChapters()
            k.insert(0, temp)
            self.book.setChapters(k)
