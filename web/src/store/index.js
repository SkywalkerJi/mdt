import Vue from "vue";
import Vuex from "vuex";
// import axios from "axios";
import sp from "../assets/sp.json";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    sp: [],
  },
  mutations: {
    setSpData(state, arr) {
      state.sp = arr;
    },
  },
  actions: {
    // getSpData(context) {
    //   axios.get("./server/sp.json").then(({ data }) => {
    //     context.commit("setSpData", data);
    //   });
    // },
    getSpData(context) {
        context.commit("setSpData", sp);
      },
  },
  getters: {
    sp: (state) => {
      return state.sp;
    },
  },
});
