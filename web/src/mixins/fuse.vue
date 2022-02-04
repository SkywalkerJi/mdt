
<script>
import Fuse from "fuse.js";
export default {
  name: "mixins-fuse",
  data() {
    return {
      options: {
        // isCaseSensitive: false,
        // includeScore: false,
        // shouldSort: true,
        // includeMatches: false,
        // findAllMatches: false,
        // minMatchCharLength: 1,
        // location: 0,
        // threshold: 0.6,
        // distance: 100,
        // useExtendedSearch: false,
        // ignoreLocation: false,
        // ignoreFieldNorm: false,
        // fieldNormWeight: 1,
        keys: [
          "sp_cn",
          "sp_en",
          "sp_jp",
          "cards.cn_n",
          "cards.en_n",
          "cards.jp_n",
          "cards.id",
          "cards.cid",
        ],
      },
      fuse: {},
      result:[],
    };
  },
  methods: {
    setFuse(list, options) {
      this.fuse = new Fuse(list, options);
    },

    setFuseSearch() {
      this.setFuse(this.$store.getters["sp"], this.options);
    },
  },
};
</script>
