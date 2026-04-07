#!/usr/bin/env python3
"""
Static site generator for Summer's Log.

Usage:
    python build.py

Reads markdown posts from content/posts/, applies templates from templates/,
and generates:
    - posts/*.html         (individual post pages)
    - posts/index.html     (searchable listing of all posts)
    - index.html           (homepage with recent posts)

Posts are .md files with YAML frontmatter:
    ---
    title: "Post Title"
    date: 2026-04-07
    tags: [research, math]
    type: research          # research, fiction, paper -- shown in meta line
    slug: custom-slug       # optional, overrides filename-based slug
    katex: true             # optional, default true
    ---
    Post content in markdown...

Existing HTML files in posts/ that don't have a corresponding .md source
are left untouched. The build only overwrites files it generates.

Requirements: pip install markdown
"""

import os
import re
import datetime
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Template loading
# ---------------------------------------------------------------------------

def load_template(name):
    path = os.path.join(ROOT, 'templates', name)
    with open(path, 'r') as f:
        return f.read()

# ---------------------------------------------------------------------------
# Frontmatter parsing (no PyYAML dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Split a markdown file into (metadata_dict, body_string).

    Supports simple YAML frontmatter between --- markers.
    Values can be: strings (optionally quoted), dates, booleans,
    and bracket-delimited lists like [a, b, c].
    """
    if not text.startswith('---'):
        return {}, text
    end = text.find('---', 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 3:].strip()

    meta = {}
    for line in fm_block.splitlines():
        line = line.strip()
        if not line or ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()
        # Strip quotes
        if (val.startswith('"') and val.endswith('"')) or \
           (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        # Parse lists [a, b, c]
        elif val.startswith('[') and val.endswith(']'):
            val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',') if v.strip()]
        # Parse booleans
        elif val.lower() in ('true', 'yes'):
            val = True
        elif val.lower() in ('false', 'no'):
            val = False
        meta[key] = val
    return meta, body

# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_markdown(text):
    """Convert markdown to HTML, preserving raw HTML passthrough and math.

    Before rendering, we protect $...$ and $$...$$ math blocks from
    markdown processing, then restore them after.
    """
    # Protect display math $$...$$
    display_blocks = []
    def save_display(m):
        display_blocks.append(m.group(0))
        return f'\x00DISPLAYMATH{len(display_blocks) - 1}\x00'
    text = re.sub(r'\$\$(.+?)\$\$', save_display, text, flags=re.DOTALL)

    # Protect inline math $...$  (but not $$)
    inline_blocks = []
    def save_inline(m):
        inline_blocks.append(m.group(0))
        return f'\x00INLINEMATH{len(inline_blocks) - 1}\x00'
    text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', save_inline, text)

    # Render markdown
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Restore math
    for i, block in enumerate(display_blocks):
        html = html.replace(f'\x00DISPLAYMATH{i}\x00', block)
    for i, block in enumerate(inline_blocks):
        html = html.replace(f'\x00INLINEMATH{i}\x00', block)

    return html

# ---------------------------------------------------------------------------
# Date formatting
# ---------------------------------------------------------------------------

def parse_date(date_val):
    """Parse a date from frontmatter. Accepts str or datetime.date."""
    if isinstance(date_val, datetime.date):
        return date_val
    if isinstance(date_val, str):
        return datetime.date.fromisoformat(date_val)
    raise ValueError(f"Cannot parse date: {date_val!r}")


def format_date_long(d):
    """e.g. 'March 20, 2026'"""
    return d.strftime('%B %-d, %Y')


def format_date_short(d):
    """e.g. 'Mar 20, 2026'"""
    return d.strftime('%b %-d, %Y')

# ---------------------------------------------------------------------------
# Post loading
# ---------------------------------------------------------------------------

def load_posts(content_dir):
    """Load all .md files from content/posts/, return list of post dicts."""
    posts_dir = os.path.join(content_dir, 'posts')
    if not os.path.isdir(posts_dir):
        return []
    posts = []
    for fn in os.listdir(posts_dir):
        if not fn.endswith('.md'):
            continue
        filepath = os.path.join(posts_dir, fn)
        with open(filepath, 'r') as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)

        # Determine slug (output filename without .html)
        slug = meta.get('slug', fn[:-3])  # strip .md

        post = {
            'title': meta.get('title', slug),
            'date': parse_date(meta['date']),
            'tags': meta.get('tags', []),
            'type': meta.get('type', ''),
            'katex': meta.get('katex', True),
            'slug': slug,
            'filename': slug + '.html',
            'body_md': body,
            'body_html': render_markdown(body),
            'meta': meta,
        }
        posts.append(post)

    # Sort by date descending, then by title
    posts.sort(key=lambda p: (-p['date'].toordinal(), p['title']))
    return posts

# ---------------------------------------------------------------------------
# KaTeX snippets
# ---------------------------------------------------------------------------

KATEX_CSS = '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.css">'

KATEX_JS = (
    '    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.js"></script>\n'
    '    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/contrib/auto-render.min.js"'
    ' onload="renderMathInElement(document.body,{delimiters:[{left:\'$$\',right:\'$$\',display:true},'
    '{left:\'$\',right:\'$\',display:false},'
    '{left:\'\\\\(\',right:\'\\\\)\',display:false},'
    '{left:\'\\\\[\',right:\'\\\\]\',display:true}],throwOnError:false});"></script>'
)

# ---------------------------------------------------------------------------
# Build individual post pages
# ---------------------------------------------------------------------------

def build_meta_line(post):
    """Build the post-meta line, e.g. 'March 20, 2026 . Summer . Fiction'"""
    parts = [format_date_long(post['date']), 'Summer']
    ptype = post['type'].strip().lower()
    if ptype in ('fiction', 'paper'):
        parts.append(ptype.capitalize())
    return ' &middot; '.join(parts)


def build_post_html(post, template):
    """Render a single post page."""
    html = template
    html = html.replace('{{title}}', post['title'])
    html = html.replace('{{meta_line}}', build_meta_line(post))
    html = html.replace('{{content}}', post['body_html'])

    if post['katex']:
        html = html.replace('{{katex_css}}', KATEX_CSS)
        html = html.replace('{{katex_js}}', KATEX_JS)
    else:
        html = html.replace('{{katex_css}}', '')
        html = html.replace('{{katex_js}}', '')

    return html

# ---------------------------------------------------------------------------
# Build post listing (posts/index.html)
# ---------------------------------------------------------------------------

def build_post_list_item(post):
    """One <li> for the post listing page."""
    ptype = post['type'].strip().lower()
    type_label = ''
    if ptype in ('fiction', 'paper', 'research'):
        type_label = f' &middot; {ptype.capitalize()}'
    date_str = format_date_short(post['date'])
    return (
        f'<li><a href="{post["filename"]}">{post["title"]}</a>'
        f' <span class="meta">{date_str}{type_label}</span></li>'
    )


def build_post_index(posts, template):
    """Build posts/index.html."""
    items = '\n'.join(build_post_list_item(p) for p in posts)
    html = template.replace('{{post_list}}', items)
    return html

# ---------------------------------------------------------------------------
# Build homepage (index.html)
# ---------------------------------------------------------------------------

def build_homepage_post_item(post):
    """One <li> for the homepage recent posts section."""
    ptype = post['type'].strip().lower()
    type_label = ''
    if ptype in ('fiction', 'paper', 'research'):
        type_label = f' &middot; {ptype.capitalize()}'
    date_str = format_date_short(post['date'])
    return (
        f'                <li><a href="posts/{post["filename"]}">{post["title"]}</a>'
        f' <span class="meta">{date_str}{type_label}</span></li>'
    )


def build_homepage(posts, template, total_count):
    """Build index.html with recent 15 posts."""
    recent = posts[:15]
    items = '\n'.join(build_homepage_post_item(p) for p in recent)
    html = template.replace('{{recent_posts}}', items)
    html = html.replace('{{post_count}}', str(total_count))
    return html

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    content_dir = os.path.join(ROOT, 'content')
    posts_out = os.path.join(ROOT, 'posts')
    os.makedirs(posts_out, exist_ok=True)

    # Load templates
    post_template = load_template('post.html')
    post_index_template = load_template('post-index.html')
    index_template = load_template('index.html')

    # Load markdown posts
    posts = load_posts(content_dir)
    if not posts:
        print('No posts found in content/posts/. Nothing to build.')
        return

    print(f'Found {len(posts)} markdown post(s).')

    # Count total posts: markdown-sourced + existing HTML without a .md source
    md_filenames = {p['filename'] for p in posts}
    existing_html = set()
    for fn in os.listdir(posts_out):
        if fn.endswith('.html') and fn != 'index.html':
            existing_html.add(fn)
    # Posts that only exist as hand-written HTML
    legacy_count = len(existing_html - md_filenames)
    total_count = len(posts) + legacy_count

    # Build individual post pages
    for post in posts:
        out_path = os.path.join(posts_out, post['filename'])
        html = build_post_html(post, post_template)
        with open(out_path, 'w') as f:
            f.write(html)
        print(f'  built posts/{post["filename"]}')

    # For the listing pages, we also need to include legacy HTML posts.
    # Parse titles/dates from existing HTML files that have no .md source.
    all_posts_for_listing = list(posts)  # start with md-sourced posts

    for fn in sorted(existing_html - md_filenames):
        filepath = os.path.join(posts_out, fn)
        info = parse_legacy_post(filepath, fn)
        if info:
            all_posts_for_listing.append(info)

    # Sort everything by date descending, then title
    all_posts_for_listing.sort(key=lambda p: (-p['date'].toordinal(), p['title']))

    # Build posts/index.html
    post_index_html = build_post_index(all_posts_for_listing, post_index_template)
    with open(os.path.join(posts_out, 'index.html'), 'w') as f:
        f.write(post_index_html)
    print(f'  built posts/index.html ({total_count} posts listed)')

    # Build homepage
    homepage_html = build_homepage(all_posts_for_listing, index_template, total_count)
    with open(os.path.join(ROOT, 'index.html'), 'w') as f:
        f.write(homepage_html)
    print(f'  built index.html (latest 15 of {total_count} posts)')

    print(f'Done. {len(posts)} posts generated from markdown, {legacy_count} legacy HTML posts included in listings.')


def parse_legacy_post(filepath, filename):
    """Extract title, date, and type from a hand-written HTML post file.

    Returns a dict compatible with the post listing functions, or None on failure.
    """
    try:
        with open(filepath, 'r') as f:
            html = f.read(8000)  # first 8KB covers even posts with large inline styles
    except Exception:
        return None

    # Extract title from <title>...</title> or <h1>...</h1>
    title = None
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    if not title:
        m = re.search(r'<title>(.*?)(?:\s*[—|]\s*Summer)', html)
        if m:
            title = m.group(1).strip()
    if not title:
        title = filename.replace('.html', '').replace('-', ' ').title()

    # Extract date from post-meta div
    date = None
    m = re.search(r'class="post-meta"[^>]*>(.*?)</div>', html, re.DOTALL)
    if m:
        meta_text = re.sub(r'<[^>]+>', '', m.group(1))
        # Try to find a date like "March 20, 2026" or "Mar 20, 2026"
        dm = re.search(r'(\w+ \d{1,2}, \d{4})', meta_text)
        if dm:
            for fmt in ('%B %d, %Y', '%b %d, %Y'):
                try:
                    date = datetime.datetime.strptime(dm.group(1), fmt).date()
                    break
                except ValueError:
                    pass

    # Try date from filename: 2026-03-20-...
    if date is None:
        dm = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
        if dm:
            date = datetime.date.fromisoformat(dm.group(1))

    if date is None:
        date = datetime.date(2026, 3, 20)  # fallback

    # Detect type from meta line -- look for standalone type labels
    # (separated by middot/bullet or at end), not words embedded in phrases
    post_type = ''
    if m:
        meta_text = re.sub(r'<[^>]+>', '', m.group(1))
        # Split on common separators and check last segment(s)
        parts = re.split(r'[·\u00b7\u2022&;]+', meta_text)
        for part in parts:
            word = part.strip().lower()
            if word == 'fiction':
                post_type = 'fiction'
            elif word == 'paper':
                post_type = 'paper'
            elif word == 'research':
                post_type = 'research'

    return {
        'title': title,
        'date': date,
        'type': post_type,
        'filename': filename,
        'tags': [],
        'katex': True,
        'slug': filename[:-5],
    }


if __name__ == '__main__':
    main()
