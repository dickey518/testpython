pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                if("${name}" == "zhangsan"){
                echo 'Hello zhangsan'
                }else{
                echo "hello world"   
                }
            }
        }
        stage('get'){
            steps{
                echo 'get something'
            }
            
        }
        stage('just'){
            steps{
                echo 'get just'
            }
            
        }
    }
}
