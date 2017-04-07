# Python: Tips, Tricks, and Aberrations

[presentation](https://docs.google.com/presentation/d/1gx5rrco8Ha7thLWT8SleLtG5zBSWY8kfWAZJvc7PQWE/edit?usp=sharing)

## Good to know

### The Zen of Python

Idea of "Pythonic"

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### PEP8

Please actually read PEP 8. 

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.
> However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment.
> In particular: do not break backwards compatibility just to comply with this PEP!

The goal is readability. 

Use 4 spaces for indentation. 

Put imports on separate lines.

Avoid wildcard (`from spam import *`) imports.

For block strings and docstrings use the triple *double*-quote method `"""like this"""`.

Don't use extra whitespace [examples](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)

Avoid putting multiple statements on the same line.

Keep comments up to date with code changes. 

Use inline comments sparingly. If you do use them:  
```python
code_things()  # Separate by two spaces before the pound then one after
```

Write docstrings for all public modules, functions, classes, and methods. (You should probably still have docstrings for private things as well.) See [PEP 257](https://www.python.org/dev/peps/pep-0257)

Naming Conventions
    * Modules should have short, all-lowercase names and can use underscores if needed. 
    * Class names should be CamelCase.
    * Type variable names should be CamelCase.
    * Functions should be lowercase with words separated by underscores.
    * Non-public or instance variables can begin with a single underscore. (Using a beginning double underscore will invoke name mangling. Don't use this unless you _really_ know why you need it.)
    * Constants are usually defined on the module level and are all caps (with underscores).
    * Names should be descriptive

Don't use getters/setters. Instead, just expose the attribute.

When comparing to singletons such as `None`, use is/is not instead of testing equality. 

If you are assigning a lambda to a variable, use a function instead. 

Limit `try` statements to the smallest section of code possible. 

Either all return statements in a function should return an expression, or none of them should. (Explicitly `return None` is fine.)

Object type comparisons shoud be done with `isinstance` instead of comparing to `type(spam)`. (I'm not happy about this one. -Sean)

PEP 8 mentions [PEP 484](https://www.python.org/dev/peps/pep-0484/) on type hinting. I think this would be useful, but I don't know if I recommend going all out to the extent that we can invoke type checking. I'd instead recommend using this just to improve readability. 

### List Comprehsions, Lambdas, Dicts, Slicing

### Logging
OMG I love logging.

[logging example](logging.py)

```
>>> import logging_example
>>> import logging
>>> mylog = logging.getLogger(__name__)
>>> logging.basicConfig()
>>> mylog.setLevel("DEBUG")
>>> mylog.debug("lol")
DEBUG:__main__:lol
>>> mylog.setLevel("INFO")
>>> mylog.debug("lol")
>>> logging_example.spam()
ERROR:logging_example:Whoops, that math didn't work
Traceback (most recent call last):
  File "/home/duck/wcsc/Python_Presentation_WCSC/logging_example.py", line 20, in spam
    baz = 1 / i
ZeroDivisionError: division by zero
>>> logging.setLevel("DEBUG")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'setLevel'
>>> log = logging.getLogger()
>>> log.setLevel("DEBUG")
>>> logging_example.spam()
DEBUG:logging_example:Running an example
INFO:logging_example:Found the number 3
ERROR:logging_example:Whoops, that math didn't work
Traceback (most recent call last):
  File "/home/duck/wcsc/Python_Presentation_WCSC/logging_example.py", line 20, in spam
    baz = 1 / i
ZeroDivisionError: division by zero
>>> 
```


### Use Python3

####Bytes vs. Unicode
```
>>> mystr = "hello"
>>> type(mystr)
<class 'str'>
>>> mybytes = b"hello"
>>> type(mybytes)
<class 'bytes'>
>>> mystr.encode("utf-8")
b'hello'
>>> mystr.encode("cp1256")
b'hello'
```

I need to actually learn this more....


### Pip
Don’t be afraid of using 3rd party libs

### Multiprocessing vs Threading

### Pwntools
The best thing since sliced bread
Read through the docs. There is _SOOO FRIGGING MUCH_ in this library

#### Mbruteforce
#### Logging
#### Asm
Rop
Printf

Crazy things
Pre-instantiated ints
Is vs equals
```
>>> a = 1
>>> b = 1
>>> a == b
True
>>> a is b
True
>>> a = 1337
>>> b = 1337
>>> a == b
True
>>> a is b
False
```

Stack introspection
logging


Exploitable things
[Deserialization](https://v0ids3curity.blogspot.com/2012/10/exploit-exercise-python-pickles.html)



