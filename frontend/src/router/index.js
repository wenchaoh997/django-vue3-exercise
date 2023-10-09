import { createRouter, createWebHistory } from "vue-router"

const routes = [
    { path: "/", component: ()=>import("~/pages/Login.vue") },
    { path: "/main", component: ()=>import("~/pages/Main.vue") },
    { path: "/register", component: ()=>import("~/pages/Register.vue") }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router