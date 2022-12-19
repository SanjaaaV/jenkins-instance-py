node('agent1') {
    stage("checkout") {
        checkout scm 
    }


    stage('junit'){
        junit 'target/*/*.xml'
    }

    stage('finish'){
        def response = httpRequest acceptType: 'APPLICATION_JSON', consoleLogResponseBody: true, contentType: 'APPLICATION_JSON', httpMode: 'POST', requestBody: '{"result":"Build job - SUCCESS - jenkinsadmin."}', responseHandle: 'NONE', url: 'http://192.168.10.200:3539/jenkins', validResponseCodes: '200', wrapAsMultipart: false  
    }

}
