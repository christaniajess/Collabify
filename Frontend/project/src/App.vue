<script></script>

<template>
    <router-view />
</template>

<style>
/* Styling buttons based off what the button's label is */
button[aria-label='View'] {
    background-color: #7879ed !important;
    border-color: #7879ed !important;
    color: white !important;
}

button[aria-label='Pay'] {
    background-color: #62d388 !important;
    border-color: #62d388 !important;
    color: white !important;
}

/* button[aria-label='Cancel'] {
    background-color: #d20f0f !important;
    border-color: #d20f0f !important;
    color: white !important;
} */
</style>
