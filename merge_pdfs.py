from PyPDF2 import PdfFileMerger

def by_appending():
    merger = PdfFileMerger()
    # Either provide file stream
    f1 = open("pdf-sample.pdf", "rb")
    merger.append(f1)
    # Or direct file path
    merger.append("test.pdf")
    merger.write("mergedPdf.pdf")

def by_inserting():
    merger = PdfFileMerger()
    merger.append("test.pdf")
    merger.merge(0, "pdf-sample.pdf")
    merger.write("mergedPdf1.pdf")

if __name__ == "__main__":
    by_appending()
    by_inserting()
