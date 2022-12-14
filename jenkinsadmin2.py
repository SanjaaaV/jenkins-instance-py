from api4jenkins import Jenkins
import sys
import requests 
import docker 
from docker.api import container
from configparser import ConfigParser
import argparse

parser = argparse.ArgumentParser(description = 'Jenkins server')
parser.add_argument('-s','--action_server', metavar='', help='stop,start,backup -Jenkins server.')
parser.add_argument('-j','--action_job', metavar='', help='build or stop -job.')
parser.add_argument('-n','--job_name', metavar='', help='Name of job to build/stop.')
parser.add_argument('-b','--backup_name', metavar='', help='Backup name.')
parser.add_argument('-c','--container', metavar='', help='container ID.')
args = parser.parse_args()




config = ConfigParser()
config.read("parametersjenkins.ini")

config_data = config["JENKINS"]
hostJenkins = config_data['hostjenkins']
usernameJenkins = config_data['usernamejenkins']
passwordJenkins = config_data['passwordjenkins']
url_projects = config_data['url_projects']

server = Jenkins(hostJenkins, auth=(usernameJenkins,passwordJenkins))


client = docker.from_env()

#server
action_server = args.action_server
if action_server == "stop":
    server.system.quiet_down()
    print("Jenkins instance was stopped.")
elif action_server == "start":
    server.system.cancel_quiet_down()
    print("Jenkins instance was started.")

elif action_server == "backup":
    if args.backup_name:
       if args.container:
          IDcontainer = args.container
          container = client.containers.get(IDcontainer)
          nameB = args.backup_name
          container.commit(nameB)
          print("Jenkins instance backup was made.")
       else:
          print("Add containerID.(-c)")
    else:
       print("Add backup_name.(-b)")



#job
job_name = args.job_name
action_job = args.action_job

if action_job == "build":
    if args.job_name:
       job = server.get_job(job_name)       
       job.build()
       print(server.build_job(job_name))
       print("Job-build.")
    else:
       print("Add job_name.(-n)")

elif action_job == "stop":
    if args.job_name:
       job = server.get_job(job_name)
       build = job.get_last_build()
       print (build)
       build.stop()
    else:
       print("Add job_name.(-n)")



