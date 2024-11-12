pipeline {
    agent none

    stages {
       /* stage('Build Java Project') {
            agent { label 'Slave02' } // Kali agent
            steps {
                script {
                    // Ensure Maven is installed on the Kali agent for Java build
                    echo "Building Java project on Kali agent"
                    dir('Java_Project/demo') {
                        sh 'mvn clean package'
                    }
                }
            }
        }
*/
        stage('Build Python Project') {
            agent { label 'Slave01' } // Windows agent
            steps {
                script {
                    // Ensure Python is installed on the Windows agent for Python build
                    echo "Building Python project on Windows agent"
                    dir('Python_Project') {
                        bat 'python main.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
