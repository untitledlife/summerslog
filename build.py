#!/usr/bin/env python3
"""Assembles summerslog pages from _templates/base.html + _content/ files."""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(ROOT, '_templates', 'base.html')).read()

# (slug, label, path-from-root)
NAV_ITEMS = [
    ('home',          'Home',          ''),
    ('presentations', 'Presentations', 'presentations/'),
    ('gallery',       'Gallery',       'gallery/'),
    ('interactive',   'Interactive',   'interactive/'),
    ('posts',         'Posts',         'posts/'),
    ('journal',       'Journal',       'journal/'),
]

def parse_content(filepath):
    """Parse a content file: extract frontmatter, extra_head, extra_scripts, and body."""
    raw = open(filepath).read()
    _, fm, body = raw.split('---', 2)
    meta = {}
    for line in fm.strip().splitlines():
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip()
    # Extract <!-- extra_head -->...<!-- /extra_head -->
    extra_head = ''
    m = re.search(r'<!-- extra_head -->\n(.*?)<!-- /extra_head -->\n?', body, re.DOTALL)
    if m:
        extra_head = m.group(1).rstrip('\n')
        body = body[:m.start()] + body[m.end():]
    # Extract <!-- extra_scripts -->...<!-- /extra_scripts -->
    extra_scripts = ''
    m = re.search(r'<!-- extra_scripts -->\n(.*?)<!-- /extra_scripts -->\n?', body, re.DOTALL)
    if m:
        extra_scripts = m.group(1).rstrip('\n')
        body = body[:m.start()] + body[m.end():]
    return meta, body.strip('\n'), extra_head, extra_scripts

def build_nav(active, rel_path):
    """Build nav HTML. active is the slug. rel_path is e.g. 'index.html' or 'posts/index.html'."""
    depth = rel_path.count('/')
    prefix = '../' * depth if depth > 0 else ''
    lines = []
    for slug, label, path in NAV_ITEMS:
        if slug == active:
            href = './'
            cls = ' class="active"'
        else:
            href = prefix + path
            cls = ''
        lines.append(f'            <a href="{href}"{cls}>{label}</a>')
    return '\n'.join(lines)

def build_page(meta, body, extra_head, extra_scripts, rel_path):
    """Fill the template with content."""
    depth = rel_path.count('/')
    root = '../' * depth if depth > 0 else ''
    html = TEMPLATE
    html = html.replace('{{title}}', meta.get('title', "Summer's Log"))
    html = html.replace('{{root}}', root)
    html = html.replace('{{nav}}', build_nav(meta.get('nav_active', ''), rel_path))
    html = html.replace('{{content}}', body)
    # Only inject extra_head/extra_scripts if non-empty
    if extra_head:
        html = html.replace('{{extra_head}}', extra_head + '\n')
    else:
        html = html.replace('{{extra_head}}', '')
    if extra_scripts:
        html = html.replace('{{extra_scripts}}', extra_scripts + '\n')
    else:
        html = html.replace('{{extra_scripts}}', '')
    return html

def main():
    content_dir = os.path.join(ROOT, '_content')
    for dirpath, _, filenames in os.walk(content_dir):
        for fn in filenames:
            if not fn.endswith('.html'):
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, content_dir)
            dest = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            meta, body, extra_head, extra_scripts = parse_content(src)
            html = build_page(meta, body, extra_head, extra_scripts, rel)
            open(dest, 'w').write(html)
            print(f'  built {rel}')
    print('done.')

if __name__ == '__main__':
    main()
