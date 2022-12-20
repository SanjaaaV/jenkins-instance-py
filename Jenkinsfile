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
            gitlabCommitStatus {
                name = 'Test',
                state = 'failed' 
            }
        }
         success {
            gitlabCommitStatus {
                name = 'Test', 
                state = 'success'
            }
        }
    }
    

}


