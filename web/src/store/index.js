import Vue from "vue";
import Vuex from "vuex";
import sp from "../assets/sp.json";
import db from "../assets/db.json";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    sp: [],
    deck: [],
    db: {},
  },
  mutations: {
    setSpData(state, arr) {
      state.sp = arr;
    },
    setCardData(state, arr) {
      state.db = arr;
    },
    findCard(state, id) {
      for (let key in state.db) {
        if (state.db[key]["id"] == id) {
          state.deck.push(state.db[key]);
        }
      }
    },
    clearDeck(state) {
      state.deck = [];
    },
  },
  actions: {
    getDeckList(context, args) {
      context.commit("clearDeck");
      args.forEach((element) => {
        context.commit("findCard", Number(element));
      });
    },
    getCardData(context) {
      context.commit("setCardData", db);
    },

    getSpData(context) {
      context.commit("setSpData", sp);
    },
  },
  getters: {
    sp: (state) => {
      return state.sp;
    },
    deck: (state) => {
      return state.deck;
    },
  },
});
