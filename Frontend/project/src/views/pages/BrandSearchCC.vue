<script setup>
import { ref, onMounted } from 'vue';
import { Ports, MicroService } from '@/service/Constant.js';
// import userImages from '@/assets/images/users';
import axios from 'axios';

const account = ref([]);
const loaded = ref(false);
const keyword = ref('');
const images = ref([]);

const getAllCreators = async () => {
    try {
        const response = await axios.get(MicroService['service'] + Ports['account'] + '/all_users');
        console.log(response.data['data']);
        // Filter and append only "cc" user type data into account.value
        account.value = response.data['data'].filter((item) => item.acc_type === 'cc');
        loaded.value = true;

        account.value.forEach((item, index) => {
            item.imageUrl = new URL('/src/assets/images/users/' + item.user_photo, import.meta.url);
            // item.edit_visible = false;
        });
    } catch (error) {
        console.error(error);
    }
};

const searchCreators = async () => {
    // Use the keyword value here for searching
    console.log(keyword.value);
    try {
        const response = await axios.get(MicroService['service'] + Ports['account'] + '/users/interests/' + keyword.value);
        console.log(response.data['data']);
        // Filter and append only "cc" user type data into account.value
        account.value = response.data['data'].filter((item) => item.acc_type === 'cc');
        loaded.value = true;
        account.value.forEach((item, index) => {
            item.imageUrl = new URL('/src/assets/images/users/' + item.user_photo, import.meta.url);
            // item.edit_visible = false;
        });
    } catch (error) {
        console.error(error);
    }
    // Call your search logic/function here
};


const passUserid = (user_id) => {
    localStorage.clickedUserID = user_id;
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
            <div class="grid col-12">
                <Card v-for="(creator, index) in account" :key="index" style="width: 20rem; overflow: hidden; margin: auto; margin-bottom: 1em" class="col-3">
                    <template #header>
                        <img alt="user header" :src="creator.imageUrl" style="width: 100%; height: 250px; object-fit: cover; border-radius: 5%" />
                    </template>
                    <template #title>
                        {{ creator.full_name }}
                        <Badge value="" severity="secondary">{{ creator.acc_type === 'cc' ? 'Creator' : '' }}</Badge>
                    </template>
                    <template #subtitle>Interests</template>
                    <template #content>
                        <p class="m-0">
                            {{ creator.interests }}
                        </p>
                    </template>

                    <template #footer>
                        <Button
                            label="View Profile"
                            style="width: 100%; background-color: #7879ed; border-color: #7879ed"
                            @click="
                                passUserid(creator.user_id);
                                $router.push('/viewccprofile');
                            "
                        />
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>
