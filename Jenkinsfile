pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Repository loaded from GitHub'
            }
        }

        stage('List Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la app'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('app') {
                    sh '''
                        python3 --version
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('app') {
                    sh '''
                        . venv/bin/activate
                        pytest test_main.py
                    '''
                }
            }
        }

        stage('Run Lint') {
            steps {
                dir('app') {
                    sh '''
                        . venv/bin/activate
                        pylint main.py || true
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                script {
                    def dcHome = tool 'DependencyCheck'

                    dir('app') {
                        sh """
                            ${dcHome}/bin/dependency-check.sh \
                            --scan . \
                            --format HTML \
                            --out dependency-check-report
                        """
                    }
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                dir('app') {
                    sh '''
                        trivy fs --format table --output trivy-report.txt > trivy-report.txt
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'app/dependency-check-report/*, app/trivy-report.txt', fingerprint: true
            echo 'Pipeline execution finished.'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
