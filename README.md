# CSC 1019 Practice 8

## What language is it?
How often a character appears in a letter compared to other letters is known as its **relative frequency**. The relative frequency of a character can tell us some basic information about a language. Computational linguists can use character frequency as a super basic way identify the language of an unknown text.

## Task
Write code that analyzes the texts in the `resources` folder. There are four texts representing four languages in the same general family. There is also a text from a mystery language.

The `frequency.py` file contains some code for you and some code you must complete.

1. Complete the `main()` function so that performs the following functions in order **for every file in resources.**

    1. `get_file_contents`
    2. `clean_text`
    3. `get_char_count`
    4. `print_char_summary`
You will need to make sure that the return value of one function becomes the input of the next function.

2. Complete the `clean_text()` function so that it performs the task described in the docstring.

3. Complete the `get_char_count()` function so that it performs the task described in the docstring.

4. Based on the code in `print_char_summary()`, write the docstring.

5. Complete the reflection and analysis questions in `REFLECTIONS.md`. Essentially you will get outputs for each language file and summarize those in the `REFLECTIONS.md` file.

## Testing
There are no automatic tests for this practice. **I will be reviewing your code and your answers in `REFLECTIONS.md`**. Start on this practice early so you can do a good job.