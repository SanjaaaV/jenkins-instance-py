import sys
import time
import argparse
from configparser import ConfigParser
from api4jenkins import Jenkins
from docker.api import container
from requests.auth import HTTPBasicAuth
import requests
import docker


parser = argparse.ArgumentParser(description="Jenkins server")
parser.add_argument(
    "-s", "--action_server", metavar="", help="stop,start,backup -Jenkins server."
)
parser.add_argument("-j", "--action_job", metavar="", help="build or stop -job.")
parser.add_argument("-n", "--job_name", metavar="", help="Name of job to build/stop.")
parser.add_argument("-b", "--backup_name", metavar="", help="Backup name.")
parser.add_argument("-c", "--container", metavar="", help="container ID.")
args = parser.parse_args()


config = ConfigParser()
config.read("parametersjenkins.ini")

# jenkins connection
config_data = config["JENKINS"]
host_jenkins = config_data["hostjenkins"]
username_jenkins = config_data["usernamejenkins"]
password_jenkins = config_data["passwordjenkins"]
url_projects = config_data["url_projects"]

server = Jenkins(host_jenkins, auth=(username_jenkins, password_jenkins))


# SERVER
def serverstatus():
    r = requests.get(
        host_jenkins, auth=HTTPBasicAuth(username_jenkins, password_jenkins)
    )
    response = r.content
    str_response = str(response, "UTF-8")
    isdown = str_response.find("Jenkins is going to shut down")
    if isdown == -1:
        return "up"
    else:
        return "down"


def stopserver():
    server.system.quiet_down()
    print("Jenkins instance-stopped.")
    serverstatus()
    response = serverstatus()
    return response


def startserver():
    server.system.cancel_quiet_down()
    print("Jenkins instance-started.")
    response = serverstatus()
    return response


def backupserver(name_b, container):
    id_container = container
    container = client.containers.get(id_container)
    container.commit(name_b)
    print("Jenkins instance-backup created.")
    image_b = client.images.get(name_b)
    return image_b


action_server = args.action_server
if action_server == "stop":
    stopserver()

elif action_server == "start":
    startserver()

elif action_server == "backup":
    if args.backup_name:
        if args.container:
            client = docker.from_env()
            id_container = args.container
            name_b = args.backup_name
            backupserver(name_b, id_container)
        else:
            print("Add containerID.(-c)")
    else:
        print("Add backup_name.(-b)")


# JOBS
def build(job_name):
    job = server.get_job(job_name)
    item = job.build()
    while not item.get_build():
        time.sleep(1)
    build = item.get_build()
    print(build)
    print("Job-building.")
    return build.building


def stop_build(job_name):
    job = server.get_job(job_name)
    build = job.get_last_build()
    print(build)
    if build.building:
        build.stop()
        while build.building:
            time.sleep(1)
        print("Job-stopped.")
        return build.building
    else:
        print("The build is alredy finished.")


def job_action(job_name, action_job):
    if action_job == "build":
        if job_name and server.get_job(job_name):
            build(job_name)
        else:
            print("Add valid job_name.(-n)")
            return "None"

    elif action_job == "stop":
        if (
            job_name
            and server.get_job(job_name)
            and server.get_job(job_name).get_last_build()
        ):
            stop_build(job_name)
        else:
            print("Add valid job_name.(-n)")
            return "None"

    else:
        print("Invalid action for job.")
        return "None"


job_name = args.job_name
action_job = args.action_job
status = serverstatus()
if action_job:
    if status == "up":
        job_action(job_name, action_job)
    else:
        print("Server is down, wait to start Jenkins server...")
        startserver()
        status = serverstatus()
        while status == "down":
            time.sleep(1)
            status = serverstatus()
        job_action(job_name, action_job)
