from Book import Book, Chapter
from Timer import Timer


soundFileLength = 35168000

title = "QualityLand 2.0 Kikis Geheimnis"
author = "Marc Uwe Kling"
timings = ['0:09', '1:39', '4:16', '6:18', '10:56', '2:12', '9:50', '11:09', '2:15', '9:15', '13:47', '2:36', '8:35', '13:50', '8:37', '9:32', '2:38', '9:55', '2:45', '11:07', '13:14', '2:29', '7:35', '2:11', '7:30', '1:55', '9:33', '7:04', '1:24', '10:53', '6:34', '8:20', '13:19', '1:17', '9:02', '10:39', '1:52', '12:13', '11:08', '1:29', '8:04', '1:56', '7:47', '12:03', '4:11', '8:08', '6:39', '6:25', '7:22', '1:53', '9:25', '4:24', '11:27', '9:27', '8:05', '3:35', '7:30', '4:42', '9:58', '5:44', '4:58', '1:42', '6:57', '11:06', '2:36', '9:26', '9:33', '2:16', '7:20', '7:49', '1:45', '16:55', '6:02', '5:45', '6:58', '8:51', '1:39', '8:25', '10:15', '16:40', '18:40']
timings_millis: [int] = [0] * len(timings)
chapters: [Chapter] = [None] * len(timings)


#covert 'mm:ss' format to milliseconds:
for i in range(0, len(timings)):
    time = timings[i]
    sp = time.split(":")
    seconds: int = int(sp[1])
    seconds += int(sp[0]) * 60
    timings_millis[i] = seconds * 1000
    chapters[i] = Chapter(str(i), timings_millis[i], 0)


qlBook = Book(title, author, chapters) #init new book with metadata

googleTimer = Timer(qlBook, soundFileLength) #init google Timer to calculate track timing offset based on the google chapter lengths compared to the real track length
googleTimer.adjustTimings() #adjusting the previous set chapter lengths by adding the calculated offset

