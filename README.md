# Marvellous Data Shield 🛡️
An automated backup and file monitoring system built with Python. 

## Features
* **Automated Backup:** Periodically backs up directories using the `schedule` module.
* **Intelligent Sync:** Uses MD5 checksums (`hashlib`) to only copy new or modified files.
* **Real-Time Logging:** Generates automated text reports of synchronized files.

## Usage
`python Marvellous_Data_Shield.py <Time_Interval> <Source_Folder> <Destination_Folder>`