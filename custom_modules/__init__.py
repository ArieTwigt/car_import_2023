import os

folder_name = "export"

if not os.path.exists(folder_name):
    print("📂 Export folder not present yet. Creating...")
    os.mkdir(folder_name)
    