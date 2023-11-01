<template>
    <el-row style="padding: 2%;">Books</el-row>
    <el-table :data="bookData.books" style="display: table-cell!important;">
        <el-table-column fixed prop="isbn" label="ISBN" width="150" />
        <el-table-column prop="title" label="Title" width="120" />
        <el-table-column fixed="right" label="Operations" width="120">
            <template #="scope">
                <el-button link type="primary" size="small" @click="detailHandle(scope.row)">Detail</el-button>
                <el-button link type="primary" size="small" @click="editHandle(scope.row)">Edit</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination background layout="prev, pager, next" :total="totalPage * 10" v-model="currPage" />
    <el-backtop :right="100" :bottom="100" />

    <el-button @click="checkHandle()">check</el-button>
    <el-button @click="newHandle()">New</el-button>
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
                    this.bookData = vv.data;
                })
            }
        })
    },
    data() {
        return {
            scope: undefined,
            currPage: 1,
            totalPage: 1,
            bookData: [],
            tableData: [],
        }
    },
    methods: {
        detailHandle(row) {
            console.log(row);
        },
        editHandle(row){
            console.log(row);

        },
        checkHandle(){
            console.log(this.bookData);
        },
        newHandle(){
            this.$router.push("/newBook");
        }
    }
}
</script>