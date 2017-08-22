#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
       distributes an archive to your web servers
Returns False if the file at the path archive_path doesn't exist
"""
import os.path
import time
from fabric.api import *
from fabric.operations import run, put, sudo
from datetime import date
env.hosts = ['66.70.184.210', '142.44.164.128']


def do_pack():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None


def do_deploy(archive_path):
    """ script that distributes archive to web servers
    All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    Returns True if all operations has been done correctly,
            otherwise returns False
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])
        run("sudo mkdir -p {:s}".format(folder))

        """Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server"""
        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(unpack, folder))

        """Delete the archive from the web server"""
        run("sudo rm /tmp/{:s}".format(unpack))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))

        """Delete the symbolic link /data/web_static/current"""
        run('sudo rm -rf /data/web_static/current')

        """Create a new the symbolic link
           /data/web_static/current on the web server, linked to the new
           version of your code
           (/data/web_static/releases/<archive filename without extension>)"""
        run("sudo ln -s {:s} /data/web_static/current".format(folder))
        return True
    except:
        return False


def deploy():
    try:
        my_archive_path = do_pack()
        deploythis = do_deploy(my_archive_path)
        return deploythis
    except:
        return False
