<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { Ports, MicroService } from '@/service/Constant.js';

const router = useRouter();
const loaded = ref(false);

const filters = ref({});
const collab = ref([]);
const ongoing_collab = ref([]);
const pending_collab = ref([]);
const account = ref();
const account_type = ref();
const id = ref('');
const columns = ref([]);
const response = ref();
const notification = ref([]);
let isGettingNotification = false;
const notification_ready = ref(false);
onMounted(() => {
    if (localStorage.id) {
        account.value = localStorage.id;
        account_type.value = localStorage.acc_type;

        getCollabInfo();
    } else {
        router.push('/auth/login');
    }
});

watch(
    () => id.value,
    (newId) => {
        localStorage.id = newId;
    }
);

const getCollabInfo = async () => {
    try {
        if (account_type.value == 'cc') {
            response.value = await axios.get(MicroService['simple'] + Ports['collab'] + '/collaborations/cc/' + account.value);
        } else {
            response.value = await axios.get(MicroService['simple'] + Ports['collab'] + '/collaborations/brand/' + account.value);
        }

        console.log(response.value.data['data']);
        collab.value = response.value.data['data'];

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

if (localStorage.acc_type == 'cc') {
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

const getNotification = async () => {
    try {
        console.log('Getting notification');
        isGettingNotification = true;
        const response = await axios.get(MicroService['simple'] + Ports['notification'] + '/notification/consume', { params: { topic: account.value } });
        notification.value = response.data['message'].reverse();
        notification_ready.value = true;
        console.log(response.data['message']);
        collab.value = response.data;
        // Format each message in notification.value
        // for (let i = 0; i < notification.value.length; i++) {
        //     notification.value[i] = { sender: notification.value[i]['sender'], message: notification.value[i]['message'].replace(/;/g, '<br>') };
        // }
    
    
    
    } catch (error) {
        console.error(error);
    } finally {
        isGettingNotification = false;
    }
};

const runGetNotification = () => {
    if (!isGettingNotification) {
        getNotification();
    }
};

// Run getNotification every second
const intervalId = setInterval(runGetNotification, 10000);
onBeforeUnmount(() => {
    clearInterval(intervalId);
});

</script>

<template>
    <div class="grid">
        <div class="col-12 lg:col-6 xl:col-8">
            <div class="card mb-3" v-if="loaded">
                <DataTable
                    ref="dt"
                    :value="ongoing_collab"
                    dataKey="id"
                    :paginator="true"
                    :rows="5"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} collabs"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">On-going Collab</h5>
                        </div>
                    </template>

                    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :sortable="true" headerStyle="width:14%; min-width:10rem;"></Column>
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
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} collabs"
                >
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0">Pending Collab</h5>
                        </div>
                    </template>
                    <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" :sortable="true" headerStyle="width:14%; min-width:10rem;"></Column>
                </DataTable>
            </div>
        </div>

        <div class="col-12 xl:col-4">
            <div class="card mb-3">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <h3>Welcome,</h3>
                        <div class="text-900 font-medium text-xl">{{ account }}</div>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="flex align-items-center justify-content-between mb-4">
                    <h5>Notifications</h5>
                </div>

                <ul class="p-0 mx-0 mt-0 mb-4 list-none" v-if="notification_ready">
                    <li v-for="message in notification" class="flex align-items-center py-2 border-bottom-1 surface-border">
                        <div class="w-3rem h-3rem flex align-items-center justify-content-center bg-blue-100 border-circle mr-3 flex-shrink-0">
                            <i class="pi pi-dollar text-xl text-blue-500"></i>
                        </div>
                        <span class="text-900 line-height-3">
                            <h4>From {{ message.sender }}</h4>
                            <span class="text-700" style="white-space: pre-line;">{{ message.message }}</span>
                        </span>
                    </li>
                </ul>
                <ProgressSpinner v-else style="display: flex" />
            </div>
        </div>
    </div>
</template>
