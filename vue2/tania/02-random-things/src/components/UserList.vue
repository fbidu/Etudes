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
            <td v-if="editing === user.id">
              <input type="text" v-model="user.email" />
            </td>
            <td v-else>{{ user.email }}</td>
            <td v-if="user.id === editing">
              <input type="text" v-model="user.name" />
            </td>
            <td v-else>{{ user.name }}</td>
            <td v-if="user.id === editing">
              <button @click="editUser(user)">Save</button>
              <button class="muted-button" @click="cancelUser(user)">Cancel</button>
            </td>
            <td v-else>
              <button @click="editMode(user)">Edit</button>
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
  },
  data() {
    return {
      editing: null,
    }
  },
  methods: {
    editMode(user) {
      this.cachedUser = Object.assign({}, user)
      this.editing = user.id
    },

    editUser(user) {
      if (user.name === '' || user.email === '') return
      this.$emit('edit:user', user.id, user)
      this.editing = null
    },

    cancelUser(user) {
      Object.assign(user, this.cachedUser)
      this.editing = null
    }
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