import sys
import webbrowser


class Cmd_Search:
    def __init__(self, prompt):
        self.url = "https://www.google.com/search?q="
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
        # Do nothing for now think about how to best apply this
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
            query = self.url + " ".join(self.prompt) + filter
            webbrowser.open(query)


obj = Cmd_Search(sys.argv[1:])
