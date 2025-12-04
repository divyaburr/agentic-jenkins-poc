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
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r agent/requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "BUILD SUCCESS"'
            }
        }

        stage('Test + Agentic AI Decision') {
            steps {
                script {
                    // Simulating test failure
                    def status = sh(script: 'bash -c "exit 1"', returnStatus: true)

                    if (status != 0) {

                        // Dummy error log for demo
                        writeFile file: 'error.log',
                                  text: 'Connection refused from database service on port 5432'

                        def logs = sh(
                            script: 'cat error.log',
                            returnStdout: true
                        ).trim()

                        def decision = sh(
                            script: "./venv/bin/python agent/agent.py \"${logs}\"",
                            returnStdout: true
                        ).trim()

                        echo "🤖 AI DECISION: ${decision}"

                        if (decision == "RETRY") {
                            echo "AI suggested: Retry"
                            sh "echo Retrying tests..."
                        }
                        else if (decision == "RESTART_SERVICE") {
                            echo "AI suggested: Restart service"
                            sh "echo Restarting service..."
                        }
                        else if (decision == "NOTIFY") {
                            echo "AI suggested: Human intervention required"
                        }
                        else {
                            error "Pipeline stopped by AI decision: ${decision}"
                        }
                    }
                    else {
                        echo "Tests passed successfully"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }
}
