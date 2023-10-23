# Motivation

When i developed my word-guessing game, i felt the need to create a radom word API so that i could use it in my game. So i decided to make the project documented and available to everyone

## **ModuleNotFoundError: No module named 'xxx'**

when I was developing this project, I came across the above error when trying to execute some files, in case you're having the same problem I'll help you fix it.

After researching I discovered that the error occurs due to the way python imports modules, and even after adding the ***init**.py* files, the error persisted.

So I created the *setup.py* file in the root of the project, and ran the following command in my terminal (also in the root of the project):

``` shell

pip install -e .

```

if you know another way to fix this bug, I'd be happy to receive your pull request or feedback.

---

## Run  it

In the app folder run the server:

'''
uvicorn main:app --reload
'''

## Endpoints

Currently only have a single endpoint:

``` http
/word/{language}
```

Which accepts as a parameter the language which the requester wants the words.

For now, we have the following language options:

- portuguese
- english

### Query Params

When making a GET request at the */word/{language}* endpoint, a dictionary with the following structure is returned:
> {\
> "_id": xxx\
> "lower": word_in_lower,\
> "upper": word_in_upper,\
> "capitalize": word_in_capitalize,\
> "length": word_length\
> }

In addition, this endpoint accepts a query param, though which the requester can specify which of the options they want:

- id
- lower
- upper
- capitalize
- length
