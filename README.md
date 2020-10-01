# RESEARCH INFO FILTER TOOL
This is a command line python script that prompts researchers to enter urls and then decide whether to save each paragraph to a file for later.
The process runs as follows.

1. User enters a topic name.
2. A file is created with the topic name, replacing spaces with underscores eg. my_topic.txt
3. The user is then prompted to enter a blog post url.
4. The user is then presented with each paragraph from the blog post, one by one, and is asked if this paragraph is useful to them.
5. If the user opts to save the paragraph, it is saved in the topic file.
6. When all paragraphs from that blog post have been filtered, the user can either end the program or enter another url and repeat the process.

## SKILLS COVERED:
For python students, here are some of the skills covered in this simple program:

- Unit testing - (we import researchtool and test the methods in the ResearchTool class.)
- Objects, attributes and methods
- Regular Expressions (import re)
- Requests library (requests.get(), requests.raise_for_status())
- bs4 library - (finds and displays paragraphs)
