<template>
  <div id="user-form">
    <form @submit.prevent="handleSubmit">
      <p v-if="error && submitting" class="error-message">
        ! Please fill all the fields!
      </p>
      <p v-if="success" class="success-message">
        ✅ Noice
      </p>
      <label>E-Mail</label>
      <input
        type="text"
        v-model="user.email"
        :class="{'has-error': submitting && invalidEmail}"
        @focus="clearStatus"
        @keypress="clearStatus"
        ref="first"
      />
      <label>Name</label>
      <input
        type="text"
        v-model="user.name"
        :class="{'has-error': submitting && invalidName}"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <button>Add User</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "user-form",
  data() {
    return {
      submitting: false,
      error: false,
      success: false,
      user: {
        email: "",
        name: ""
      }
    };
  },
  computed: {
    invalidName() {
      return this.user.name === "";
    },

    invalidEmail() {
      return this.user.email === "";
    }
  },

  methods: {
    handleSubmit() {
      this.submitting = true;
      this.clearStatus();

      if (this.invalidName || this.invalidEmail) {
        this.error = true;
        return;
      }

      this.$emit("add:user", this.user);
      this.$refs.first.focus()

      this.user = {
        name: "",
        email: ""
      };

      this.error = false;
      this.success = true;
      this.submitting = false;
    },

    clearStatus() {
      this.success = false;
      this.error = false;
    }
  }
};
</script>

<style scoped>
form {
  margin-bottom: 2rem;
}

[class*="-message"] {
  font-weight: 500;
}

.error-message {
  color: #d33c40;
}

.success-message {
  color: #32a95d;
}
</style>