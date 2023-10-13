import axios from "axios";

// Base domain and base url
const BASE_DOMAIN = "http://localhost/";

export default axios.create({ 
    baseURL: BASE_DOMAIN,
    timeout: 3000,
 });