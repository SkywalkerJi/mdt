import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Convert from "../views/Convert.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Secret Pack",
    component: Home,
  },
  {
    path: "/convert",
    name: "Convert",
    component: Convert,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
