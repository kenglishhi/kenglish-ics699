"""Setup the bio1 application"""
import logging

from paste.deploy import appconfig
from pylons import config

from bio1.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_config(command, filename, section, vars):
    """Place any commands to setup bio1 here"""
    conf = appconfig('config:' + filename)
    load_environment(conf.global_conf, conf.local_conf)
