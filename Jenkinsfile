pipeline {
    agent 'agent1'
    stages {
        stage('Test') {
            steps {
                sh 'python3 unitjenkins.py'
            }
        }
    }

    post ('finish'){
            failure {

                gitlabCommitStatus(connection: gitLabConnection(gitLabConnection: 'jenadmin', jobCredentialId: '')) {
                   state: ‘failed’
                } 

            }

            success {

                gitlabCommitStatus(connection: gitLabConnection(gitLabConnection: 'jenadmin', jobCredentialId: '')) {
                    state: ‘success’
                }

            }
    }

}


