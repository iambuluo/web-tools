import os

def replace_in_file(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    replacements = {
        "justhtmls": "aichatx.com.cn",
        "JustHTMLs": "AiChatX Tools",
        "JustHtmls": "AiChatX Tools",
        "htmls.dev": "aichatx.com.cn",
        "www.htmls.dev": "www.aichatx.com.cn"
    }
    
    # Specific files to update
    files_to_update = [
        "index.html",
        "sitemap.xml",
        "readme.md",
        "index.json",
        "CONTRIBUTING.md",
        "reference.html",
        "tools-rank.html",
        "privacy.html",
        "terms.html",
        "contact.html",
        "USAGE.md"
    ]
    
    for file in files_to_update:
        if os.path.exists(file):
            replace_in_file(file, replacements)
            
    # Update all tool index.html and app.html files
    for root, dirs, files in os.walk("tools"):
        for file in files:
            if file.endswith(".html") or file.endswith(".json") or file.endswith(".js"):
                replace_in_file(os.path.join(root, file), replacements)

if __name__ == "__main__":
    main()
