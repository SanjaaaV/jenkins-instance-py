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
         success {
            addGitlabMRComment comment: 'Test'
        }
    }
    

}


