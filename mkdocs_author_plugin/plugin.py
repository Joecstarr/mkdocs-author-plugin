from pathlib import Path

import yaml
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin


class AuthorsPlugin(BasePlugin):
    config_scheme = (("authors_file", Type(str, default="authors.yaml")),)

    def __init__(self):
        self.authors = {}

    def __get_socials(self, socials) -> str:
        html = ""
        for social in socials:
            html += f"""<a class="author-icon"
                           target="_blank"
                           href="{social["link"]}"
                           title="{social["name"]}">
                               <i class="{social["icon"]}"></i>
                        </a>
                    """
        return html

    def on_config(self, config):
        """Load authors data from YAML file."""
        authors_file = self.config.get("authors_file")
        try:
            yaml_path = Path(config["docs_dir"]) / authors_file
            with yaml_path.open("r") as f:
                self.authors = yaml.safe_load(f) or {}
        except FileNotFoundError:
            print(f"Warning: Authors file '{authors_file}' not found.")
            self.authors = {}
        return config

    def on_page_markdown(self, markdown, page, config, files):
        """Process the markdown content to add author information."""
        # extract authors from the YAML front matter
        html = """<div class="authors-section">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet"/>
            <style>
            .authors-section {  margin-bottom:0px; }
            .authors-list {  font-size: .75em; gap: 10px; }
            .author-card { display: flex; align-items: center; }
            .author-image { width: 4em; height: 4em; border-radius: 50%; margin:1em; margin-left:0; }
            .author-icon { width: 1.5em; height: 1.5em; }
            .author-name {  margin-bottom:0px;   font-weight: bold;}
            .author-socials {  margin-bottom:0px; }
            .author-bio { font-size: .75em; }
            .author-list-title {margin-top:0 !important; margin-bottom:0 !important;}
            </style>
            """

        html += """<h6 class="author-list-title" >Authors</h6>"""
        if page.meta and "authors" in page.meta:
            authors_list = page.meta["authors"]
            if not isinstance(authors_list, list):
                authors_list = [authors_list]

            # create HTML for author profiles at the bottom of the page
            html += "<div class='authors-list'>"

            for author_id in authors_list:
                if author_id in self.authors:
                    author = self.authors[author_id]

                    html += f"""
                    <div class="author-card">
                        <img
                            class="author-image"
                            alt="{author["name"]} image"
                            src="{author["img"]}"
                        >
                        <div>
                            <div>
                                <p class="author-name">{author["name"]}</p>
                                <p class="author-bio">{author["bio"]}</p>
                            </div>
                            <section class="author-socials">{self.__get_socials(author["socials"])}</section>
                        </div>
                    </div>"""

            html += "</div>"
        html += "</div><hr>"
        # append the HTML to the markdown content
        html += markdown

        return html
