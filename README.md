# command-line-search
Allows user to use command line to enter a prompt that will open a search window
Or allow user to ask a question directly to chatgpt.

# Getting Started
1. `pip install -r requirements.txt`.
2. Create a `.env` file 
3. Head over to [openai](https://openai.com/) create an accout, and generate your API Key.
4. Inside the `.env` file, create a variable called `API_KEY` and assign the key from #3.
  `API_KEY = "YOUR-API-KEY"`

note: OpenAI ChatGPT is "free". Your are given certain amount of credits to spend.
Once those are spent you might need to pay for more credits. 
Be mindfull of that when using this tool.

# How to use
Add seach.py and search_gpt.py as aliases in your .bashrc file (or whatver you use)

`alias s='python3 path/to/repo/command-line-search/search.py'`

`alias sgpt='python3 path/to/repo/command-line-search/search_gpt.py'`

Then source your .bashrc

`source .bashrc`

Finally, just write a query

`s how to be rich quick`, `s -f how to be write good code` or `sgpt how to make by gf happy`

The `-f` flag on the `search.py` script will apply a filter to search only on stackoverflow

In case of a query using `search.py` a list with the top 10 links will be displayed in the terminal

In case of a query using `search_gpt.py` your response will be displayed in the terminal.

# Linting
The project uses the python's Flake8 to check formatting style. It can be run locally by using
```
flake8
```
And if there are violations they will be printed in the terminal

# TODO
- Allow insertion of websites to query (filter websites).
