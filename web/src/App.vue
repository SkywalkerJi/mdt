<template>
  <v-app id="inspire">
    <div ref="vantaRef">
      <v-navigation-drawer v-model="drawer" app>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="text-h6"
              >Yu-Gi-Oh! Master Duel</v-list-item-title
            >
            <v-list-item-title class="text-h6">MDT-web 工具</v-list-item-title>
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
      <v-app-bar app>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>{{ $route.name }}</v-toolbar-title>
      </v-app-bar>

      <v-main>
        <router-view></router-view>
      </v-main>
    </div>
  </v-app>
</template>

<script>
import RINGS from "vanta/src/vanta.rings";
import * as THREE from "three";
export default {
  data: () => ({
    drawer: false,
    items: [
      { title: "Secret Pack", icon: "mdi-card-search-outline", to: "/" },
      // { title: "关于", icon: "mdi-information-variant", to: "/about" },
    ],
  }),
  mounted() {
    this.vantaEffect = RINGS({
      el: this.$refs.vantaRef,
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 220.0,
      minWidth: 200.0,
      scale: 1.0,
      scaleMobile: 1.0,
      THREE: THREE,
    });
  },
  beforeDestroy() {
    if (this.vantaEffect) {
      this.vantaEffect.destroy();
    }
  },
};
</script>
<style>
.vanta-canvas {
  position: fixed !important;
}
</style>