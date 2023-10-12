import axios from "./index"
import Account from "./index"

// 
export const login = (params) => {
    return axios.post(
        url="/accounts/login",
        data=params,
    )
};