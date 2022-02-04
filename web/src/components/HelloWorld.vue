<template>
  <p>{{ $t("hello") }}</p>
</template>

<script>
export default {
  name: "HelloI18n",
  created: function () {
    console.log(process.env.VUE_APP_I18N_LOCALE);
  },
};
</script>
