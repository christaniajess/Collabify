<script setup>
import { ref, onMounted } from 'vue';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import axios from 'axios';

const dataviewValue = ref(null);
const layout = ref('grid');
const sortKey = ref(null);
const sortOrder = ref(null);
const sortField = ref(null);

onMounted(() => {
    // productService.getProductsSmall().then((data) => (dataviewValue.value = data));
});

const getAllCreators = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['accounts'] + '/accounts/users/' + account.value);
        console.log(response.data['data']);
        collab.value = response.data['data'];
        collab.value.forEach((item, index) => {
            item.sn = index + 1;
            item.edit_visible = false;
        });
        loaded.value = true;
    } catch (error) {
        console.error(error);
    }
};

const onSortChange = (event) => {
    const value = event.value.value;
    const sortValue = event.value;

    if (value.indexOf('!') === 0) {
        sortOrder.value = -1;
        sortField.value = value.substring(1, value.length);
        sortKey.value = sortValue;
    } else {
        sortOrder.value = 1;
        sortField.value = value;
        sortKey.value = sortValue;
    }
};
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
        <div class="card col-12 flex">
            <div class="col-4" v-for="index in 3" :key="index">
                <Card style="width: 21rem; overflow: hidden">
                    <template #header>
                        <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
                    </template>
                    <template #title>Advanced Card</template>
                    <template #subtitle>Card subtitle</template>
                    <template #content>
                        <p class="m-0">
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
                            quas!
                        </p>
                    </template>
                    <template #footer>
                        <div class="flex gap-3 mt-1">
                            <Button label="Cancel" severity="secondary" outlined class="w-full" />
                            <Button label="Save" class="w-full" />
                        </div>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>

