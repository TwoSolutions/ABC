from Book import Book
from GoogleParser import GoogleBookParser
from Splitter import Splitter
id = "AQAAAEAc7BasGM"
title = "QualityLand 2.0 Kikis Geheimnis"
author = "Marc Uwe Kling"
path_to_file = "QualityLand_2_0.m4a"

parser = GoogleBookParser(id)
chapters = parser.chapter_from_start_to_end(parser.chapters)

qlBook = Book(title, author, chapters)
splitter = Splitter(qlBook,path_to_file)
splitter.split()