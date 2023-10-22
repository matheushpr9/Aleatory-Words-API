# Motivation

When i developed my word-guessing game, i felt the need to create a radom word API so that i could use it in my game. So i decided to make the project documented and available to everyone

## **ModuleNotFoundError: No module named 'xxx'**

when I was developing this project, I came across the above error when trying to execute some files, in case you're having the same problem I'll help you fix it.

After researching I discovered that the error occurs due to the way python imports modules, and even after adding the *__init__.py* files, the error persisted.

So I created the *setup.py* file in the root of the project, and ran the following command in my terminal (also in the root of the project):

``` shell

pip install -e .

```

if you know another way to fix this bug, I'd be happy to receive your pull request or feedback.

---

## Run  it

run the server:

'''
uvicorn main:app --reload
'''
