# -*- coding: utf-8 -*-
"""
Python script to Automate 'Repository-Creation' Task
Author: Shreyas Subhedar
"""
# installing SDK
# !pip install PyGithub

import os
from github import Github

readme_content = 'Automated Repository </br> Testing Python Automation  </br>// code away! </br> Repository Owner : Shreyas Subehdar'

# creating github instance by providing username-password
git = Github(os.environ.get(GITHUB_USERNAME), os.environ.get(GITHUB_PASSWORD))

# reading all repositories names
for repo in git.get_user().get_repos():
    print(repo.name)

# get user
user = git.get_user()

# create reposirty with MIT open source license
repo = user.create_repo('Automated Repository',license_template='MIT')

# creating readme File
repo.create_file('README.md', 'intial commit', readme_content)
