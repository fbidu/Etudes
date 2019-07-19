<template>
    <div id="random-number">
        <p>I like the number {{ number }}</p>
    </div>
</template>

<script>
export default {
    name: "random-number",
    data: function() {
        return {
            "number": Math.ceil(Math.random() * 1000)
        }
    }
};
</script>

<style scoped>
</style>