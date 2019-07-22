<template>
  <div id="user-form">
    <form @submit.prevent="handleSubmit">
      <label>E-Mail</label>
      <input type="text" v-model="user.email"/>
      <label>Name</label>
      <input type="text" v-model="user.name"/>
      <button>Add User</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "user-form",
  data() {
      return {
          user: {
              email: "",
              name: ""
          }
      }
  },
  methods: {
    handleSubmit() {
      this.$emit("add:user", this.user)
    }
  }
};
</script>

<style scoped>
</style>