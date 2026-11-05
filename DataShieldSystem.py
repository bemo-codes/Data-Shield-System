#############################################################################
#
#   Importing required libraries
#
#############################################################################
import os
import sys
import time
import schedule
import hashlib
import shutil

#############################################################################
#
#   Function name:      hashfile
#   Input:              path (string), blocksize (int)
#   Description:        Calculates and returns the MD5 checksum of a file.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def hashfile(path, blocksize=1024):
    try:
        afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {path}: {e}")
        return None

#############################################################################
#
#   Function name:      DirectoryBackup
#   Input:              SourceDir (string), DestDir (string)
#   Description:        Automates file backup and synchronization between 
#                       source and destination directories.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def DirectoryBackup(SourceDir, DestDir):
    Border = "-" * 50

    # Validate source directory
    if not os.path.exists(SourceDir) or not os.path.isdir(SourceDir):
        print(f"Unable to proceed. Source directory '{SourceDir}' does not exist or is not a directory.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(DestDir):
        os.mkdir(DestDir)
        print(f"Destination directory '{DestDir}' created successfully.")

    # Setting up log file for real-time reporting
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogFileName = os.path.join(DestDir, "BackupLog_%s.txt" % timestamp)

    fobj = open(LogFileName, "w")
    print(f"Backup process started. Log file created: {LogFileName}")

    fobj.write(Border + "\n")
    fobj.write("---- Data Shield: Backup & Sync Report ----\n")
    fobj.write("Backup executed at: " + timestamp + "\n")
    fobj.write(Border + "\n")

    copied_count = 0

    # Traverse the source directory
    for foldername, subfolders, filenames in os.walk(SourceDir):
        for filename in filenames:
            src_path = os.path.join(foldername, filename)
            
            # Create corresponding relative path for destination
            rel_path = os.path.relpath(src_path, SourceDir)
            dest_path = os.path.join(DestDir, rel_path)

            # Ensure destination subdirectories exist
            dest_dir_struct = os.path.dirname(dest_path)
            if not os.path.exists(dest_dir_struct):
                os.makedirs(dest_dir_struct)

            needs_copy = False

            # Detect new files
            if not os.path.exists(dest_path):
                needs_copy = True
                fobj.write(f"New File Detected & Copied: {rel_path}\n")
            
            # Detect modified files using MD5 Checksum
            else:
                src_hash = hashfile(src_path)
                dest_hash = hashfile(dest_path)
                
                if src_hash != dest_hash:
                    needs_copy = True
                    fobj.write(f"Modified File Detected & Updated: {rel_path}\n")

            # Execute the synchronization
            if needs_copy:
                try:
                    shutil.copy2(src_path, dest_path)
                    copied_count += 1
                except Exception as e:
                    fobj.write(f"Error copying {rel_path}: {e}\n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files synchronized/backed up: {copied_count}\n")
    fobj.write(Border + "\n")
    fobj.write("------------------ End of log file ---------------------\n")
    fobj.write(Border + "\n")

    fobj.close()
    print("Backup cycle completed.")
    print(Border)

#############################################################################
#
#   Function name:      main
#   Input:              None
#   Description:        Entry point of the script, handles command line 
#                       arguments and scheduling loop.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def main():
    Border = "-" * 50
    print(Border)
    print("---- Data Shield System ----")
    print(Border)

    # Handling --h and --u flags
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This automation script is used to perform:")
            print("1: Automated file backup and synchronization.")
            print("2: File monitoring using MD5 checksum to detect changes.")
            print("3: Real-time reporting via log files generated in the destination.")
            print("4: Periodic background execution based on a schedule.")
        
        elif sys.argv[1].lower() == "--u":
            print("Use the automation script as: ")
            print(f"python {sys.argv[0]} Time_Interval Source_Folder Destination_Folder")
            print("Time_Interval      : Time in minutes for periodic backup execution.")
            print("Source_Folder      : Directory containing your important data.")
            print("Destination_Folder : Directory where the backup/archives will be stored.")
        
        else:
            print("Unable to proceed as there is no matching argument.")
            print("Please use --h or --u flag for getting more details.")

    # Actual project code execution
    elif len(sys.argv) == 4:
        try:
            interval = int(sys.argv[1])
            source_dir = sys.argv[2]
            dest_dir = sys.argv[3]

            print(f"Scheduler started successfully.")
            print(f"Monitoring '{source_dir}' every {interval} minute(s).")
            print("Press Ctrl + C to abort the automation script.")
            print(Border)
            
            # Schedule the task
            schedule.every(interval).minutes.do(
                DirectoryBackup,
                source_dir,
                dest_dir
            )

            # Infinite loop to keep the script running
            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Error: Time_Interval must be an integer.")

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching.")
        print("Please use --h or --u flag for getting more details.")

    print(Border)
    print("--- Thank you for using Data Shield ---")
    print(Border)

#############################################################################
#
#   Starter of main
#
#############################################################################

if __name__ == "__main__":
    main()