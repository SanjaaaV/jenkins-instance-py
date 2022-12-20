node('agent1') {
    stage("checkout") {
        checkout scm 
    }

    stage ('Test'){
        sh 'python3 unitjenkins.py'
    }
    post ('finish'){
            failure {

                gitlabCommitStatus(connection: gitLabConnection(gitLabConnection: 'jenadmin', jobCredentialId: '')) {
                    name: ‘build’, state: ‘failed’
                } 

            }

            success {

                gitlabCommitStatus(connection: gitLabConnection(gitLabConnection: 'jenadmin', jobCredentialId: '')) {
                    name: ‘build’, state: ‘success’
                }

            }
    }



}
