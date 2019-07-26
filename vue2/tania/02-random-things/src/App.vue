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
      users: [
        {
          id: 0,
          name: "Felipe Rodrigues",
          email: "felipe@felipevr.com"
        }
      ]
    };
  },

  methods: {
    addUser(user) {
      let lastId = 0;

      if (this.users.length > 0) {
        lastId = this.users.length;
      }

      const newUser = { ...user, id: lastId };

      this.users = [...this.users, newUser];
    },

    deleteUser(userID) {
      this.users = this.users.filter(
        user => user.id !== userID
      )
    }
  }
};
</script>

<style>
.small-container {
  max-width: 680px;
  margin-left: 3%;
}
</style>