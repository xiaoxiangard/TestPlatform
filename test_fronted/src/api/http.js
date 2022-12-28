//导入axios
import axios from 'axios'

//创建axios实例
var instance = axios.create({
    //请求头
    headers: {
      'Content-Type': 'application/json'
    },
    //超时时间
    timeout: 2500,
    //基础URL，接口服务地址
    baseURL: 'http://127.0.0.1:5000'
})

export default instance