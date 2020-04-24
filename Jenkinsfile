pipeline {
    agent {
        dockerfile { filename 'Dockerfile'
        }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {

                sh 'python3 test.py'
            }
        }
        stage('Push Docker') {
            steps {
                sh 'docker push jmrobinson/myflasksite'
                }
            }
        }
    }
