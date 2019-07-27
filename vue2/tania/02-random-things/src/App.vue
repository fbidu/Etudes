<template>
  <div id="app" class="small-container">
    <h1>Random Number</h1>
    <random-number />

    <h1>Random Sequence</h1>
    <random-sequence />

    <h1>Random String</h1>
    <random-string />

    <h1>Look at them users!</h1>
    <user-list :listName="listName" :users="users" @delete:user="deleteUser" />

    <h1>Add moooore</h1>
    <user-form @add:user="addUser" />
  </div>
</template>

<script>
import RandomNumber from "@/components/RandomNumber.vue";
import RandomSequence from "@/components/RandomSequence.vue";
import RandomString from "@/components/RandomString.vue";
import UserForm from "@/components/UserForm.vue";
import UserList from "@/components/UserList.vue";

export default {
  name: "app",
  components: {
    RandomNumber,
    RandomSequence,
    RandomString,
    UserList,
    UserForm
  },

  data: function() {
    return {
      listName: "hai",
      users: []
    };
  },

  methods: {
    async deleteUser(userID) {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/users/${userID}`, {
            method: "DELETE"
        });
        this.users = this.users.filter(user => user.id !== userID )
      } catch(error){
        console.error(error)
      }
    },

    async getUsers() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/users"
        );
        const data = await response.json();
        this.users = data;
      } catch (error) {
        console.error(error);
      }
    },

    async addUser(user) {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/users",
          {
            method: "POST",
            body: JSON.stringify(user),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
          }
        );
        const data = await response.json();
        this.users = [...this.users, data];
      } catch (error) {
        console.error(error);
      }
    },

    async editUser(id, updatedUser) {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/users/${id}`,
          {
            method: "PUT",
            body: JSON.stringify(updatedUser),
            headers: { "Content-type": "application/json; charset=UTF-8" }
          }
        );
        const data = await response.json();
        this.users = this.users.map(users => (users.id === id ? data : users));
      } catch (error) {
        console.error(error);
      }
    }
  },

  mounted() {
    this.getUsers();
  }
};
</script>

<style>
.small-container {
  max-width: 680px;
  margin-left: 3%;
}
</style>