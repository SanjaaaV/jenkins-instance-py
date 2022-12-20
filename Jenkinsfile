pipeline {
    agent {
        label 'agent1'
    }

    post {
        success {
            updateGitlabCommitStatus name: 'Test', state: 'success' 
        }
        failure {
            updateGitlabCommitStatus name: 'Test', state: 'failed'
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


