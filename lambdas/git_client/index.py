import logging
import os
import git
 
TMP_DIR = "/tmp"
REPO_DIR = 'Open-Source-AI-For-Robotics-Degree'
REPO_URL = f'https://github.com/thomasdunlap/{REPO_DIR}'
CLONE_PATH = os.path.join(TMP_DIR, REPO_DIR)
 
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
 
def clone(branch='master'):
   repo = git.Repo.clone_from(REPO_URL, CLONE_PATH, branch=branch)
 
   with repo.config_writer() as git_config:
       git_config.set_value('user', 'email', 'tom.a.dunlap@gmail.com')
       git_config.set_value('user', 'name', 'thomasdunlap')
  
def handler(event, context):
   LOGGER.info('Event: %s', event)
 
   LOGGER.info('Cloning repo: %s', REPO_URL)
   clone()
