import os

tools_dir = "tools"
target_str = "justhtmls"
replacement_str = "aichatx.com.cn"

def replace_in_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if target_str in content:
            # Case insensitive replacement might be risky for URLs, so sticking to lowercase 'justhtmls'
            # But let's handle "JustHTMLs" as "AiChatX Tools" for display text
            
            new_content = content.replace("JustHTMLs", "AiChatX Tools")
            new_content = new_content.replace(target_str, replacement_str)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Process index.html in root
replace_in_file("index.html")

# Process tools directory
for root, dirs, files in os.walk(tools_dir):
    for file in files:
        if file.endswith(".html") or file.endswith(".json") or file.endswith(".js"):
            replace_in_file(os.path.join(root, file))

print("Batch replacement completed.")