#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 14:45
@Author  : alexanderwu
@File    : llm.py
"""

from metagpt.provider.anthropic_api import Claude2 as Claude
from metagpt.provider.openai_api import OpenAIGPTAPI as LLM

DEFAULT_LLM = LLM()
# CLAUDE_LLM = Claude()
#note: default is to be OpenAI's GPT-3
#note: Claude2 is the anthropic.ai API

DEFAULT_LLM = LLM()
CLAUDE_LLM = Claude()
OPEN_AI_GPT3 = LLM()



async def ai_func(prompt):
  """
  The ai_func function is the main function that will be called by the bot.
  It takes in a prompt, which is a string of text that was sent to the bot.
  The function should return an answer, which is also a string of text.

  :param prompt: Get the user's input
  :return: A string, which is the next message to send
  :doc-author: Trelent
  """

    return await DEFAULT_LLM.aask(prompt)
