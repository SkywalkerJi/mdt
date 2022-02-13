<template>
  <div class="Search">
    <v-container>
      <v-text-field
        outlined
        label="搜索卡片"
        prepend-inner-icon="mdi-magnify"
        v-model="keyWord"
        @input="searchSp"
      ></v-text-field>
      <v-data-table
        :headers="spListHeaders"
        :items="spList"
        :single-expand="false"
        :expanded.sync="expanded"
        item-key="sp_id"
        show-expand
        class="elevation-1"
        style="opacity: 0.9"
        :v-if="spList.length"
        :footer-props="{ 'items-per-page-options': [15, 30, 50, 100, -1] }"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Yu-Gi-Oh! Master Duel</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-switch
              v-model="webSearch"
              label="网页卡查"
              class="mt-2"
            ></v-switch>
          </v-toolbar>
        </template>
        <template v-slot:[`item.sp_en`]="{ item }">
          <div @click="handleClickSp">{{ item.sp_en }}</div>
        </template>
        <template v-slot:[`item.sp_jp`]="{ item }">
          <div @click="onSingleCellClick">{{ item.sp_jp }}</div>
        </template>
        <template v-slot:[`item.sp_cn`]="{ item }">
          <div @click="onSingleCellClick">{{ item.sp_cn }}</div>
        </template>
        <template v-slot:expanded-item="{ headers, item }">
          <td :colspan="headers.length">
            <v-data-table
              :headers="cardsHeaders"
              :items="item.cards"
              :item-key="item.cid"
              @click:row="handleClickCard"
              hide-default-header
              elevation="0"
              :footer-props="{ 'items-per-page-options': [5, 10, 20, -1] }"
            >
              <template v-slot:[`item.id`]="{ item }">
                <div @click="onSingleCellClick">{{ item.id }}</div>
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
              <template v-slot:[`item.cn_n`]="{ item }">
                <div @click="onSingleCellClick">{{ item.cn_n }}</div>
              </template>
              <template v-slot:[`item.en_n`]="{ item }">
                <div @click="onSingleCellClick">{{ item.en_n }}</div>
              </template>
              <template v-slot:[`item.jp_n`]="{ item }">
                <div @click="onSingleCellClick">{{ item.jp_n }}</div>
              </template>
            </v-data-table>
          </td>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
import fuse from "../mixins/fuse.vue";
export default {
  name: "Search",
  mixins: [fuse],
  data() {
    return {
      keyWord: "",
      message: "复制到剪贴板",
      expanded: [],
      webSearch: false,
      spListHeaders: [
        {
          text: "序号",
          align: "start",
          sortable: true,
          value: "sp_id",
        },
        { text: "封面卡片", value: "sp_cn" },
        { text: "卡包英文名", value: "sp_en" },
        { text: "卡包日文名", value: "sp_jp" },
        { text: "", value: "data-table-expand" },
      ],
      cardsHeaders: [
        {
          text: "卡密",
          align: "start",
          value: "id",
        },
        {
          text: "卡图",
          sortable: false,
          value: "img",
        },
        { text: "卡名", value: "cn_n" },
        { text: "英文名", value: "en_n" },
        { text: "日文名", value: "jp_n" },
      ],
      spList: [],
    };
  },
  methods: {
    searchSp(pattern) {
      this.result = this.fuse.search(pattern);
      if (this.keyWord.length) {
        this.spList = [];
        this.result.forEach((element) => {
          this.spList.push(element.item);
        });
      } else {
        this.spList = this.$store.getters["sp"];
      }
    },
    handleClickSp(e) {
      this.onSingleCellClick(e);
      if (this.webSearch) {
        window.open(
          "https://yugipedia.com/wiki/" +
            e.target.outerText.replace(/\s+/g, "_"),
          "_blank"
        );
      }
    },
    handleClickCard(item) {
      if (this.webSearch) {
        window.open("https://ygocdb.com/?search=" + item.cid, "_blank");
      }
    },
    getCardImgUrl(id) {
      return (
        "https://cdn.233.momobako.com/ygopro/pics/" +
        id.toString() +
        ".jpg!thumb2"
      );
    },
    onSingleCellClick(e) {
      this.$copyText(e.target.outerText).then(
        function () {
          // console.log(e)
        },
        function () {
          // console.log(e)
        }
      );
    },
  },
  created() {
    this.$store.dispatch("getSpData").then(() => {
      this.setFuseSearch();
      this.spList = this.$store.getters["sp"];
    });
  },
};
</script>