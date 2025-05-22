import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track:
            i = 1
            if filename != 'thepu':
                new_name = filename
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i += 1
                    new_name = filename + str(i)
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)


                src = folder_to_track + '/' + filename
                new_name = folder_destination + '/' + new_name
                os.rename(src, new_name)

folder_to_track = '/Users/thepu/Desktop'
folder_destination = '/Users/thepu/Desktop'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()