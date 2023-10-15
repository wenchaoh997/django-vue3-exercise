<template>
  <div class="register-demo">
    <el-row type="flex" justify="center">
      <el-form ref="form" :rules="rules" :model="form" label-width="100px">
        <h3>Register</h3>
        <el-form-item prop="email" label="Name">
          <el-input placeholder="Please input user name" v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="Password">
          <el-input placeholder="Please input password" v-model="form.password" show-password></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="registerHandle('form')">Signup</el-button>
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
        email: "",
        password: "",
      },
      rules: {
        email: [
          { required: true, message: "Username can not be empty.", trigger: "blur" }
        ],
        password: [
          { required: true, message: "Password can not be empty.", trigger: "blur" }
        ]
      },
    }
  },
  methods: {
    registerHandle(FormName) {
      this.$refs[FormName].validate((valid) => {
        if (valid) {
          const response = api.register(this.form);
          response.then((value) => {
            this.$router.push("/login");
            ElNotification({
              title: 'Success',
              message: 'Now turn to the login page.',
              type: 'success'
            });
          }).catch((error) => {
            ElNotification({
              title: 'Error',
              type: 'error'
            });
          })
        }
      })
    },
    resetHandle() {
      this.form.email = ""
      this.form.password = ""
    }
  }
}
</script>