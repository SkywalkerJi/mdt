<template>
  <div class="Convert">
    <v-container>
      <v-textarea
        filled
        name="ygopro-input"
        label="YGOPRO配置代码"
        auto-grow
        clearable
        row-height="15"
        v-model="ydkText"
      ></v-textarea>
      <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
        style="opacity: 0.9"
        :footer-props="{ 'items-per-page-options': [40, 55, 60, 75, -1] }"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-btn
              class="ma-2"
              :loading="loading"
              :disabled="loading"
              color="info"
              @click="loader = 'loading'"
            >
              转换
              <template v-slot:loader>
                <span class="custom-loader">
                  <v-icon light>mdi-cached</v-icon>
                </span>
              </template>
            </v-btn>
            <v-spacer></v-spacer>
            <v-switch
              v-model="copyText"
              label="复制日文名"
              class="mt-2"
            ></v-switch>
          </v-toolbar>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loader: null,
      loading: false,
      copyText: false,
      ydkText: "",
      headers: [
        { text: "英文名", value: "en_name" },
        { text: "日文名", value: "jp_name" },
        { text: "中文名", value: "cn_name" },
        { text: "数量", value: "num" },
      ],
      desserts: [
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 59911557,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 59911553,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 59911552,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 59911551,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 59911523,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 599115233,
          cid: 10979,
        },
        {
          cn_name: "隆隆隆咕噜",
          en_name: "Gogogo Goram",
          jp_name: "ゴゴゴゴラム",
          num: 1,
          id: 599115123,
          cid: 10979,
        },
      ],
    };
  },
  methods:{
    async setCardList(){

    },
  },
  watch: {
    loader() {
      //let deck=this.ydkText.split("\n");
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    },
  },
};
</script>
<style>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>