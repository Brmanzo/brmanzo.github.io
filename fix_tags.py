import os
import re

root_dir = "."

for root, dirs, files in os.walk(root_dir):
    if '.git' in root or '.crossnote' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig_content = content
            
            content = re.sub(r'<header></header>', '<custom-header></custom-header>', content)
            content = re.sub(r'<contact></contact>', '<custom-contact></custom-contact>', content)
            content = re.sub(r'<footer></footer>', '<custom-footer></custom-footer>', content)
            
            if content != orig_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed tags in {filepath}")
