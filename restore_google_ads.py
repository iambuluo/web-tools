import os, re

# Monetag 代码匹配模式
monetag_pattern = r'<!-- Monetag -->\s*\n\s*<script src="https://quge5.com/88/tag.min.js" data-zone="229646" async data-cfasync="false"></script>'

# Google AdSense 代码
adsense_code = """<!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2259331322940741" crossorigin="anonymous"></script>"""

count = 0
unchanged = 0

for root, dirs, files in os.walk('.'):
    # 跳过备份目录和系统目录
    dirs[:] = [d for d in dirs if d not in ('备份-20260330', '.git', '.workbuddy', 'node_modules')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            new_content = re.sub(monetag_pattern, adsense_code, content, flags=re.DOTALL)
            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f'  [OK] {fpath}')
            else:
                unchanged += 1
        except Exception as e:
            print(f'  [ERR] {fpath}: {e}')

print(f'\n完成！已替换: {count} 个文件，未变动: {unchanged} 个文件')