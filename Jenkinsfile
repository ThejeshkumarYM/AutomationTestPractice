pipeline {
    agent any

    environment {
        BUILD_TIMESTAMP = new Date().format("yyyy-MM-dd_HH-mm-ss")
    }

    stages {
        stage('📥 Clone Project from GitHub') {
            steps {
                git url: 'https://github.com/ThejeshkumarYM/AutomationTestPractice.git', branch: 'master'
            }
        }

        stage('🐍 Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('✅ Run Pytest Automation Scripts') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest testcases/ --maxfail=1 --disable-warnings -s -v --capture=tee-sys --html=reports/%BUILD_TIMESTAMP%.html
                '''
            }
        }
    }

    post {
        always {
            echo '📊 Publishing HTML Report...'
            publishHTML([
                reportDir: 'reports',
                reportFiles: '*.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                allowMissing: false,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}