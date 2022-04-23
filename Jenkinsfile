pipeline {
    agent any
    parameters{
       choice(name: 'myname', choices: ['zhangsan','lisi','wangwu'],description: 'yigecanshu')   
    }
    stages {
        stage('Hello zhangsan') {
            when {equals expected: 'zhangsan',actual: "${params.myname}"}
            steps{
             echo "hello zhangsan"   
            }
        }
        stage('Hello lisi') {
            when {equals expected: 'lisi',actual: "${params.myname}"}
            steps{
             echo "hello lisi"   
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
