import os, re

# AdSense 旧代码匹配模式（含注释行）
old_patterns = [
    # 带注释版本
    r'<!-- Google AdSense.*?-->\s*\n\s*<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-2259331322940741" crossorigin="anonymous"></script>',
    # 不带注释版本
    r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-2259331322940741" crossorigin="anonymous"></script>',
]

new_code = '<!-- Monetag -->\n    <script src="https://quge5.com/88/tag.min.js" data-zone="229646" async data-cfasync="false"></script>'

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
            new_content = content
            for pattern in old_patterns:
                new_content = re.sub(pattern, new_code, new_content, flags=re.DOTALL)
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
