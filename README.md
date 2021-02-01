# RESEARCH INFO FILTER TOOL
This is a command line python script that prompts researchers to enter a topic name, a folder to save the results to and multiple urls for research. 
The code then creates a file with the topic name in the entered directory.
Python code then saves the html from the url in a temp file, then finds each paragraph in the text and saves the paragraph to the topic file.

The process runs as follows.

1. User enters a topic name and a directory.
2. A file is created with the topic name in the chosen directory, replacing spaces with underscores eg. my_topic.txt
3. The user is then prompted to enter as many blog post urls as they like.
4. All paragraphs from the urls are saved to the topic file.

## SKILLS COVERED:
For python students, here are some of the skills covered in this simple program:

- Unit testing - (we import researchtool and test the methods in the ResearchTool class.)
- Objects, attributes and methods
- Regular Expressions (import re)
- Requests library (requests.get(), requests.raise_for_status())
- bs4 library - (finds and displays paragraphs)
