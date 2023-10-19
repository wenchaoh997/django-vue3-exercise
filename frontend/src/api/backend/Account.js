import axios from "./index"

export default {
    login(params){
        return axios.post("/accounts/login", params);
    }, 
    register(params){
        return axios.post("/accounts/register", params);
    },
    verification(params){
        return axios.post("/accounts/login_verification", params)
    },
}