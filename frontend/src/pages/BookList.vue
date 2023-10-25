<template>
    <el-row style="padding: 2%;">Books</el-row>
    <el-table :data="tableData" style="display: table-cell!important;">
        <el-table-column fixed prop="date" label="Date" width="150" />
        <el-table-column prop="name" label="Name" width="120" />
        <el-table-column prop="state" label="State" width="120" />
        <el-table-column prop="city" label="City" width="120" />
        <el-table-column prop="address" label="Address" width="200" />
        <el-table-column prop="zip" label="Zip" width="120" />
        <el-table-column fixed="right" label="Operations" width="120">
            <template #default>
                <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
                <el-button link type="primary" size="small">Edit</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-pagination background layout="prev, pager, next" :total="totalPage*10" v-model="currPage" />
    <el-backtop :right="100" :bottom="100" />
</template>

<script>
import api from "~/api/backend/Account"

export default {
    created() {
        const response = api.verification({ "jwt": this.$cookies.get("jwt") });
        response.then((value) => {
            if (value.data.message === "None") {
                this.$router.push("/login")
            }
            else{
                
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
        }
    }
}
</script>