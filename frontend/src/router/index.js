import { createRouter, createWebHistory } from "vue-router"

const routes = [
    { path: "/", redirect: "/dashboard" },
    { path: "/login", component: ()=>import("~/pages/auth/Login.vue") },
    { path: "/register", component: ()=>import("~/pages/auth/Register.vue") },
    { path: "/dashboard", component: ()=>import("~/pages/Dashboard.vue") },
    { path: "/feedback", component: ()=>import("~/pages/Feedback.vue") },
    { path: "/booklist", component: ()=>import("~/pages/BookList.vue") },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router