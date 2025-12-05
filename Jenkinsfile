stage('Test + Agentic AI Decision') {
    steps {
        script {
            // Simulate test failure
            def status = bat(script: 'exit /b 1', returnStatus: true)

            if (status != 0) {

                // Write dummy error log
                writeFile file: 'error.log',
                          text: 'Connection refused from database service on port 5432'

                // Read file in Windows
                def logs = bat(
                    script: 'type error.log',
                    returnStdout: true
                ).trim()

                // Call AI agent
                def decision = bat(
                    script: "venv\\Scripts\\python agent\\agent.py \"${logs}\"",
                    returnStdout: true
                ).trim()

                echo "🤖 AI DECISION: ${decision}"

                if (decision.contains("RETRY")) {
                    echo "AI suggested: Retry"
                }
                else if (decision.contains("RESTART")) {
                    echo "AI suggested: Restart service"
                }
                else if (decision.contains("NOTIFY")) {
                    echo "AI suggested: Human intervention"
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
