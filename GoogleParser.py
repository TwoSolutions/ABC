import requests
from bs4 import BeautifulSoup
import re
from Book import Chapter


class GoogleBookParser:
    """Class used for parsing the google demo page and extracting all chapter lengths.Needs the ID of the audiobook."""

    def __init__(self, id):
        self.id = id
        self.url = "https://play.google.com/books/listen?id=%s" % self.id
        self.chapters = self.build_list(self.parse_scripts(self.get_html_from_demo(self.id)))

    def get_html_from_demo(self, id: str) -> str:
        """downloads the html from the demo page"""
        url = "https://play.google.com/books/listen?id=%s" % id
        response = requests.request("GET", url)
        return str(response.text)

    def parse_scripts(self, html: str):
        """This finds the Script where the Chapter Duration Information is hidden and extracts it."""
        parser = BeautifulSoup(html, features="html.parser")
        scripts = parser.find_all("script")  # Finds all Script
        for script in scripts:
            match = re.search("_OC_contentInfo = \\[*.*\\r*\\n*(,\\[.*\\r*\\n*)*",
                              str(script))  # Regex Check to find the correct Script
            if match is not None:
                # print(match)
                start = match.span()[0]
                stop = match.span()[1]
                contentinfo = str(script)[int(start):int(stop)]
                # contentinfo = contentinfo.split(",")
                return contentinfo

    def find_all(self, a_str: str, sub: str) -> [int]:
        """This method takes one string and one substring and returns every index of the substring in the string"""
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return
            yield start
            start += len(sub)  # use start += 1 to find overlapping matches

    def build_list(self, contentinfo: str) -> [[str, int]]:
        """This builds a list out of a list representation in a String.The \"Elements\" of the list can contain any Character since they are parsed by \"[\" and \"]\"
        Works with any List as String of form \"[[a,b],[c,d]]\"

        """
        chapters = []
        contentinfo = contentinfo.replace("\n", "")
        contentinfo = contentinfo.replace("_OC_contentInfo = [[[", "")  # removes everything that isnt a list
        opens = list(self.find_all(contentinfo, "["))
        closes = list(self.find_all(contentinfo, "]"))
        if len(opens) == len(closes):
            for i in range(1, len(opens)):
                chapter = contentinfo[opens[i] + 1:closes[i]]
                opensg = list(self.find_all(contentinfo[opens[i] + 1:closes[i]], "\""))
                chapterlist = []
                for k in range(0, len(opensg), 2):
                    chapterlist.append(chapter[opensg[k] + 1:opensg[k + 1]])
                chapterlist[1] = int(chapterlist[1])
                chapters.append(chapterlist)
            return chapters

    def chapter_from_start_to_end(self, chapters: [[str, int]]) -> [Chapter]:
        """This turnes an abstract Title,start representation of a Chapter into a Chapter with Title,Start,Stop"""
        rlist = []
        for i in range(0, len(chapters)):
            if i == len(chapters) - 1:
                end = -1  # Set -1 for the end of the last chapter. Fixed Later with bitrate or tag duration.
            else:
                end = chapters[i + 1][1]
            rlist.append(Chapter(chapters[i][0], chapters[i][1], end))
        return rlist
