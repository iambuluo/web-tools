import os
from bs4 import BeautifulSoup

def check_tools(root_dir="tools"):
    report = []
    
    for tool_name in os.listdir(root_dir):
        tool_path = os.path.join(root_dir, tool_name)
        if not os.path.isdir(tool_path):
            continue
            
        index_path = os.path.join(tool_path, "index.html")
        app_path = os.path.join(tool_path, "app.html")
        
        # Check if index.html exists
        if not os.path.exists(index_path):
            report.append(f"[MISSING] {tool_name}: index.html not found")
            continue
            
        # Check if app.html exists
        if not os.path.exists(app_path):
            report.append(f"[MISSING] {tool_name}: app.html not found")
            continue
            
        # Basic check of app.html content
        try:
            with open(app_path, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Check for script errors (very basic static analysis)
                scripts = soup.find_all('script')
                has_script = False
                for script in scripts:
                    if script.string:
                        has_script = True
                        # Check for common JS errors or empty logic
                        if "addEventListener" not in script.string and "function" not in script.string:
                             pass # might be just variable declaration
                
                if not has_script and not soup.find('script', src=True):
                     report.append(f"[WARN] {tool_name}: No inline script or external script found in app.html")

                # Check for input elements
                if not soup.find('input') and not soup.find('textarea') and not soup.find('select') and not soup.find('button'):
                     # Some tools might be purely informational or use contenteditable, but most have inputs
                     report.append(f"[INFO] {tool_name}: No interactive elements (input/button) found")

        except Exception as e:
            report.append(f"[ERROR] {tool_name}: Failed to parse app.html - {str(e)}")

    return report

if __name__ == "__main__":
    results = check_tools()
    if results:
        print("Found issues:")
        for line in results:
            print(line)
    else:
        print("No obvious structure issues found in tools.")