from scholarly import scholarly

# Fetch profile
author = scholarly.search_author_id("BDil2hgAAAAJ")
filled = scholarly.fill(author)

# Format publication HTML
pub_html = "<ul>\n"
for pub in filled['publications'][:5]:
    title = pub['bib'].get('title', 'No Title')
    year = pub['bib'].get('pub_year', 'Year N/A')
    pub_html += f"<li>{title} ({year})</li>\n"
pub_html += "</ul>"

# Inject into index.html between custom markers
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- START_PUBLICATIONS -->"
end_tag = "<!-- END_PUBLICATIONS -->"
start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

# Safely replace the section
updated = content[:start_idx] + pub_html + content[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated)
