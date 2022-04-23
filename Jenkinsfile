pipeline {
    agent any
    parameters{
       choice(name: 'myname', choices: ['zhangsan','lisi','wangwu'],description: 'yigecanshu')   
    }
    stages {
        stage('Hello') {
            steps{
                if("${params.myname}" == "zhangsan"){
            echo "hello zhangsan"
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
