pipeline {
  agent {
    kubernetes {
      yamlFile 'agent.yaml'
    }
  }
  stages {
    stage('Docker Build') {
      steps {
	container('sonar') {
        	sh "sonar-scanner   -Dsonar.projectKey=CICD-COURSE  -Dsonar.sources=."
	}
      }
    }
}
}
