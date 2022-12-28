//导入配置好的axios实例
import axios from './http'

const plan = {
   //获取测试计划信息
   getPlan(params){
     return axios({
        method: "GET",
        url: "/plan",
        //get 请求需要通过 url 拼接请求参数
        params: params
     })
   },
   //添加测试计划
   addPlan(data){
    return axios({
       method: "POST",
       url: "/plan",
       //传递请求体，要是用 data
       data: data
    })
  }
}

//导出
export default plan