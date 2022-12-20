pipeline {
    agent {
        label 'agent1'
    }
    options {
        gitLabConnection('jenadmin')
    }
    triggers {
        gitlab(triggerOnPush: true, triggerOnMergeRequest: true)
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 unitjenkins.py'
            }
        }
    }


    post {
         failure {
            updateGitlabCommitStatus name: 'build', state: 'failed' 
        }
         success {
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
    }
    

}


