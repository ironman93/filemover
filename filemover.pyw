import os, time, goal_dirs
from shutil import move
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
move_dir = "/home/finn/Downloads/sort"


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
