from Book import Book
from GoogleParser import GoogleBookParser

id = "AQAAAEAc7BasGM"

parser = GoogleBookParser(id)
chapters = parser.chapter_from_start_to_end(parser.chapters)

title = "QualityLand 2.0 Kikis Geheimnis"
author = "Marc Uwe Kling"

qlBook = Book(title, author, chapters)
