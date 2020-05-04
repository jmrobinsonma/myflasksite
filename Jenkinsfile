pipeline {
    environment {
        registry = "jmrobinsn/myflasksite"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
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


#####################################################################################
                        PARAMETERS

agent any
parameters {
    choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: '')
    booleanParam(name: 'executeTests', defaultValue: true, description: '')
}

stages {
    stage() {
        when {
            expression {
                params.executeTests
            }
        }
        steps {
            echo "testing ${VERSION}"
        }
    }
}

###################################################################################
                        CREDENTIALS

agent any
    environment {
        SERVER_CREDENTIALS = credentials('dockerhub-creds')
    }
stages {
    stage {
        step {
            echo "deploy with ${SERVER_CREDENTIALS}"
        }
    }
}



steps {
    withCredentials([
        usernamePassword(credentials: 'docker-hub', usernameVariable: USER, passwordVariable: PASS)
    ]) {
        sh "deploy with ${USER} ${PASS}"
    }
}
