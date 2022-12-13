
import docker
import jenkins
import sys
import requests
from docker.api import container

#Docker
client = docker.from_env()
container = client.containers.get('9ae6f859ec58')

#Jenkins api
host = "http://192.168.10.200:8082/"
usernameJenkins = "svukelic"
passwordJenkins = "1148d3b78430eb28c6060cecab43236008"
server = jenkins.Jenkins(host, username=usernameJenkins, password=passwordJenkins)
response = requests.get("http://192.168.10.200:8082/api/v4/users/svukelic/projects")
user = server.get_whoami()
version = server.get_version()
print(f'Jenkins user: {user["fullName"]} Jenkins version: {version}')
jobs = server.get_jobs()

#functions
def print_options():
    print("Options:\n"
          "status - Check the status of Jenkins server container.\n"
          "start - Start the Jenkins instance.\n"
          "stop - Stop the Jenkins instance.\n"
          "backup - To make a backup of the Jenkins instance.\n"
          "build_job - Build the job.\n"
          "stop_job - Stop the job.\n")

def print_job():
    print("\nbuild_job - Build the job.\n"
          "stop_job - Stop the job.\n"
          "exit - Exit.\n"
          "You can also run script again to stop the Jenkins instance.\n")
    print(jobs)

def job_choice():
    choice = input()
    if choice == "build_job":
        name_job = input("Name of the job to build:")
        server.build_job(name_job)
    elif choice == "stop_job":
        name_job = input("Name of the job to stop:")
        number_job = input("Number of the job to stop:")
        server.stop_build(name_job, number_job)
    elif choice == "exit":
        exit()



#main
if (len(sys.argv)>1):
    a = sys.argv[1]
    if a == "help":
        print_options()
    elif a == "status":
        print(container.status)
        if (container.status) == "running":
            print_job()
            job_choice()

    elif a == "stop":
        container.stop()
        print("Jenkins instance was stopped.")
    elif a == "start":
        container.start()
        print("Jenkins instance was started.")
        print_job()
        job_choice()

    elif a == "backup":
        nameB = input("Enter name for Jenkins backup:")
        container.commit(nameB)
        print("Jenkins instance backup was made.")
        images = client.images.list()
        for image in images:
            print(image)

    elif a == "build_job":
        print(jobs)
        name_job = input("Name of the job to build:")
        server.build_job(name_job)

    elif a == "stop_job":
        print(jobs)
        name_job = input("Name of the job to stop:")
        number_job = input("Number of the job to stop:")
        server.stop_build(name_job, number_job)

else:
    print_options()
