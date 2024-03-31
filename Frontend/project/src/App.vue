<script></script>

<template>
    <router-view />
</template>

<style>
/* Styling buttons based off what the button's label is */
button[aria-label="View"] {
    background-color: #7879ED !important;
    border-color: #7879ED !important;
    color: white !important;
}

button[aria-label="Pay"] {
    background-color: #62D388 !important;
    border-color: #62D388 !important;
    color: white !important;
}

button[aria-label="Cancel"] {
    background-color: #D20F0F !important;
    border-color: #D20F0F !important;
    color: white !important;
}

</style>
