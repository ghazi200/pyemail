import PyPDF2
import re

def find_matches():
    with open("e.pdf", "rb") as f:
        data = PyPDF2.PdfFileReader(f)
        lines = []
        for i in range(data.numPages):
            lines.append(data.getPage(i).extractText())
        matches = []
        for i in lines:
            # Do smarter things with a better regex pattern
            # and something with the matched objects
            # https://docs.python.org/3.4/library/re.html
            matches.append(re.search(r'[A-Z]', i))
        print(matches)

if __name__ == "__main__":
    find_matches()
