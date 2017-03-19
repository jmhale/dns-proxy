#!groovy
pipeline {
  stages {
    stage('Start DNS Instance') {
      node {
        checkout scm
        sh "echo 'Starting DNS instance'"
      }
    }

    stage('Re-associate Floating IP') {
      node() {
        sh "echo 'Re-associating floating IP'"
      }
    }

    stage('Terminate DNS Instance') {
      node() {
        sh "echo 'Terminating DNS instance'"
      }
    }
  }
  post {
    always {
      deleteDir()
    }
  }
}
