"""公式のリポジトリのパッケージ一覧からリストに含まれないプラグインやテーマを探す"""
from collections.abc import Iterator
from pathlib import Path
from urllib.request import urlopen

from bs4 import BeautifulSoup

PLUGIN_LIST_URL = "https://github.com/gatsbyjs/gatsby/tree/master/packages"
THEME_LIST_URL = "https://github.com/gatsbyjs/themes/tree/master/packages"

PATH_README = Path(__file__).resolve().parent.parent / "README.md"


def main() -> None:
    with PATH_README.open() as f:
        content = f.read()

    print("Missing plugins:")
    plugins = fetch_names_in_github_repo_dir(PLUGIN_LIST_URL)
    for plugin in yield_missing(plugins, content):
        print(plugin)
    print()

    print("Missing themes:")
    themes = fetch_names_in_github_repo_dir(THEME_LIST_URL)
    for themes in yield_missing(themes, content):
        print(theme)
    print()


def yield_missing(names: str, content: str) -> Iterator[str]:
    return (name for name in names if name not in content)


def fetch_names_in_github_repo_dir(url: str) -> list[str]:
    with urlopen(url) as f:
        body = f.read()
    soup = BeautifulSoup(body, "html.parser")
    selector = '.repository-content [aria-labelledby="files"] .Link--primary'
    return [x.text for x in soup.select(selector)]


if __name__ == "__main__":
    main()
