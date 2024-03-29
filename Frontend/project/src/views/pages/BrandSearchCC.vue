<script setup>
import { ref, onMounted } from 'vue';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import { Ports, MicroService } from '@/service/Constant.js';
import axios from 'axios';

const account = ref([]);
const loaded = ref(false);
const keyword = ref('');

const getAllCreators = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['account'] + '/all_users');
        console.log(response.data['data']);
        // Filter and append only "cc" user type data into account.value
        account.value = response.data['data'].filter((item) => item.acc_type === 'cc');
        loaded.value = true;
    } catch (error) {
        console.error(error);
    }
};

const searchCreators = async () => {
    // Use the keyword value here for searching
    console.log(keyword.value);
    try {
        const response = await axios.get(MicroService['simple'] + Ports['account'] + '/users/interests/' + keyword.value);
        console.log(response.data['data']);
        // Filter and append only "cc" user type data into account.value
        account.value = response.data['data'].filter((item) => item.acc_type === 'cc');
        loaded.value = true;
    } catch (error) {
        console.error(error);
    }
    // Call your search logic/function here
};

onMounted(() => {
    getAllCreators();
});
</script>
<template>
    <div class="card">
        <h2>Search</h2>
        <!-- Loop to display three cards in a row -->
        <div class="col-12 md:col-12">
            <InputGroup>
                <Button label="Search" @click="searchCreators" />
                <InputText v-model="keyword" placeholder="Keyword" />
            </InputGroup>
        </div>
        <div class="card" style="width: 100%">
            <!-- Loop to display creators dynamically -->
            <div class="grid">
                <Card v-for="(creator, index) in account" :key="index" style="width: 20rem; overflow: hidden; margin: auto; margin-bottom: 1em" class="col-4">
                    <template #header>
                        <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
                    </template>
                    <template #title>{{ creator.full_name }}</template>
                    <template #subtitle>Interests</template>
                    <template #content>
                        <p class="m-0">
                            {{ creator.interests }}
                        </p>
                    </template>
                    <Button label="Help" severity="help" class="mb-2 mr-2" />
                </Card>
            </div>
        </div>
    </div>
</template>
