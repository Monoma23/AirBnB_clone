#!/usr/bin/python3
"""
Fabric script extending 1-pack_web_static.py, facilitating the distribution
of an archive to designated web servers.
"""

from fabric.api import put, run, env
from os.path import exists

# Define web server hosts
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """Distributes the specified archive to the web servers."""
    # Check if the archive exists
    if exists(archive_path) is False:
        return False
    
    try:
        # Extract necessary information from the archive path
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        # Transfer archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')
        
        # Create directory and extract contents
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        
        # Move extracted content to the correct location
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        
        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        
        return True
    except:
        return False
