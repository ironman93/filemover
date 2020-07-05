import os, time
from shutil import move
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
move_dir = "/home/finn/Downloads/sort"

goal_dirs = {
'.zip':    '/home/finn/Downloads/zipped',
#Bilder
'.ai':     '/home/finn/Bilder',
'.bmp':    '/home/finn/Bilder',
'.gif':    '/home/finn/Bilder',
'.jpg':    '/home/finn/Bilder',
'.jpeg':   '/home/finn/Bilder',
'.png':    '/home/finn/Bilder',
'.ps':     '/home/finn/Bilder',
'.psd':    '/home/finn/Bilder',
'.svg':    '/home/finn/Bilder',
'.tif':    '/home/finn/Bilder',
'.tiff':   '/home/finn/Bilder',
'.cr2':    '/home/finn/Bilder',
#Audio
'.aif':    '/home/finn/Musik',
'.cda':    '/home/finn/Musik',
'.mid':    '/home/finn/Musik',
'.midi':   '/home/finn/Musik',
'.mp3':    '/home/finn/Musik',
'.mpa':    '/home/finn/Musik',
'.ogg':    '/home/finn/Musik',
'.wav':    '/home/finn/Musik',
'.wma':    '/home/finn/Musik',
'.wpl':    '/home/finn/Musik',
'.m3u':    '/home/finn/Musik',
#Video
'.3g2':    '/home/finn/Video',
'.3gp':    '/home/finn/Video',
'.avi':    '/home/finn/Video',
'.flv':    '/home/finn/Video',
'.h264':   '/home/finn/Video',
'.m4v':    '/home/finn/Video',
'.mkv':    '/home/finn/Video',
'.mov':    '/home/finn/Video',
'.mp4':    '/home/finn/Video',
'.mpg':    '/home/finn/Video',
'.mpeg':   '/home/finn/Video',
'.rm':     '/home/finn/Video',
'.swf':    '/home/finn/Video',
'.vob':    '/home/finn/Video',
'.wmv':    '/home/finn/Video',
#programmieren
'.py':     '/home/finn/Dokumente/programmieren/',
'.pyw':    '/home/finn/Dokumente/programmieren/',
'.asp':    '/home/finn/Dokumente/internet',
'.aspx':   '/home/finn/Dokumente/internet',
'.cer':    '/home/finn/Dokumente/internet',
'.cfm':    '/home/finn/Dokumente/internet',
'.cgi':    '/home/finn/Dokumente/internet',
'.pl':     '/home/finn/Dokumente/internet',
'.css':    '/home/finn/Dokumente/internet',
'.htm':    '/home/finn/Dokumente/internet',
'.js':     '/home/finn/Dokumente/internet',
'.jsp':    '/home/finn/Dokumente/internet',
'.part':   '/home/finn/Dokumente/internet',
'.php':    '/home/finn/Dokumente/internet',
'.rss':    '/home/finn/Dokumente/internet',
'.xhtml':  '/home/finn/Dokumente/internet',
'.html':   '/home/finn/Dokumente/internet',
#Dokumente
'.txt':    '/home/finn/Dokumente/text_files',
'.doc':    '/home/finn/Dokumente/word',
'.docx':   '/home/finn/Dokumente/word',
'.odt ':   '/home/finn/Dokumente/text_files',
'.pdf':    '/home/finn/Dokumente/pdf',
'.rtf':    '/home/finn/Dokumente/text_files',
'.tex':    '/home/finn/Dokumente/text_files',
'.wks ':   '/home/finn/Dokumente/text_files',
'.wps':    '/home/finn/Dokumente/text_files',
'.wpd':    '/home/finn/Dokumente/text_files',
'.key':    '/home/finn/Dokumente/presentations',
'.odp':    '/home/finn/Dokumente/presentations',
'.pps':    '/home/finn/Dokumente/presentations',
'.ppt':    '/home/finn/Dokumente/presentations',
'.pptx':   '/home/finn/Dokumente/presentations',
'.ods':    '/home/finn/Dokumente/microsoft/excel',
'.xlr':    '/home/finn/Dokumente/microsoft/excel',
'.xls':    '/home/finn/Dokumente/microsoft/excel',
'.xlsx':   '/home/finn/Dokumente/microsoft/excel',
#executables
'.apk':    '/home/finn/Downloads/Executables',
'.bat':    '/home/finn/Downloads/Executables',
'.com':    '/home/finn/Downloads/Executables',
'.exe':    '/home/finn/Downloads/Executables',
'.gadget': '/home/finn/Downloads/Executables',
'.jar':    '/home/finn/Downloads/Executables',
'.wsf':    '/home/finn/Downloads/Executables',
'.AppImage':'/home/finn/Downloads/Executables'
}

os.chdir(move_dir)
def moveall():
    for item in os.listdir(move_dir):
        for extension in goal_dirs:
            if item.endswith(extension):
                file_path = os.path.abspath(item)
                if os.path.isdir(goal_dirs[extension]) == False:
                    os.mkdir(goals_dirs[extensions])
                shutil.move(file_path, goal_dirs[extension])
                os.remove(file_path)


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        print('file was created')
        moveall()
        print('created file moved')

    def on_deleted(event):
        print('file was deleted')

    def on_modified(event):
        print('file was modified')
        moveall()
        print('modified file moved')

    def on_moved(event):
        print('file was moved')
        moveall()

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, move_dir, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
