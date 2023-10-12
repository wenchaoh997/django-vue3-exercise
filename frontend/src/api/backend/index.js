import axios from "axios";

// Base domain and base url
const BASE_DOMAIN = "http://0.0.0.0:8000/";

export default axios.create({ 
    baseURL: BASE_DOMAIN,
    timeout: 3000,
 });