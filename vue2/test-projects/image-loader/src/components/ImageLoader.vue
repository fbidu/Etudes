<template>
  <div>
    <h1 class="title">{{ message }}, I'm the Loader!</h1>
    <input v-model="target" type="text" />
    <img :src="target" />
  </div>
</template>

<script>
export default {
  name: "image-loader",
  data() {
    return {
      message: "Hi",
      target: "./assets/logo.png"
    };
  }
};
</script>

<style scoped>
</style>

