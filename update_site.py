import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Update hero buttons
new_hero = [
    '        <div class="hero-buttons">\n',
    '          <a href="#inquiry" class="btn-primary">Get a Free Quote</a>\n',
    '          <a href="#inquiry" class="btn-outline" onclick="setProductInterest(\'Download 2026 Catalog\')">📥 Download 2026 Catalog</a>\n',
    '        </div>\n'
]
# Find hero buttons start
hero_start = -1
for i, line in enumerate(lines):
    if '<div class="hero-buttons">' in line:
        hero_start = i
        break

if hero_start != -1:
    # Find next </div>
    hero_end = -1
    for i in range(hero_start + 1, hero_start + 20):
        if '</div>' in lines[i]:
            hero_end = i + 1
            break
    if hero_end != -1:
        lines[hero_start:hero_end] = new_hero

# Update setProductInterest function
start_idx = -1
for i, line in enumerate(lines):
    if 'function setProductInterest(productName) {' in line:
        start_idx = i
        break

if start_idx != -1:
    new_func = [
        'function setProductInterest(productName) {\n',
        '  const productSelect = document.getElementById(\'productSelect\');\n',
        '  const catalogCheckbox = document.getElementById(\'requestCatalog\');\n',
        '  if (productSelect) {\n',
        '    if (productName.includes(\'Catalog\') || productName.includes(\'Guide\')) {\n',
        '      productSelect.value = \'Custom\';\n',
        '      if (catalogCheckbox) catalogCheckbox.checked = true;\n',
        '    } else {\n',
        '      productSelect.value = productName;\n',
        '    }\n',
        '  }\n',
        '}\n'
    ]
    # Find the end of the function (})
    func_end = -1
    for i in range(start_idx + 1, start_idx + 15):
        if '}' in lines[i]:
            func_end = i + 1
            break
    if func_end != -1:
        lines[start_idx:func_end] = new_func

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("SUCCESS")
