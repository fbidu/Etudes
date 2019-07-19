<template>
  <div id="app" class="small-container">
    <h1>Random Number</h1>
    <RandomNumber />

    <h1>Random Sequence</h1>
    <RandomSequence />

    <h1>Random String</h1>
    <RandomString />
  </div>
</template>

<script>
import RandomNumber from "@/components/RandomNumber.vue"
import RandomSequence from "@/components/RandomSequence.vue"
import RandomString from "@/components/RandomString.vue"

export default {
  name: 'app',
  components: {
    RandomNumber,
    RandomSequence,
    RandomString
  }
}
</script>

<style>
  .small-container {
    max-width: 680px;
    margin-left: 3%;
  }
</style>