<script setup>
import { ref, onMounted } from 'vue';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import { Ports, MicroService } from '@/service/Constant.js';
import axios from 'axios';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const project = ref([]);
const projectName = ref('');
const projectDescription = ref('');
const projectDialog = ref(false);
const uploadedFileName = ref('');
const fileUploadRef = ref(null);

const getAllProjects = async () => {
    // try {
    //     const response = await axios.get(MicroService['simple'] + Ports['projects'] + '/get_project');
    //     console.log(response.data['data']);
    //     project.value = response.data['data'];
    // } catch (error) {
    //     console.error(error);
    // }
};

project.value = [{ name: 1 }, { name: 2 }];

const postProject = async () => {
    try {
        const response = await axios.post(MicroService['simple'] + Ports['project'] + '/create_project/' + account.value, {
            proj_name: projectName.value,
            proj_description: projectDescription.value,
            proj_image: uploadedFileName.value // Include uploaded file names in the request
        });
        console.log(response.data['data']);
        toast.add({ severity: 'success', summary: 'Success', detail: 'Project created successfully', life: 3000 });
        clearFields();
    } catch (error) {
        console.error(error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to create project', life: 3000 });
    }
};
const onUpload = (event) => {
    const uploadedFiles = event.files;
    uploadedFileName.value = uploadedFiles.map((file) => file.name).join(', '); // Store uploaded file names
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
};
const openNew = () => {
    project.value = {};
    // submitted.value = false;
    projectDialog.value = true;
};
const hideDialog = () => {
    projectDialog.value = false;
    // submitted.value = false;
};
onMounted(() => {
    getAllProjects();
});
</script>
<template>
    <div class="card">
        <h2>Manage Projects</h2>
        <div class="">
            <Button label="Post" icon="pi pi-plus" class="mr-2" severity="help" @click="openNew" />
        </div>
        <Dialog v-model:visible="projectDialog" :style="{ width: '450px' }" header="Product Details" :modal="true" class="p-fluid">
            <div class="field">
                <label for="name1">Project name:</label>
                <InputText id="name1" type="text" v-model="projectName" />
            </div>
            <div class="field">
                <label for="images">Add images:</label>
                <FileUpload ref="fileUploadRef" name="demo[]" @uploader="onUpload" :multiple="true" accept="image/*" :maxFileSize="1000000" customUpload />
            </div>
            <div class="field">
                <label for="description">Project description:</label>
                <Textarea id="address" rows="4" v-model="projectDescription" />
            </div>
            <template #footer>
                <Button label="Cancel" icon="pi pi-times" text="" @click="hideDialog" />
                <Button label="Save" icon="pi pi-check" text="" @click="postProject" />
            </template>
        </Dialog>
        <!-- Loop to display creators dynamically -->
        <div class="row">
            <div>
                <div class="col-12" style="display: flex">
                    <Card style="width: 21rem; overflow: hidden" v-for="(project, index) in project" :key="index">
                        <template #header>
                            <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
                        </template>
                        <template #title> {{ project.name }} </template>
                        <template #subtitle>{{ project.proj_brand }}</template>
                        <template #content>
                            <p class="m-0">
                                {{ project.proj_description }}
                            </p>
                        </template>
                    </Card>
                </div>
            </div>
        </div>
    </div>
</template>
