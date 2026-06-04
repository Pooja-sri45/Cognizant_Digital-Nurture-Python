import shutil
copied_files = set()
def backup_file(source, destination):

    try:
        if source in copied_files:
            print("Duplicate file skipped")
            return

        shutil.copy(source, destination)
        copied_files.add(source)

        log = open("backup.log", "a")
        log.write(f"Copied: {source}\n")
        log.close()
        print("File copied successfully")
        
    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission denied")

backup_file("sample.txt", "backup_sample.txt")