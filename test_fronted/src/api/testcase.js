//导入配置好的axios实例
import axios from './http'

const testcase = {
   //获取用例信息
   getTestcase(params){
     return axios({
        method: "GET",
        url: "/testcase",
        //get 请求需要通过 url 拼接请求参数
        params: params
     })
   },
   //添加用例
   addTestcase(data){
    return axios({
       method: "POST",
       url: "/testcase",
       //传递请求体，要是用 data
       data: data
    })
  },
  //删除用例
  deleteTestcase(data){
    return axios({
       method: "DELETE",
       url: "/testcase",
       //传递请求体，要是用 data
       data: data
    })
  }, 
  //修改用例
  updateTestcase(data){
    return axios({
       method: "PUT",
       url: "/testcase",
       //传递请求体，要是用 data
       data: data
    })
  }
}

//导出
export default testcase