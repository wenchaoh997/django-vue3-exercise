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
          <el-button @click="loginHandle('form')">Login</el-button>
          <el-button type="primary" @click="registerHandle">Signup</el-button>
          <el-button type="warning" @click="resetHandle">Reset</el-button>
        </el-form-item>
      </el-form>
    </el-row>
  </div>
</template>

<script>
import { ElNotification } from 'element-plus'
import api from "~/api/backend/Account"

export default {
  data() {
    return {
      form: {
        UserName: "",
        Password: "",
      },
      rules: {
        UserName: [
          { required: true, message: "Username can not be empty.", trigger: "blur" }
        ],
        Password: [
          { required: true, message: "Password can not be empty.", trigger: "blur" }
        ]
      },
    }
  },
  methods: {
    loginHandle(FormName) {
      this.$refs[FormName].validate((valid) => {
        if (valid) {
          const response = api.login(this.form);
          response.then((value) => {
            this.$cookies.set("jwt", value.data.token);
            this.$router.push("/dashboard");
            ElNotification({
                title: 'Success',
                message: value.data.message,
                type: 'success'
              });
          }).catch((error) => {
              ElNotification({
                title: 'Error',
                message: error.response.data.message,
                type: 'error'
              });
            })
        }
      })
    },
    registerHandle() {
      this.$router.push("/register")
    },
    resetHandle() {
      this.form.UserName = ""
      this.form.Password = ""
    }
  }
}
</script>

<style></style>