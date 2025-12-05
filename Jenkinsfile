pipeline {

    agent any

    stages {

        stage('Test + Agentic AI Decision') {
            steps {
                script {

                    // Simulate test failure in Windows
                    def status = bat(script: '@echo off\nexit /b 1', returnStatus: true)

                    if (status != 0) {

                        // Write dummy error log
                        writeFile file: 'error.log',
                                  text: 'Connection refused from database service on port 5432'

                        // Read error log from Windows file
                        def logs = bat(
                            script: '@echo off\ntype error.log',
                            returnStdout: true
                        ).trim()

                        echo "Error log from file: ${logs}"

                        // Call AI agent
                        def decision = bat(
                            script: '@echo off\nvenv\\Scripts\\python agent\\agent.py "' + logs + '"',
                            returnStdout: true
                        ).trim()

                        decision = decision.toUpperCase()
                        echo "🤖 AI DECISION: ${decision}"

                        if (decision.contains("RETRY")) {
                            echo "AI suggested: Retry"
                            bat 'echo Retrying tests...'
                        }
                        else if (decision.contains("RESTART")) {
                            echo "AI suggested: Restart service"
                            bat 'echo Restarting service...'
                        }
                        else if (decision.contains("NOTIFY")) {
                            echo "AI suggested: Human intervention required"
                        }
                        else {
                            error "Pipeline stopped by AI decision: ${decision}"
                        }

                    } else {
                        echo "Tests passed successfully"
                    }
                }
            }
        }

    }
}
