pipeline {
    agent {
        label 'agent1'
    }

    post {
        success {
            updateGitlabCommitStatus name: 'build', state: 'success' 
        }
        failure {
            updateGitlabCommitStatus name: 'build', state: 'failed'
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


