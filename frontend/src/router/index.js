import { createRouter, createWebHistory } from "vue-router"

const routes = [
    { path: "/", redirect: "/login" },
    { path: "/login", component: ()=>import("~/pages/Login.vue") },
    { path: "/register", component: ()=>import("~/pages/Register.vue") },
    { path: "/main", component: ()=>import("~/pages/Main.vue") },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router