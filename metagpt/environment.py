#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 22:12
@Author  : alexanderwu
@File    : environment.py
"""
import asyncio
from typing import Iterable

from pydantic import BaseModel, Field

from metagpt.memory import Memory
from metagpt.roles import Role
from metagpt.schema import Message


class Environment(BaseModel):

    """
     THE ENVIRONMENT CLASS

    This class is used to create an environment for the roles to interact with each other.
    The environment hosts a batch of roles, roles can publish messages to the environment, and can be observed by other roles.

    :return: A class instance, which is the environment
    :rtype: Environment
    """
    #Environment, hosting a batch of roles, roles can publish messages to the environment, and can be observed by other roles

    roles: dict[str, Role] = Field(default_factory=dict)
    memory: Memory = Field(default_factory=Memory)
    history: str = Field(default='')

    class Config:
        arbitrary_types_allowed = True

    def add_role(self, role: Role):
        """
        The add_role function adds a role to the environment.

        :param self: Represent the instance of the class
        :param role: Role: Set the role of a person
        :return: The role
        :doc-author: Trelent
        """

        role.set_env(self)
        self.roles[role.profile] = role

    def add_roles(self, roles: Iterable[Role]):
        """
        The add_roles function adds a role to the guild.
            Parameters
            ----------
            roles : Iterable[Role]

        :param self: Represent the instance of the class
        :param roles: Iterable[Role]: Specify what type of data is expected to be passed into the function
        :return: A list of roles that were added
        :doc-author: Trelent
        """

        for role in roles:
            self.add_role(role)

    def publish_message(self, message: Message):
        """
        The publish_message function is used to publish a message to the memory.
            It takes in a message object and adds it to the memory, as well as adding it
            to the history of messages for this agent.

        :param self: Refer to the object itself
        :param message: Message: Add a message to the memory
        :return: Nothing, but it does add the message to the memory and history of the chatbot
        :doc-author: Trelent
        """

        # self.message_queue.put(message)
        self.memory.add(message)
        self.history += f"\n{message}"

    async def run(self, k=1):
        """
        The run function is the main function of a model. It runs the model for k steps,
        where k is an integer passed to it as an argument. The run function should be called
        from within a coroutine, and will return when all roles have finished running.

        :param self: Access the attributes of the class
        :param k: Define the number of times that the run function is called
        :return: A list of futures
        :doc-author: Trelent
        """

        # while not self.message_queue.empty():
        # message = self.message_queue.get()
        # rsp = await self.manager.handle(message, self)
        # self.message_queue.put(rsp)
        for _ in range(k):
            futures = []
            for role in self.roles.values():
                future = role.run()
                futures.append(future)

            await asyncio.gather(*futures)

    def get_roles(self) -> dict[str, Role]:
        """
        The get_roles function returns a dictionary of all the roles in the guild.
        The key is the role ID and value is a Role object.

        :param self: Refer to the current object
        :return: A dictionary of the roles in a guild
        :doc-author: Trelent
        """

        return self.roles

    def get_role(self, name: str) -> Role:
        """
        The get_role function takes a string as an argument and returns the role object with that name.
        If no such role exists, it returns None.

        :param self: Refer to the object itself
        :param name: str: Specify that the parameter name is a string
        :return: The role object of the name passed in
        :doc-author: Trelent
        """

        return self.roles.get(name, None)
