pipeline {
    agent any
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
                sh "python3 test.py"
            }
        }
        stage('Deliver') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                withCredentials([
                    usernamePassword(credentials: 'docker-hub', usernameVariable: USER, passwordVariable: PASS)
                ]) {
                    sh "docker login -u ${USER} -p ${PASS}"
                }
                sh "docker push jmrobinson/site-testpipe"
            }
        }
    }
}
