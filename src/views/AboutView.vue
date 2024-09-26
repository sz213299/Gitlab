<template>
    <el-button type="primary" @click="handleligin">测试登录</el-button>
    <el-button type="success" @click="handUserList">测试获取用户信息</el-button>
  
</template>

<script  setup>
import requsetUtil from '@/util/request'
// 处理登录
const handleligin=async() =>{
  // await 处理请求
let result = await requsetUtil.get("user/jwt")
let data = result.data;
if (data.code ==200){
  const token=data.token;
  console.log('登录成功,tokeb='+token)
  // 把token存进去
  window.sessionStorage.setItem('token',token)
}else{
  console.log("登录出错")
}
}
const handUserList=async()=>{
  let result =await requsetUtil.get("user/test")
  let data =result.data;
  if (data.code ==200){
    const userList=data.data
    console.log('用户信息列表，userlist='+userList)
  }else{
    console.log("登录出错")
  }
}

</script>
