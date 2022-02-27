<template>
  <v-app id="inspire">
      <v-navigation-drawer v-model="drawer" app>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="text-h6"
              >MDT-web GPLv3</v-list-item-title
            >
            <v-list-item-title class="text-h6">@SkywalkerJi</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar app collapse-on-scroll style="opacity: 1">
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>{{ $route.name }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="openGithub">
        <v-icon>mdi-github</v-icon>
      </v-btn>
      <v-btn icon  @click="openTwitter"> 
        <v-icon>mdi-twitter</v-icon>
      </v-btn>
      <v-btn icon  @click="openYoutube">
        <v-icon>mdi-youtube</v-icon>
      </v-btn>
      </v-app-bar>

      <v-main>
        <router-view></router-view>
      </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    items: [
      { title: "Secret Pack", icon: "mdi-card-search-outline", to: "/" },
      { title: "Convert", icon: "mdi-swap-horizontal", to: "/convert" },
      // { title: "关于", icon: "mdi-information-variant", to: "/about" },
    ],
  }),
  methods:{
  openGithub(){
    window.open("https://github.com/SkywalkerJi/mdt", "_blank");
  },
  openYoutube(){
    window.open("https://www.youtube.com/channel/UC3kA_NGfQFHMMn-kja8GTFA?sub_confirmation=1", "_blank");
  },
  openTwitter(){
    window.open("https://twitter.com/Skywalker_Ji", "_blank");
  },
  },
};
</script>
