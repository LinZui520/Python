import { defineStore } from "pinia";

export const useUserStore = defineStore({
  id: 'users',
  state: () => ({
    userName:'Account',
    email:'',
    passWord:'',
  }),

  actions: {

  }
})