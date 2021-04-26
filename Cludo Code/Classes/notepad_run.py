from notepad import Notepad

notepad_run = Notepad()

while notepad_run.running:
    notepad_run.display_text()
    notepad_run.notepad_loop()
