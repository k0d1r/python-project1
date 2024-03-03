import aspose.words as aw

fileNames = [ "Input1.pdf", "Input2.pdf" ]

output = aw.Document()
# Eklemeden önce hedef belgedeki tüm içeriği kaldırın.
output.remove_all_children()

for fileName in fileNames:
    input = aw.Document(fileName)
    # Kaynak belgeyi hedef belgenin sonuna ekleyin.
    output.append_document(input, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

output.save("Output.pdf");
    