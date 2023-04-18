<script setup lang="ts">
  import { ref } from 'vue'
  import { getUser,addUser } from '../api/user';
  import { useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus'

  const userName = ref('')
  const email = ref('')
  const passWord = ref('')

  const router = useRouter()

  const register = () => {
    if(userName.value&&email.value&&passWord.value){
      getUser(userName.value).then(res =>{
        if(res.data.length==0){
          addUser(userName.value,email.value,passWord.value).then(res => {
            ElMessage({
              message: '注册成功',
              type: 'success',
            })
            router.push('login')
          }).catch(err=>{
            ElMessage({
              message: '注册失败，服务器错误',
              type: 'warning',
            })
          })
        }
        else{
          ElMessage({
            message: '账号已注册',
            type: 'warning',
          })
        }
      }).catch(err => {
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
        <h2>Register</h2>
        <div class="inputbox">
          <input type="text" v-model="userName" required>
          <label for="">用户名</label>
        </div>
        <div class="inputbox">
          <input type="text" v-model="email" required>
          <label for="">邮箱</label>
        </div>
        <div class="inputbox">
          <input type="password" v-model="passWord" required>
          <label for="">密码</label>
        </div>
        <button type="button" @click="register">注册</button>
        <div class="login">
          <p>已有账号？<a href="/login">登录</a></p>
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
.login{
    font-size: .9em;
    color: #fff;
    text-align: center;
    margin: 25px 0 10px;
}
.login p a{
  text-decoration: none;
  color: #fff;
  font-weight: 600;
}
.login p a:hover{
  text-decoration: underline;
}
</style>