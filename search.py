import sys
import webbrowser

class Cmd_Search:
  def __init__(self, prompt):
    self.url = "https://www.google.com/search?q="
    self.prompt = prompt
    self.valid_websites = [
      "stackoverflow.com",
      # "medium.com",
      # "reddit.com"
    ]
    
    self.search()

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

  def search(self):
    if len(self.prompt) == 0:
      print("Please enter a valid query...")
    else:
      query = self.url + " ".join(self.prompt)
      webbrowser.open(query)

obj = Cmd_Search(sys.argv[1:])
