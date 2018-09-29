StackExchange
------------------

Description
------------------
A Friendly wrapper for StackExchange public API used to harvest information about Questions, Answers
and even search for questions.

Installation:
------------------

you can install StackExchange from its official PyPI repository.


    $ pip install stackexchange
   


Usage
------------------

searching
------------------

We can use the StackExchange search API to search in various titles


    from stackexchange import search

    g = search("python", site="stackoverflow", order="desc")

    for item in g:

        print item.title

        print dir(item)


answers
------------------

Let's look at the answer API now.


    from stackexchange import Answer

    a = Answer('stackoverflow')

    g = a.get_all_answer(order="desc", page=1)

    for item in g:

        answer_id = item.answer_id

        ans = a.get_by_id(answer_id)

        comments = a.get_comments(answer_id)

        print (comments)


questions
------------------

On Questions API


    from stackexchange import Question

    q = Question('stackoverflow')

    g = q.get_all_questions(order="desc")

    for item in g:
        question_id = item.question_id

        ques = q.get_by_id(question_id)

    g = q.get_unanswered()

    g = q.get_featured()


License
------------------

MIT
