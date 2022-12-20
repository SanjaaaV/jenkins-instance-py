pipeline {
    agent {
        label 'agent1'
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
            updateGitlabCommitStatus name: 'build', state: 'failure' 
        }
         success {
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
    }

}


