import connect
from models import Author, Quote
import json

def search_by_name(name: str) -> set[Quote]:
    quotes = set()
    authors = Author.objects.filter(name__icontains=name)
    for author in authors:
        quotes.update(Quote.objects.filter(author=author.id))
    return quotes

def search_by_tag(tags: tuple[str]) -> set[Quote]:
    quotes = set()
    for tag in tags:
        quotes.update(Quote.objects(tags__icontains=tag))
    return quotes

def print_quotes(quotes: set[Quote]) -> None:
    result = "/n".join([[quote.author.name, quote.quote, ", ".join(quote.tags)] for quote in quotes])
    print(result)
    
def main() -> None:
    while True:
        user_input = input('Enter command: ')
        search_by, search = user_input.split(':')
        match search_by:
            case 'name':
                result = search_by_name(entry)
            case 'tag':
                entry = tuple(entry.split(','))
                result = search_by_tag(entry)
            case 'exit':
                break
            case _:
                print('wrong search by field')
        print_quotes(result)
        
if __name__ == "__main__":
    main()