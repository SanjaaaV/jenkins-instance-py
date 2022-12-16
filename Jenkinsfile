node('agent1') {
    stage("checkout") {
        checkout scm 
    }

    stage('junit'){
        junit 'target/*/*.xml'
    }
}
