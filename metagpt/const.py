#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/1 11:59
@Author  : alexanderwu
@File    : const.py
"""
from pathlib import Path


def get_project_root():
    """
    The get_project_root function is used to find the root directory of a project.
    It does this by looking for the existence of either a .git or .project_root file in
    the current working directory, and if it doesn't find one, it looks in its parent
    directory. It continues doing this until it finds either a .git or .project_root file,
    or until there are no more parent directories left to look through (in which case an exception is raised).

    :return: The path to the root of the project
    :doc-author: Trelent
    """

    current_path = Path.cwd()
    while True:
        if (current_path / '.git').exists() or \
           (current_path / '.project_root').exists() or \
           (current_path / '.gitignore').exists():
            return current_path
        parent_path = current_path.parent
        if parent_path == current_path:
            raise Exception("Project root not found.")
        current_path = parent_path


PROJECT_ROOT = get_project_root()
DATA_PATH = PROJECT_ROOT / 'data'
WORKSPACE_ROOT = PROJECT_ROOT / 'workspace'
PROMPT_PATH = PROJECT_ROOT / 'metagpt/prompts'
UT_PATH = PROJECT_ROOT / 'data/ut'
SWAGGER_PATH = UT_PATH / "files/api/"
UT_PY_PATH = UT_PATH / "files/ut/"
API_QUESTIONS_PATH = UT_PATH / "files/question/"
YAPI_URL = "http://yapi.deepwisdomai.com/"
TMP = PROJECT_ROOT / 'tmp'
RESEARCH_PATH = DATA_PATH / "research"

MEM_TTL = 24 * 30 * 3600
