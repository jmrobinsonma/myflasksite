pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
}
    stages {
        stage('Test') {
            agent {
                dockerfile {
                    filename 'testing.Dockerfile'
}
}
            steps {
                sh "which python3"
}
}
        stage('Deliver') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
}
}
            steps {
                script {
                    docker.withRegistry('','dockerhub')
                        sh "docker push jmrobinson/myflasksite"
}
}
}
}
}
