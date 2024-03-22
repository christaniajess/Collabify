<script setup>
    import { RouterLink, RouterView } from 'vue-router'
</script>
<style scoped>
    .full-panel {
    /* border: 3px solid #000; 1px solid black border */
    margin: 0;
    padding: 0;
    height: 100%;
    }
</style>
<template>
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
        rel="stylesheet"
        crossorigin="anonymous"
    />
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet" />
    <div class="full-panel">
        <RouterView />
    </div>
</template>