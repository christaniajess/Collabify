<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import { Ports, MicroService } from '@/service/Constant.js';

import axios from 'axios';
import { useRouter } from 'vue-router';
const router = useRouter();
var accept = false;
const filters = ref({});
const collab = ref([]);
const ongoing_collab = ref([]);
const pending_collab = ref([]);
const loaded = ref(false);
const account = ref();
const account_type = ref();
const collab_status = [
    { name: 'In-progress', code: 'In-progress' },
    { name: 'Review', code: 'Review' }
];
const selectedStatus = ref();
const columns = ref([]);

const getCollabInfo = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['collab'] + '/collaborations/cc/' + account.value);
        console.log(response.data['data']);
        collab.value = response.data['data'];

        pending_collab.value = collab.value.filter((item) => item.collab_status === 'Pending');
        pending_collab.value.forEach((item, index) => {
            item.sn = index + 1;
            item.edit_visible = false;
        });
        ongoing_collab.value = collab.value.filter((item) => item.collab_status === 'In-progress' || item.collab_status === 'Review');
        ongoing_collab.value.forEach((item, index) => {
            item.sn = index + 1;
            item.edit_visible = false;
        });
        loaded.value = true;
    } catch (error) {
        console.error(error);
    }
};

const update_status = async (brand_id, status = false) => {
    try {
        var update_collab_status;
        if (status) {
            update_collab_status = status;
        } else {
            update_collab_status = selectedStatus.value;
        }
        const response = await axios.put(MicroService['simple'] + Ports['collab'] + '/collaborations/status', {
            cc_id: account.value,
            brand_id: brand_id,
            collab_status: update_collab_status
        });

        console.log(response.data);
        getCollabInfo();
    } catch (error) {
        console.error(error);
    }
};

const rejectCollab = async (brand_id) => {
    try {
        const response = await axios.delete(MicroService['simple'] + Ports['collab'] + '/collaborations', { data: { cc_id: account.value, brand_id: brand_id } });

        console.log(response.data);
        getCollabInfo();
    } catch (error) {
        console.error(error);
    }
};

const setBlacklist = async (brand_id) => {
    try {
        const response = await axios.post(MicroService['simple'] + Ports['blacklist'] + '/blacklist', { data: { account: account.value, banned_account: brand_id } });
        console.log(response.data['data']);
    } catch (error) {
        console.error(error);
    }
};

const payment = async (brand_id) => {
    try {
        const response = await axios.put(MicroService['simple'] + Ports['payment'] + '/collaborations/status', {
            cc_id: account.value,
            brand_id: brand_id,
            collab_status: 'Paid'
        });

        console.log(response.data);
        getCollabInfo();
    } catch (error) {
        console.error(error);
    }
};

onBeforeMount(() => {
    initFilters();
    if (localStorage.id) {
        account.value = localStorage.id;
        account_type.value = localStorage.acc_type;
        console.log(account_type.value == 'cc');
    } else {
        router.push('/auth/login');
    }
});

onMounted(async () => {
    await getCollabInfo();
    if (account_type.value == 'cc') {
        columns.value = [
            { field: 'sn', header: 'S/N' },
            { field: 'brand_id', header: 'Brand' },
            { field: 'collab_title', header: 'Title' },
            { field: 'collab_status', header: 'Status' }
        ];
    } else {
        columns.value = [
            { field: 'sn', header: 'S/N' },
            { field: 'cc_id', header: 'Content Creator' },
            { field: 'collab_title', header: 'Title' },
            { field: 'collab_status', header: 'Status' }
        ];
    }
});

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card" v-if="loaded">
                <DataTable
                    ref="dt"
                    :value="ongoing_collab"
                    dataKey="id"
                    :paginator="true"
                    :rows="10"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} collabs"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">On-going Collab</h5>
                            <IconField iconPosition="left" class="block mt-2 md:mt-0">
                                <InputIcon class="pi pi-search" />
                                <InputText class="w-full sm:w-auto" v-model="filters['global'].value" placeholder="Search..." />
                            </IconField>
                        </div>
                    </template>

                    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :sortable="true" headerStyle="width:14%; min-width:10rem;"></Column>

                    <Column headerStyle="width:14%;" v-if="account_type == 'cc'">
                        <template #body="slotProps">
                            <div class="flex flex-wrap gap-2">
                                <Button label="Edit" severity="warning" @click="slotProps.data.edit_visible = true" />
                                <Dialog v-model:visible="slotProps.data.edit_visible" modal header="Edit Collab" :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>

                                    <div class="flex align-items-center gap-3 mb-5">
                                        <label for="email" class="font-semibold w-6rem">Status</label>
                                        <Dropdown v-model="selectedStatus" :options="collab_status" optionLabel="name" placeholder="Select a Status" class="w-full md:w-14rem" />
                                    </div>
                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.edit_visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Update"
                                            @click="
                                                update_status(slotProps.data.brand_id);
                                                slotProps.data.edit_visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>
                            </div>
                        </template>
                    </Column>

                    <Column headerStyle="width:14%;" v-if="account_type == 'brand'">
                        <template #body="slotProps">
                            <div class="flex flex-wrap gap-2">
                                <Button label="Pay" severity="warning" v-if="slotProps.data.collab_status == 'Review'" @click="slotProps.data.edit_visible = true" />

                                <Dialog v-model:visible="slotProps.data.edit_visible" modal header="Pay" :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>

                                    <div class="flex align-items-center gap-3 mb-5">
                                        <label for="email" class="font-semibold w-6rem">Content Creator</label>
                                        {{ slotProps.data.cc_id }}
                                    </div>
                                    <div class="flex align-items-center gap-3 mb-5">
                                        <label for="email" class="font-semibold w-6rem">Collab title</label>
                                        {{ slotProps.data.collab_title }}
                                    </div>

                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.edit_visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Pay"
                                            @click="
                                                payment(slotProps.data.brand_id);
                                                slotProps.data.edit_visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>
                            </div>
                        </template>
                    </Column>
                </DataTable>
            </div>

            <div class="card" v-if="loaded">
                <DataTable
                    ref="dt"
                    :value="pending_collab"
                    dataKey="id"
                    :paginator="true"
                    :rows="10"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} collabs"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">Pending Collab</h5>
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
                                <Button
                                    label="Accept"
                                    @click="
                                        slotProps.data.edit_visible = true;
                                        accept = true;
                                    "
                                />
                                <Button
                                    label="Reject"
                                    severity="danger"
                                    @click="
                                        slotProps.data.edit_visible = true;
                                        accept = false;
                                    "
                                />

                                <Dialog v-if="accept" v-model:visible="slotProps.data.edit_visible" modal header="Are you sure to accept this collab? " :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>

                                    <div class="flex align-items-center gap-3 mb-5">
                                        <p class="font-semibold w-6rem">Brand: {{ slotProps.data.brand_id }}</p>
                                    </div>
                                    <div class="flex align-items-center gap-3 mb-5">
                                        <p class="font-semibold w-6rem">Title: {{ slotProps.data.collab_title }}</p>
                                    </div>

                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.edit_visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Accept"
                                            @click="
                                                update_status(slotProps.data.brand_id, 'In-progress');
                                                slotProps.data.edit_visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>

                                <Dialog v-else v-model:visible="slotProps.data.edit_visible" modal header="Are you sure to reject this collab? " :style="{ width: '25rem' }">
                                    <span class="p-text-secondary block mb-5">{{ slotProps.cc_id }}</span>

                                    <div class="flex align-items-center gap-3 mb-5">
                                        <p class="font-semibold w-6rem">Brand: {{ slotProps.data.brand_id }}</p>
                                    </div>
                                    <div class="flex align-items-center gap-3 mb-5">
                                        <p class="font-semibold w-6rem">Title: {{ slotProps.data.collab_title }}</p>
                                    </div>

                                    <div class="flex justify-content-end gap-2">
                                        <Button type="button" label="Cancel" severity="secondary" @click="slotProps.data.edit_visible = false"></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Reject"
                                            @click="
                                                rejectCollab(slotProps.data.brand_id, 'Reject');
                                                slotProps.data.edit_visible = false;
                                            "
                                        ></Button>
                                        <Button
                                            type="button"
                                            severity="danger"
                                            label="Reject and blacklist"
                                            @click="
                                                rejectCollab(slotProps.data.brand_id, 'Reject');

                                                setBlacklist(slotProps.data.brand_id);
                                                slotProps.data.edit_visible = false;
                                            "
                                        ></Button>
                                    </div>
                                </Dialog>
                            </div>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </div>
    </div>
</template>
