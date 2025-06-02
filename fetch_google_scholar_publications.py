from scholarly import scholarly

author = scholarly.search_author_id("BDil2hgAAAAJ")
filled = scholarly.fill(author)

# Create the publication list HTML
pub_list = "<ul>\n"
for pub in filled['publications'][:5]:
    title = pub['bib'].get('title', 'No Title')
    year = pub['bib'].get('pub_year', '')
    pub_list += f"<li>{title} ({year})</li>\n"
pub_list += "</ul>"

# Inject into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_tag = "<!-- START_PUBLICATIONS -->"
end_tag = "<!-- END_PUBLICATIONS -->"
start_idx = html.find(start_tag) + len(start_tag)
end_idx = html.find(end_tag)
new_html = html[:start_idx] + pub_list + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
