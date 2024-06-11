# Async Comprehension in Python

This repository contains solutions for the project "0x02. Python - Async Comprehension" as part of the ALX Back-end Python curriculum.

## Description

In this project, you'll learn about asynchronous generators, async comprehensions, and type-annotating generators in Python. The project consists of several tasks, each focusing on different aspects of asynchronous programming.

## Learning Objectives

By completing this project, you will gain proficiency in the following:

- Writing asynchronous generators
- Utilizing async comprehensions
- Type-annotating generators

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Use pycodestyle style (version 2.5.x)
- Length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Functions and coroutines must be type-annotated

### Tasks

1. **Async Generator**: Write a coroutine called `async_generator` that yields random numbers asynchronously.
2. **Async Comprehensions**: Write a coroutine called `async_comprehension` to collect random numbers using async comprehensions.
3. **Run time for four parallel comprehensions**: Write a coroutine `measure_runtime` to execute async_comprehension four times in parallel using `asyncio.gather` and measure the total runtime.

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#async-generators-and-comprehensions)
- [Type-hints for generators](https://www.python.org/dev/peps/pep-0484/#type-hints-for-generators)

## Instructions

Clone the repository and execute the scripts for each task to verify the implementation.

## Repo Details

- **GitHub repository:** [alx-backend-python](https://github.com/your-username/alx-backend-python)
- **Directory:** 0x02-python_async_comprehension

## Files

- **0-async_generator.py**: Contains the implementation of the async generator.
- **1-async_comprehension.py**: Implements the coroutine to collect random numbers using async comprehensions.
- **2-measure_runtime.py**: Measures the total runtime for executing async comprehensions four times in parallel.

## Usage

Execute the respective Python scripts to run and test each task.

```bash
$ python3 0-main.py
$ python3 1-main.py
$ python3 2-main.py
```

## Author

This project is developed by [Your Name] for ALX School.
