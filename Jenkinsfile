pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages {

        stage('Checkout') {
            steps { 
                checkout scm 
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r agent\\requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat 'echo BUILD SUCCESS'
            }
        }

        stage('Test + Agentic AI Decision') {
            steps {
                script {

                    // Simulate failure
                    def status = bat(script: "echo Simulating failure & exit /b 1", returnStatus: true)

                    if (status != 0) {

                        writeFile file: 'error.log',
                                  text: 'Connection refused from database service on port 5432'

                        def logs = bat(
                            script: 'type error.log',
                            returnStdout: true
                        ).trim()

                        def decision = bat(
                            script: "venv\\Scripts\\python agent\\agent.py \"${logs}\"",
                            returnStdout: true
                        ).trim()

                        echo "🤖 AI DECISION: ${decision}"

                        if (decision == "RETRY") {
                            bat "echo AI suggested: Retry test"
                        }
                        else if (decision == "RESTART_SERVICE") {
                            bat "echo AI suggested: Restarting service"
                        }
                        else if (decision == "NOTIFY") {
                            bat "echo AI suggested: Human intervention required"
                        }
                        else {
                            error "Pipeline stopped by AI decision: ${decision}"
                        }

                    } else {
                        bat "echo Tests passed successfully"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Deploying application...'
            }
        }
    }
}
