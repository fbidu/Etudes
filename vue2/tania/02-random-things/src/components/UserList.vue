<template>
  <div id="user-list">
    <p>{{ listName }}</p>
    <table>
      <thead>
        <th>e-mail</th>
        <th>Name</th>
        <th>last sign-in</th>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.email }}</td>
          <td>{{ user.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "user-list",
  props: {
    listName: String,
    users: Array
  }
};
</script>

<style scoped>
form {
    margin-bottom: 2rem;
}
</style>