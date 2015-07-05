##StackExchange

[![Build Status](https://travis-ci.org/plasmashadow/stackexchange.svg?branch=master)](https://travis-ci.org/plasmashadow/stackexchange)
[![PyPI version](https://badge.fury.io/py/stackexchange.svg)](http://badge.fury.io/py/stackexchange)
[![PyPI](https://img.shields.io/pypi/dm/stackexchange.svg)](https://pypi.python.org/pypi/stackexchange)

##Description
A Friendly wrapper for stackexchange public api used to harvest information about Questions, Answers
and even search for questions.

##Installation:

you can install stackexchange from its official pypi repository.

```python
   pip install stackexchange
   
```

##Usage

###searching

We can use the stackexchange search api to search in various titles

```python

from stackexchange import search

g = search("python", site="stackoverflow", order="desc")

for item in g:
	print item.title
	# will help you to see all properties it contains
	print dir(item)

```

### answers

Let's look at the answer api now.

```python

from stackexchange import Answer

a = Answer()
g = a.get_all_answer(site="stackoverflow", order="desc", page=1)

for item in g:
    answer_id = item.answer_id
    ans = a.get_by_id(answer_id)
    comments = a.get_comments(answer_id)
    print comments
```

###questions

On Questions api

```python

from stackexchange import Question

q = Question()

g = q.get_all_questions(site="stackoverflow", order="desc")

for item in g:
    question_id = item.question_id
    ques = q.get_by_id(question_id)
    
 #for getting unanswered questions

g = q.get_unanswered()
 
 #for getting featured questions

g = q.get_featured()
    
```


##License

<h4> MIT </h4>
