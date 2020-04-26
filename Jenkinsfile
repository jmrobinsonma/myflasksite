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
}
stage('Deliver') {
agent {
dockerfile {
filename 'Dockerfile'
}
}
steps {
sh "docker push jmrobinson/myflasksite"
}
}
}
}

