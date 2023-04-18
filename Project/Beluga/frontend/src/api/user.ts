import request from "../utils/request"



export const addUser = (userName:string,email:string,passWord:string) => request({
  url: '/user/add',
  method:'post',
  data:{
    userName: userName,
    passWord: passWord,
    email: email
  }
})

export const updateUser = (userName:string,email:string,passWord:string) => request({
  url:'/user/update',
  method:'put',
  data:{
    userName: userName,
    passWord: passWord,
    email: email
  }
})

export const getUser = (userName:string) => request({
  url:'/user/get/'+userName,
  method:'get',
})

