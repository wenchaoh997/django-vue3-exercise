<template>
  <el-form :rules="rules" :model="form" label-width="120px">
    <h3>create new book</h3>
    <el-form-item prop="title" label="Title">
      <el-input v-model="form.title" placeholder="Please input title" />
    </el-form-item>
    <el-form-item prop="author" label="Author">
      <el-input v-model="form.author" placeholder="Please input author" />
    </el-form-item>
    <el-form-item prop="summary" label="Summary">
      <el-input v-model="form.summary" placeholder="Please input summary" />
    </el-form-item>
    <el-form-item prop="isbn" label="ISBN">
      <el-input v-model="form.isbn" placeholder="Please input isbn" />
    </el-form-item>
    <el-form-item prop="genre" label="Genre">
      <el-input v-model="form.genre" placeholder="Please input genre" />
    </el-form-item>
    <el-form-item>
      <el-button @click="submitHandle('form')">Submit</el-button>
      <el-button type="warning" @click="resetHandle">Reset All</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        title: "",
        author: "",
        summary: "",
        isbn: "",
        genre: "",
      },
      rules: {
        title: [],
        author: [],
        summary: [],
        isbn: [],
        genre: [],
      },
    }
  },
  methods: {
    submitHandle(FormName) {
      this.$refs[FormName].validate((valid) => {
        if (valid) {
          console.log(this.form);
        }
      })
    },
    resetHandle() {
      this.form.title = ""
      this.form.author = ""
      this.form.summary = ""
      this.form.isbn = ""
      this.form.genre = ""
    }
  },
}
</script>