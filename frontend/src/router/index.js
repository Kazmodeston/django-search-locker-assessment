import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/home.vue";
import Rent from "../components/rent.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/rent",
    name: "Rent",
    component: Rent,
  },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;