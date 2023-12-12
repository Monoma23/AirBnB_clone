#!/usr/bin/python3
"""
Fabric script to create a compressed tgz archive from the web_static folder
in the AirBnB Clone repository.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Generates a tgz archive containing web_static contents."""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
