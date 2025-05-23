import FreeSimpleGUI as sg
from zipExtractor import extract_archive

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File Compressor", layout = [[label1, input1, choose_button1], 
                                                [label2, input2, choose_button2], 
                                                [extract_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed Successfully")
window.close()