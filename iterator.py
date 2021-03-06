import json
import wikipedia


class WikiCountries:

    def __init__(self):
        self.i = 0
        with open('countries.json', 'rb') as f:
            self.data = f.read()
        self.data = json.loads(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > len(self.data) - 1:
            raise StopIteration
        else:
            name = self.data[self.i]['name']['common']
            try:
                wiki_page = wikipedia.page(name)
            except wikipedia.DisambiguationError:
                wiki_page = wikipedia.page(f'{name} (country)')
            pair = {name: wiki_page.url}
            with open('countries_wiki_urls.txt', 'a') as outfile:
                json.dump(pair, outfile, indent=2)
            self.i += 1
