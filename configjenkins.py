from configparser import ConfigParser

config = ConfigParser()

config["JENKINS"] = {
    "hostJenkins": "http://192.168.10.200:8082/",
    "usernameJenkins": "svukelic",
    "passwordJenkins": "1148d3b78430eb28c6060cecab43236008",
    "url_projects": "http://192.168.10.200:8082/api/v4/users/svukelic/projects",
}

with open("parametersjenkins.ini", "w") as f:
    config.write(f)
