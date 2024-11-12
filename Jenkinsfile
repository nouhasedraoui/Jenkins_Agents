pipeline {
    agent none

    stages {
         stage('GIT') {
            agent { label 'master' }  // Specify an agent (master or any other node you have)
            steps {
                git branch: 'main', url: 'https://github.com/nouhasedraoui/Jenkins_Agents.git'
            }
        }
        }
       /* stage('Build Java Project') {
            agent { label 'Slave02' } // Kali agent
            steps {
                script {
                    
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
