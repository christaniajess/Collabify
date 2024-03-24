<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import {Ports, MicroService} from '@/service/Constant.js';
import axios from 'axios';


const filters = ref({});
const blacklist = ref([]);
const getblacklistInfo = async () => {
    try {
        const response = await axios.get(MicroService["simple"] + Ports["blacklist"] + '/blacklist/all');

        var data = response.data["data"]["records"];
        data.forEach((item, index) => {
            item.sn = index + 1;
        });

        blacklist.value = data;
        return data;
    } catch (error) {
        console.error(error);
    }
};

onBeforeMount(async () => {
    initFilters();


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
    { field: 'date', header: 'Date' },
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
                    {{ slotProps }}

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
                    
                    <Column headerStyle="width:14%;"     >
                        <template #body >
                            <div class="flex flex-wrap gap-2">
                                <Button label="Remove" severity="danger" />
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
