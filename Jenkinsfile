node('agent1') {
    stage("checkout") {
        checkout scm 
    }

    stage ('Test'){
        sh 'python3 unitjenkins.py'
    }

}
