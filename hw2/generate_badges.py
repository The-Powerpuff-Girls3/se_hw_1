import os

def generate_badge(label, value, color):
    return f"https://img.shields.io/badge/{label}-{value}-{color}"

def main():
    # 读取分析报告
    with open('flake8_report.txt') as f:
        issues = len(f.readlines())
    flake8_badge = generate_badge('flake8', f'{issues} issues', 'red')

    with open('pylint_report.txt') as f:
        score = '8.5'  # 示例：从报告中提取实际分数
    pylint_badge = generate_badge('pylint', f'{score}/10', 'green')

    # 将徽章的 HTML 写入到一个文件
    with open('docs/index.html', 'w') as f:
        f.write(f'''
        <html>
        <body>
          <h1>Static Analysis Results</h1>
          <p><img src="{flake8_badge}" alt="Flake8 Badge"/></p>
          <p><img src="{pylint_badge}" alt="Pylint Badge"/></p>
        </body>
        </html>
        ''')

if __name__ == "__main__":
    main()
