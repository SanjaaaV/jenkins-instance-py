pipeline {
    agent {
        label 'agent1'
    }

    post {
        success {
            updateGitlabCommitStatus name: 'jenkins', state: 'success' 
        }
        failure {
            updateGitlabCommitStatus name: 'jenkins', state: 'failed'
        }
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 unitjenkins.py'
            }
        }
    }
 

}


