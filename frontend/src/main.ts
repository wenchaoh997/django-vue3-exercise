import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index"
import api from "./api/backend/index"
import VueCookies from 'vue-cookies'

// import "~/styles/element/index.scss";

import ElementPlus from "element-plus";
// import all element css, uncommented next line
import "element-plus/dist/index.css";

// or use cdn, uncomment cdn link in `index.html`

import "~/styles/index.scss";
import "uno.css";

// Import .scss before using feedback components
import "element-plus/theme-chalk/src/message.scss";
import "element-plus/theme-chalk/src/notification.scss";

const app = createApp(App);
app.use(ElementPlus);
app.use(router);
app.use(VueCookies, { expires: "1d" });
app.provide('$http', api);
app.mount("#app");
