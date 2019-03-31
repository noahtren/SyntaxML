(From [devpost](https://devpost.com/software/syntaxml))
## Inspiration
We knew we wanted to do something educational, specifically for programmers. Our first idea was to generate flash cards with code snippets that a programmer often forgets. 
## What it does
We changed our idea when we considered that a programmer could quickly access syntax patterns at exactly the time they forget it, and this would make them a much more productive programmer. Our program pulls a code snippet from a curated database of common syntactical structures based on a natural language search. For example, searching `reverse a list` and `make a list backwards` and `make a list go the other way` returns the following code snippet in the context of Python:
```python
array=[0,10,20,40]
array=list(reverse(array))
```
Another example is `make an item from a list go bye bye`, which returns the code:
```python
numbers = [0,2,4,5]
numbers.remove(2)
```

## How we built it
We used a lot of different technologies which ultimately resulted in a Flask server that makes use of both a custom classification algorithm and a package containing a trained model on vector representations of words, called word2vec. This model was implemented through the Gensim Python package, As it required a lot of computing power, we made use of our Google Cloud Credit and have an instance of a 16 vCPU Compute Engine Instance. This provides quick computations for a lag-free website.
## Challenges we ran into
Where do we get started? Two words: web scraping. We tried many techniques to extract relevant code snippets algorithmically, but this was much harder than we anticipated. This partially speaks towards why we think our program is so helpful -- it is hard to quickly find the basic syntax you want by searching somewhere like StackOverflow because there are many irrelevant answers. We eventually decided to curate our database of solutions by hand. We have around 50 relevant code snippets in the dataset which cover simple operations including working with iterables, files, data type manipulation, and string manipulation. Our dataset currently contains relevant snippets for 3 programming languages: Python, C++, and JQuery. 
## Accomplishments that we're proud of
We believe that we've created something very helpful by making use of machine learning research. This is a very practical and feasible application as shown by the demo on our website. We hope it can be used as an extension in text editors such as VS Code or Vim to quickly lookup syntax without having to search the Internet.
## What we learned
This was our first time working with machine learning, and we are happy to have made something that works very well. This was accomplished by using previously trained models from accomplished machine learning research. Then we were able to apply it by running a compute engine in the cloud. We also learned that web scraping is hard if you want clean, structured data all the time.
## What's next for SyntaxML
We are very excited about this project, and definitely want to see it become an extension for the most popular text editors. We also want to improve and extend our database so that more common syntax structures can be quickly returned to the user.
