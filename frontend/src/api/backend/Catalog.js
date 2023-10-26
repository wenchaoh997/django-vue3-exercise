import axios from "./index"

export default {
    get_bookList(params) {
        return axios.get("/catalog/bool_list", params);
    },
}