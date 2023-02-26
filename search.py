import sys
import webbrowser

valid_websites = [
  "stackoverflow.com",
  "medium.com",
  "reddit.com"
]

url = "https://www.google.com/search?q="

def create_filter():
  filter = "("
  for index, website in enumerate(valid_websites):
    filter +='site: ' + website
    if index == len(valid_websites) - 1:
      filter += ')'
    else:
        filter += ' OR '
  return filter

def create_querry():
  query = sys.argv[1:]
  return ' '.join(query)

def create_url():
  if len(sys.argv[1:]) == 0:
    print("Please enter a valid argument")
  else:
    final_url = url + create_querry() + create_filter()
    webbrowser.open(final_url)

create_url()