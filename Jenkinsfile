pipeline {
    environment {
        registry = "jmrobinsn/myflasksite"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
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
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
