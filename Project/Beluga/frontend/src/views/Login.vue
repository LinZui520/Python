<script setup lang="ts">
  import { ref } from 'vue'
  import { getUser } from '../api/user'
  import { useUserStore } from '../store/modules/user'
  import { useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus'

  const userName = ref('')
  const passWord = ref('')

  const userStore = useUserStore()

  const router = useRouter()
  
 


  
  const login = () => {
    if(userName.value&&passWord.value){
      getUser(userName.value).then(res => {
        if(res.data.length!=0){
          if(res.data.passWord==passWord.value){
            userStore.userName=res.data.userName
            userStore.email=res.data.email
            userStore.passWord=res.data.passWord
            ElMessage({
              message: '登录成功',
              type: 'success',
            })
            router.push({ name: 'account', params: { userName: userStore.userName  }})
          }
          else{
            ElMessage({
              message: '账号或密码错误',
              type: 'warning',
            })
          }
        }
        else{
          ElMessage({
            message: '账号不存在',
            type: 'warning',
          })
        }
      }).catch(err => {
        console.log(err)
        ElMessage({
          message: '服务器繁忙',
          type: 'warning',
        })
      })
    }
    else{
      ElMessage({
        message: '信息不完整',
        type: 'warning',
      })
    }
  }


</script>

<template>
  <section>
    <div class="form-box">
      <form action="">
        <h2>Login</h2>
        <div class="inputbox">
          <input type="text" v-model="userName" required>
          <label for="">用户名</label>
        </div>
        <div class="inputbox">
          <input type="password" v-model="passWord" required>
          <label for="">密码</label>
        </div>
        <div class="forget">
          <label for=""><input type="checkbox">记住我</label>
          <a href="">忘记密码</a>
        </div>
        <button type="button" @click="login">登录</button>
        <div class="register">
          <p>没有账号？<a href="/register">注册</a></p>
        </div>
      </form>
    </div>
  </section>
</template>


<style scoped>
section{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
    
  background: url('../assets/images/background.jpg')no-repeat;
  background-position: center;
  background-size: cover;
}
.form-box{
  position: relative;
  width: 400px;
  height: 450px;
  background: transparent;
  border: 2px solid rgba(255,255,255,0.5);
  border-radius: 20px;
  backdrop-filter: blur(15px);
  display: flex;
  justify-content: center;
  align-items: center;
}
h2{
  font-size: 2em;
  color: #fff;
  text-align: center;
}
.inputbox{
  position: relative;
  margin: 30px 0;
  width: 310px;
  border-bottom: 2px solid #fff;
}
.inputbox label{
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  color: #fff;
  font-size: 1em;
  pointer-events: none;
  transition: .5s;
}
input:focus ~ label,
input:valid ~ label{
  top: -5px;
}
.inputbox input {
  width: 100%;
  height: 50px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1em;
  padding:0 35px 0 5px;
  color: #fff;
}
/* .inputbox {
  position: absolute;
  right: 8px;
  color: #fff;
  font-size: 1.2em;
  top: 20px;
} */
.forget{
  margin: -15px 0 15px ;
  font-size: .9em;
  color: #fff;
  display: flex;
  justify-content: space-between;  
}

.forget label input{
  margin-right: 3px; 
}
.forget a{
  color: #fff;
  text-decoration: none;
}
.forget a:hover{
  text-decoration: underline;
}
button{
  width: 100%;
  height: 40px;
  border-radius: 40px;
  background: #fff;
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 1em;
  font-weight: 600;
}
button:hover{
  background-color: #f0f0f0;
}
button:active{
  transform: scale(0.991);
  box-shadow: 3px 2px 22px 1px rgba(0, 0, 0, 0.20);
}
.register{
    font-size: .9em;
    color: #fff;
    text-align: center;
    margin: 25px 0 10px;
}
.register p a{
  text-decoration: none;
  color: #fff;
  font-weight: 600;
}
.register p a:hover{
  text-decoration: underline;
}
</style>