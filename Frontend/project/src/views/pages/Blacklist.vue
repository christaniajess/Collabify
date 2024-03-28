<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import { Ports, MicroService } from '@/service/Constant.js';
import axios from 'axios';
import { useRouter } from 'vue-router';


const router = useRouter();
const filters = ref({});
const blacklist = ref([]);
const loaded = ref(false);
const account = ref();

const getblacklistInfo = async () => {
    let data = {
        account: account.value
    };

    let config = {
        method: 'get',
        maxBodyLength: Infinity,
        url: MicroService['simple'] + Ports['blacklist'] + '/blacklist',
        params: data
    };

    axios
        .request(config)
        .then((response) => {
            console.log(response['data']['data']);
            var result = response.data['data'];
            result.forEach((item, index) => {
                item.sn = index + 1;
                item.visible = false;
            });

            blacklist.value = result;
            loaded.value = true;
        })
        .catch((error) => {
            console.log(error);
        });
};

const remove_blacklist = async (banned_account) => {
    try {
        const payload = {
            account: account.value,
            banned_account: banned_account
        };
        const response = await axios.delete(MicroService['simple'] + Ports['blacklist'] + '/blacklist', { data: payload });

        console.log(response.data);
        getblacklistInfo();
    } catch (error) {
        console.error(error);
    }
};

onBeforeMount(async () => {
    initFilters();
    if (localStorage.id) {
        account.value = localStorage.id;
    } else {
        router.push('/auth/login');
    }
});

onMounted(async () => {
    getblacklistInfo();
});

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

const columns = ref([
    { field: 'sn', header: 'S/N' },
    { field: 'banned_account', header: 'Banned Account' },
    { field: 'date', header: 'Date' }
]);
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card">
                <DataTable
                    ref="dt"
                    :value="blacklist"
                    dataKey="id"
                    :paginator="true"
                    :rows="10"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">Manage Products</h5>
                            <IconField iconPosition="left" class="block mt-2 md:mt-0">
                                <InputIcon class="pi pi-search" />
                                <InputText class="w-full sm:w-auto" v-model="filters['global'].value" placeholder="Search..." />
                            </IconField>
                        </div>
                    </template>

                    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :sortable="true" headerStyle="width:14%; min-width:10rem;"></Column>
                    <Column headerStyle="width:14%;">
                        <template #body="slotProps">
                            <div class="flex flex-wrap gap-2">
                                <Button label="Remove" severity="danger" @click="slotProps.data.visible = true" />
                                <Dialog v-model:visible="slotProps.data.visible" modal header="Are you sure to remove this user from blacklist?" :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>
                                    <div class="flex align-items-center gap-3 mb-3">
                                        <label for="username" class="font-semibold w-6rem">Banned Account{{ slotProps.data.cc_id }}</label>
                                        {{ slotProps.data.banned_account }}
                                    </div>
                                    <div class="flex align-items-center gap-3 mb-5">
                                        <label for="email" class="font-semibold w-6rem">Banned Date</label>
                                        {{ slotProps.data.date }}
                                    </div>
                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Remove"
                                            @click="
                                                remove_blacklist(slotProps.data.banned_account);
                                                slotProps.data.visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>
                            </div>
                        </template>
                    </Column>
                    <!-- <Column field="S/N" header="S/N" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="blacklist">
                            <span class="p-column-title">S/N</span>
                            {{ blacklist.name }}
                        </template>
                    </Column>
                    <Column field="Content Creator" header="Content Creator" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Content Creator</span>
                            {{ slotProps.data.name }}
                        </template>
                    </Column>

                    <Column field="Title" header="Title" :sortable="true" headerStyle="width:14%; min-width:8rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Title</span>
                            {{ formatCurrency(slotProps.data.price) }}
                        </template>
                    </Column>
                    <Column field="Status" header="Status" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Status</span>
                            {{ slotProps.data.category }}
                        </template>
                    </Column> -->

                    <!-- <Column field="rating" header="Reviews" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Rating</span>
                            <Rating :modelValue="slotProps.data.rating" :readonly="true" :cancel="false" />
                        </template>
                    </Column> -->
                    <!-- <Column field="inventoryStatus" header="Status" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Status</span>
                            <Tag :severity="getBadgeSeverity(slotProps.data.inventoryStatus)">{{ slotProps.data.inventoryStatus }}</Tag>
                        </template>
                    </Column> -->
                    <!-- <Column headerStyle="min-width:10rem;">
                        <template #body="slotProps">
                            <Button icon="pi pi-pencil" class="mr-2" severity="success" rounded @click="editProduct(slotProps.data)" />
                            <Button icon="pi pi-trash" class="mt-2" severity="warning" rounded @click="confirmDeleteProduct(slotProps.data)" />
                        </template>
                    </Column> -->
                </DataTable>
            </div>
        </div>
    </div>
</template>
