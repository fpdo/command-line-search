import sys
from googlesearch import search


class Cmd_Search:
    def __init__(self, prompt):
        self.filter = ''
        if (prompt[0] == "-f"):
            self.filter = prompt[0]
            self.prompt = prompt[1:]
            self.valid_websites = ["stackoverflow.com"]
            self.filter = self.apply_filter()
        else:
            self.prompt = prompt

        self.search(self.filter)

    def apply_filter(self):
        filter = "("
        for index, website in enumerate(self.valid_websites):
            filter += 'site: ' + website
            if index == len(self.valid_websites) - 1:
                filter += ')'
            else:
                filter += ' OR '
        return filter

    def search(self, filter):
        if len(self.prompt) == 0:
            print("Please enter a valid query...")
        else:
            self.query = " ".join(self.prompt) + self.filter
            for links in search(self.query, tld="co.in", num=10, stop=10,
                                pause=1):
                print(links)


obj = Cmd_Search(sys.argv[1:])
