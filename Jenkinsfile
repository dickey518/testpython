pipeline {
    agent any
    parameters{
       choice(name: 'name', choices: ['zhangsan','lisi','wangwu'],description: 'yigecanshu')   
    }
    stages {
        stage('Hello') {
                when { params name: 'name',value: 'zhangsan' }
            steps{
            echo "hello zhangsan"
            }
            steps{
             echo "hello world"   
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
