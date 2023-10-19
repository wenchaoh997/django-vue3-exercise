<template>
    <h3>dashboard</h3>
</template>

<script lang="js">
import api from "~/api/backend/Account"

export default {
    created() {
        const response = api.verification({"jwt": this.$cookies.get("jwt")});
        response.then((value) => {
            if (value.data.message === "None"){
                this.$router.push("/login")
            }
        })
    },
}
</script>