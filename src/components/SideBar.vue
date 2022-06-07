<script>
export default {
    props: ['keyData', 'selectedIndex'],
    emits: ['updateIndex']
}
</script>

<template>
    <div id="barsd">
        <div class="countries" v-for="(keyD, index) in keyData" v-bind:key="keyD" @click="$emit('updateIndex', index)">
            <span class="active" v-if="index == selectedIndex">{{ keyD[0] }}</span>
            <span class="inactive" v-if="index !== selectedIndex">{{ keyD[0] }}</span>

        </div>
    </div>

</template>
<style>
@import '../assets/styles/sidebar.css';
</style>