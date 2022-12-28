//导入配置好的axios实例
import axios from './http'

const build = {
   //获取构建记录信息
   getBuild(params){
     return axios({
        method: "GET",
        url: "/build",
        //get 请求需要通过 url 拼接请求参数
        params: params
     })
   }
}

//导出
export default build