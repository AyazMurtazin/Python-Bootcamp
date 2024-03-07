import argparse
import wikipediaapi
import logging
import json

MAX_PAGES: int = 1000
WIKIPEDIA_BASE_URL: str = 'https://en.wikipedia.org'
DEFAULT_START_PAGE: str = "Wikipedia:Very short featured articles"
DEFAULT_DEPTH: int = 1

graph: dict = dict()
counter = MAX_PAGES

wikipedia = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Finding nested links on a Wikipedia page with a certain depth')
    parser.add_argument(
        '-d',
        '--depth',
        type=int,
        default=DEFAULT_DEPTH,
        help='Search depth (3 by default)')
    parser.add_argument(
        '-p',
        '--page',
        type=str,
        default=DEFAULT_START_PAGE,
        help='Start page'
    )
    arguments = parser.parse_args()
    return arguments


def logger(parrent_title, childs) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info(f"--- {parrent_title} connected with {childs} ---")


def get_depth_wiki_internal_links(title: str, depth: int):
    if get_wiki_internal_links(title):
        if depth != 0:
            for i in graph[title]:
                get_depth_wiki_internal_links(i, depth - 1)


def get_wiki_internal_links(title: str):
    global counter
    page = wikipedia.page(title)
    if title not in graph and counter > 0:
        linked_with = list(page.links.keys())
        if(len(linked_with) > counter):
            linked_with = linked_with[:counter]
            graph[title] = list(linked_with)
            counter = 0
            return False
        graph[title] = list(linked_with)
        counter -= len(linked_with)
        return True
    else:
        return False


def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_arguments()
    start_page_name = args.page
    depth = args.depth
    get_depth_wiki_internal_links(start_page_name, depth)
    with open('wiki.json', 'w') as json_file:
        json.dump(graph, json_file)


if __name__ == "__main__":
    main()
