<template>
  <div class="login-demo">
    <el-row type="flex" justify="center">
      <el-form ref="form" :rules="rules" :model="form" label-width="100px">
        <h3>Login</h3>
        <el-form-item prop="UserName" label="Name">
          <el-input placeholder="Please input user name" v-model="form.UserName"></el-input>
        </el-form-item>
        <el-form-item prop="Password" label="Password">
          <el-input placeholder="Please input password" v-model="form.Password" show-password></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="LoginHandle('form')">Login</el-button>
          <el-button type="primary" @click="SignupHandle">Signup</el-button>
          <el-button type="warning" @click="ResetHandle">Reset</el-button>
        </el-form-item>
      </el-form>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        UserName: "",
        Password: "",
      },
      rules:{
        UserName:[
          {required: true, message: "Username can not be empty.", trigger: "blur"}
        ],
        Password:[
          {required: true, message: "Password can not be empty.", trigger: "blur"}
        ]
      },
      dialogDisabled: true
    }
  },
  methods: {
    LoginHandle(FormName) {
      this.$refs[FormName].validate((valid) => {
        if (valid){
          this.$router.push("/main")
          console.log(this.form.UserName, this.form.Password);
        }
        else{
          this.dialogDisabled = false
        }
      })
    },
    SignupHandle(){
      this.$router.push("/main")
    },
    ResetHandle(){
      this.form.UserName = ""
      this.form.Password = ""
    }
  }
}
</script>

<style></style>