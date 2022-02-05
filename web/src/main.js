import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import i18n from "./i18n";
import store from "./store";
import VueClipboard from "vue-clipboard2";

Vue.config.productionTip = false;

Vue.use(VueClipboard);

new Vue({
  vuetify,
  router,
  i18n,
  store,
  render: (h) => h(App),
}).$mount("#app");
