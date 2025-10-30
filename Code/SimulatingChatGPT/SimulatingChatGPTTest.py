"""
Simulating ChatGPT Locally – Solutions
These exercises allow you to enhance the capabilities of the simulated ChatGPT function. 
The exercises emphasise the importance of conditional logic in determining appropriate responses.
Exercise 1: Problem: Expand the simulated_chatgpt function to handle questions about the weather, e.g., 
"How's the weather today?". It should return a random weather condition from a list, like ["sunny", "cloudy", "rainy"].
Exercise 2: Problem: Enhance the simulated_chatgpt function so that when asked, 
"Tell me a joke", it responds with a random joke from a predefined list of jokes.

在本地模拟ChatGPT–解决方案
这些练习允许您增强模拟的ChatGPT函数的功能。这些练习强调了条件逻辑在确定适当反应中的重要性。
练习1：问题：展开simulated_chatgpt函数以处理有关天气的问题，例如“今天天气怎么样？”。
它应该从列表中返回一个随机的天气条件，如[“晴天”、“阴天”、“雨天”]。
练习2：问题：增强simulated_chatgpt函数，这样当被问到“给我讲个笑话”时，它会从预定义的笑话列表中随机返回一个笑话。

"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:00:57 2023
@author: mireilla
"""
import random

def simulated_chatgpt(query):
    """
    A simple function to simulate ChatGPT's response based on given queries.

    Parameters:
    - query (str): The user's question/input

    Returns:
    - str: The simulated response from ChatGPT
    """
    # Lowercase the query for consistent matching
    query = query.lower()

    if "hello" in query:
        return "Hello there!"
    elif "how are you" in query:
        return "I'm just a simulation, so I don't have feelings. But thanks for asking!"
    elif "recommend a book" in query:
        return "I suggest reading 'To Kill a Mockingbird' by Harper Lee. It's a classic!"
    elif "how's the weather" in query:
        weather_conditions = ["sunny", "cloudy", "rainy"]
        return f"It's {random.choice(weather_conditions)} today!"
    elif "tell me a joke" in query:
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems."
        ]
        return random.choice(jokes)
    else:
        return "Sorry, I'm not sure how to respond to that."

# Let's test the simulation:
print(simulated_chatgpt("Hello"))  # Output: "Hello there!"
print(simulated_chatgpt("Can you recommend a book?"))
print(simulated_chatgpt("How are you?"))
print(simulated_chatgpt("How's the weather?"))