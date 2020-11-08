<template>
  <v-app style="background: #eaeaea;">
    <v-main>
      <Main/>
    </v-main>
  </v-app>
</template>

<script>
import Main from './components/Main';

export default {
  name: 'App',

  components: {
    Main,
  },

  data: () => ({
    //
  }),
};
</script>

<style>
  body {
    background: grey;
  }
</style>
