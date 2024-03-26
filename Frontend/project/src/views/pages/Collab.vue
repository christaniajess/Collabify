<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import { Ports, MicroService } from '@/service/Constant.js';

import axios from 'axios';

const filters = ref({});
const collab = ref([]);
const loaded = ref(false);
const account = ref('0210');
const collab_status = [
    { name: 'In-progress', code: 'In-progress' },
    { name: 'Done', code: 'Done' }
];
const selectedStatus = ref();

const getCollabInfo = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['collab'] + '/collaborations/cc/' + account.value);
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

const update_status = async (brand_id) => {
    try {

        const response = await axios.put(MicroService['simple'] + Ports['collab'] + '/collaborations/status', {
            cc_id: account.value,
            brand_id: brand_id,
            collab_status: selectedStatus.value.code
        });

        console.log(response.data);
        getCollabInfo();
    } catch (error) {
        console.error(error);
    }
};

onBeforeMount(() => {
    initFilters();
});

onMounted(async () => {
    await getCollabInfo();
});

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

const columns = ref([
    { field: 'sn', header: 'S/N' },
    { field: 'cc_id', header: 'Content Creator' },
    { field: 'collab_title', header: 'Title' },
    { field: 'collab_status', header: 'Status' }
]);
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card" v-if="loaded">
                <!-- <Toolbar class="mb-4">
                    <template v-slot:start>
                        <div class="my-2">
                            <Button label="New" icon="pi pi-plus" class="mr-2" severity="success" @click="openNew" />
                            <Button label="Delete" icon="pi pi-trash" severity="danger" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                        </div>
                    </template>

                    <template v-slot:end>
                        <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="mr-2 inline-block" />
                        <Button label="Export" icon="pi pi-upload" severity="help" @click="exportCSV($event)" />
                    </template>
                </Toolbar> -->

                <DataTable
                    ref="dt"
                    :value="collab"
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

                    <!-- <Column selectionMode="multiple" headerStyle="width: 3rem"></Column> -->

                    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :sortable="true" headerStyle="width:14%; min-width:10rem;"></Column>

                    <Column headerStyle="width:14%;">
                        <template #body="slotProps">
                            <div class="flex flex-wrap gap-2">
                                <Button label="View" v-if="slotProps.data.collab_status != 'rejected'" />
                                <Button label="Edit" severity="warning" v-if="slotProps.data.collab_status != 'rejected'" @click="slotProps.data.edit_visible = true" />

                                <Dialog v-model:visible="slotProps.data.edit_visible" modal header="Edit Collab" :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>
                                    <div class="flex align-items-center gap-3 mb-3">
                                        <label for="username" class="font-semibold w-6rem">Banned Account{{ slotProps.data.cc_id }}</label>
                                        {{ slotProps.data.banned_account }}
                                    </div>
                                    <div class="flex align-items-center gap-3 mb-5">
                                        <label for="email" class="font-semibold w-6rem">Status</label>
                                        <Dropdown v-model="selectedStatus" :options="collab_status" optionLabel="name" placeholder="Select a Status" class="w-full md:w-14rem" />
                                    </div>
                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Update"
                                            @click="
                                                update_status(slotProps.data.brand_id);
                                                slotProps.data.visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>

                                <Button label="Remove" severity="danger" v-if="slotProps.data.collab_status == 'rejected'" />
                                <Button label="Remove" severity="danger" v-if="slotProps.data.collab_status == 'In-progress'" />
                            </div>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </div>
    </div>
</template>
