import sys
import webbrowser

class Cmd_Search:
  def __init__(self):
    self.url = "https://www.google.com/search?q="
    self.valid_websites = [
      "stackoverflow.com",
      # "medium.com",
      # "reddit.com"
    ]

  def apply_filter(self, filter):
    # Do nothing for now think about how to best apply this
    #   filter = "("
    # for index, website in enumerate(valid_websites):
    #   filter +='site: ' + website
    #   if index == len(valid_websites) - 1:
    #     filter += ')'
    #   else:
    # filter += ' OR '
    # return filter
    return

  def search(self, seed):
    if len(seed) == 0:
      print("Please enter a valid query...")
    else:
      query = self.url + " ".join(seed)
      webbrowser.open(query)

obj = Cmd_Search()
cmd = sys.argv[1:]
obj.search(sys.argv[1:])