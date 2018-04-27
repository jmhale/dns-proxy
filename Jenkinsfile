pipeline {
    // Reminder: Job isn't pulling this automatically yet. Need to paste it into the pipeline
    // config, so I'm not checking in every little change while I mess around.
    agent any

    environment {
      DO_TOKEN = credentials('DigitalOcean API Key')
    }

    parameters {
      choice(choices: 'nyc1\nnyc3', description: 'Which region to recycle?', name: 'region')
    }

    stages {
        stage('Check out code') {
            steps {
                if (!fileExists ('bin/activate')) {
                    sh 'virtualenv --no-site-packages .'
                }
                git url: 'https://github.com/jmhale/dns-proxy'
                sh '''
                    source bin/activate
                    pip install -r requirements.txt
                    deactivate
                   '''
            }
        }
        stage('Start Replacement DNS Instance') {
            environment {
              IP = credentials("${params.region}_ip") //This doesn't work.
            }
            steps {
                echo "Building..${params.region}"
                echo "Using IP: ${IP}"
            }
        }
        stage('Move Floating IP Address') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Terminate Old DNS Instance') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
