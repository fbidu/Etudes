<template>
  <div id="user-list">
    <p v-if="users.length < 1" class="empty-table">
      No usersss
    </p>
    <div v-else>
      <p>{{ listName }}</p>
      <table>
        <thead>
          <th>e-mail</th>
          <th>Name</th>
          <th>Actions</th>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.email }}</td>
            <td>{{ user.name }}</td>
            <td>
              <button>Edit</button>
              <button @click="$emit('delete:user', user.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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

button {
    margin: 0 0.5rem 0 0;
}
</style>