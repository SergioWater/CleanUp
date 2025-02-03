import os

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

for item_name in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item_name)
    
    if os.path.isfile(item_path):
        print(f"File: {item_name}")
    elif os.path.isdir(item_path):
        print(f"Directory: {item_name}")