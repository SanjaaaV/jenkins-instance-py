import docker
import jenkins
import sys
import requests
from docker.api import container
from configparser import ConfigParser
import argparse

parser = argparse.ArgumentParser(description = 'Jenkins server')
parser.add_argument('-s','--action_server', metavar='', help='stop,start,backup -Jenkins server.')
parser.add_argument('-c','--containerID', metavar='',required=True,  help='ID of Jenkins server container.')
parser.add_argument('-j','--action_job', metavar='', help='build or stop -job.')
parser.add_argument('-n','--job_name', metavar='', help='Name of job.')
parser.add_argument('-b','--backup_name', metavar='', help='Backup name.')
args = parser.parse_args()


#Docker
client = docker.from_env()
container = client.containers.get(args.containerID)


#main
action_server = args.action_server
if action_server == "stop":
    container.stop()
    print("Jenkins instance was stopped.")
elif action_server == "start":
    container.start()
    print("Jenkins instance was started.")

elif action_server == "backup":
    nameB = args.backup_name
    container.commit(nameB)
    print("Jenkins instance backup was made.")



action_job = args.action_job
if container.status == "running":
    config = ConfigParser()
    config.read("parametersjenkins.ini")

    config_data = config["JENKINS"]
    hostJenkins = config_data['hostjenkins']
    usernameJenkins = config_data['usernamejenkins']
    passwordJenkins = config_data['passwordjenkins']
    url_projects = config_data['url_projects']

    server = jenkins.Jenkins(hostJenkins, username=usernameJenkins, password=passwordJenkins)
    response = requests.get(url_projects)
    user = server.get_whoami()
    version = server.get_version()
    print(f'Jenkins user: {user["fullName"]} Jenkins version: {version}')
    jobs = server.get_jobs()
    if action_job == "build":       
       job_name = args.job_name
       server.build_job(job_name)
       print("Job-build.")

    elif action_job == "stop":
       job_name = args.job_name
       job_number = args.job_number
       server.stop_build(job_name, job_number)
    else:
       print("Wrong action_job argument.(build, stop)")
else:
    print("Start Jenkins server.(arguments: -s start -c containerID)")

