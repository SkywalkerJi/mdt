<template>
  <div class="Convert">
    <v-container>
      <v-textarea
        filled
        name="ygopro-input"
        label="请在此处复制粘贴 YGOPRO 配置代码"
        auto-grow
        clearable
        row-height="15"
        v-model="ydkText"
      ></v-textarea>
      <v-data-table
        :headers="headers"
        :items="deck"
        item-key="sno"
        @click:row="handleClickCard"
        :items-per-page="5"
        class="elevation-1"
        style="opacity: 1"
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
              v-model="webSearch"
              label="网页卡查"
              class="mt-2"
            ></v-switch>
          </v-toolbar>
        </template>
        <template v-slot:[`item.img`]="{ item }">
          <v-img
            max-height="100"
            max-width="70"
            :src="getCardImgUrl(item.id)"
            alt="卡图"
          >
          </v-img>
        </template>
        <template v-slot:[`item.cn_name`]="{ item }">
          <div @click="onSingleCellClick">{{ item.cn_name }}</div>
        </template>
        <template v-slot:[`item.en_name`]="{ item }">
          <div @click="onSingleCellClick">{{ item.en_name }}</div>
        </template>
        <template v-slot:[`item.jp_name`]="{ item }">
          <div @click="onSingleCellClick">{{ item.jp_name }}</div>
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
      webSearch: false,
      ydkText: "",
      headers: [
        { text: "序号", value: "sno" },
        {
          text: "卡图",
          sortable: false,
          value: "img",
        },
        { text: "英文名", value: "en_name" },
        { text: "日文名", value: "jp_name" },
        { text: "中文名", value: "cn_name" },
      ],
      deck: [],
    };
  },
  methods: {
    getDeckList() {
      let deck = this.ydkText.split("\n").filter((item) => {
        if (!isNaN(item)) return true;
      });
      this.$store.dispatch("getDeckList", deck);
      const db = this.$store.getters["deck"];
      this.deck = db.map((d, index) => ({ ...d, sno: index + 1 }));
    },
    getCardImgUrl(id) {
      return (
        "https://cdn.233.momobako.com/ygopro/pics/" +
        id.toString() +
        ".jpg!thumb2"
      );
    },
    handleClickCard(item) {
      if (this.webSearch) {
        window.open("https://ygocdb.com/?search=" + item.cid, "_blank");
      }
    },
    onSingleCellClick(e) {
      this.$copyText(e.target.outerText);
    },
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];
      setTimeout(() => (this[l] = false), 1000);
      if (this.ydkText.length > 0) {
        this.getDeckList();
      }
      this.loader = null;
    },
  },
  created() {
    this.$store.dispatch("getCardData");
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