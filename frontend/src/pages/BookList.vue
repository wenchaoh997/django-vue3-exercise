<template>
    <el-row style="padding: 2%;">Books</el-row>
    <el-table :data="bookData.books" style="display: table-cell!important;">
        <el-table-column fixed prop="isbn" label="ISBN" width="150" />
        <el-table-column prop="title" label="Title" width="120" />
        <el-table-column fixed="right" label="Operations" width="120">
            <template #default>
                <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
                <el-button link type="primary" size="small">Edit</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination background layout="prev, pager, next" :total="totalPage * 10" v-model="currPage" />
    <el-backtop :right="100" :bottom="100" />

    <el-button @click="checkHandle()">check</el-button>
</template>

<script>
import acountApi from "~/api/backend/Account"
import bookApi from "~/api/backend/Catalog"

export default {
    created() {
        const response = acountApi.verification({ "jwt": this.$cookies.get("jwt") });
        response.then((value) => {
            if (value.data.message === "None") {
                this.$router.push("/login")
            }
            else {
                const res = bookApi.get_bookList({ "jwt": this.$cookies.get("jwt") });
                res.then((vv) => {
                    console.log(vv.data);
                    this.bookData = vv.data;
                })
            }
        })
    },
    data() {
        return {
            currPage: 1,
            totalPage: 10,
            bookData: [],
            tableData: [],
        }
    },
    methods: {
        handleClick() {
            console.log('click')
        },
        checkHandle(){
            console.log(this.bookData);
        }
    }
}
</script>