import request from "../utils/request"

export const uploadPicture = () => request({
  url: '/image/upload',
  method:'post',
})