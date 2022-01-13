#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") is False:
            local("mkdir version")
        file_name = "version/web_statics_{}.tgz".format(date)
        local("tar -cvf {} web_static".format(file_name))
        return file_name
    except:
        return None
