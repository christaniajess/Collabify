<script setup>
import { ref, onMounted } from 'vue';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import { Ports, MicroService } from '@/service/Constant.js';
import axios from 'axios';

const account = ref([]);
const loaded = ref(false);

const getAllCreators = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['account'] + '/users');
        console.log(response.data['data']);
        // Filter and append only "cc" user type data into account.value
        account.value = response.data['data'].filter((item) => item.acc_type === 'cc');
        loaded.value = true;
    } catch (error) {
        console.error(error);
    }
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
                <Button label="Search" />
                <InputText placeholder="Keyword" />
            </InputGroup>
        </div>
<<<<<<< HEAD
        <div class="card">
            <!-- Loop to display creators dynamically -->
            <div class="row">
                <div v-for="(creator, index) in account" :key="index">
                    <div class="col-12">
                        <Card style="width: 21rem; overflow: hidden">
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
                        </Card>
                    </div>
                </div>
=======
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
                    
                </Card>
>>>>>>> 415d20d2eb8fba53d7d03d2180c9d30ade12ad62
            </div>
        </div>
    </div>
</template>
