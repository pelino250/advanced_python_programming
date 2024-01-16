# Asynchronous programming
# allows for multiple things to happen at once
# async programming is a style of programming that allows you to run multiple functions at the same time
#  rather than blocking code execution until a task is complete


# advantages of async programming:
# 1 - faster execution
# 2 - efficient resource utilization
# 3 - better user experience


# async programming in python:
# async programming in python is achieved using coroutines
# coroutines are functions that can pause execution and return control to the caller
#  without losing their state
# coroutines are declared using the async/await syntax
# coroutines can be executed using the asyncio module

# example of async programming:
import asyncio  # pypi.org/project/asyncio
import time


async def hello_world():
    print('Hello')
    await asyncio.sleep(1)
    print('World')


# run the coroutine
asyncio.run(hello_world())

# Event loop:
# the event loop is the core of every asyncio application
# it runs in a thread and executes all tasks and callbacks
# the event loop uses cooperative multitasking
# the event loop is in charge of scheduling tasks and callbacks

# event loop steps of managing tasks:
# 1 - Async tasks added to the event loop's task queue
# 2 - continually checks if the task queue for tasks to execute
# 3 - the event loop executes the tasks until they are complete or await is called
# 4 - the event loop stops when the tasks are complete


# example of event loop:
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)


# example of async programming with asyncio that involves an API call:
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        todos = await fetch(session, 'https://jsonplaceholder.typicode.com/todos')
        print(todos)


# Run the function
asyncio.run(main())

# common use cases for async programming:
# 1 - data processing
# 2 - web scraping
# 3 - web servers
# 4 - API calls
# 5 - UI interfaces
# 6 - real-time operations
