<script setup>
import { ref, onMounted, onBeforeMount } from 'vue';
import { Ports, MicroService } from '@/service/Constant.js';
import axios from 'axios';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const project = ref([]);
const projectName = ref('');
const projectDescription = ref('');
const projectPostDialog = ref(false);
const projectEditDialog = ref(false);
const uploadedFileName = ref('');
const fileUploadRef = ref(null);
const visible = ref(false);
const account = ref('');

const getAllProjects = async () => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['project'] + '/get_project', { params: { cc_id: account.value } });
        console.log(response.data['data']);
        project.value = response.data['data'];
    } catch (error) {
        console.error(error);
    }
};
const postProject = async () => {
    try {
        const response = await axios.post(MicroService['simple'] + Ports['project'] + '/create_project/' + account.value, {
            proj_name: projectName.value,
            proj_description: projectDescription.value,
            proj_image: uploadedFileName.value // Include uploaded file names in the request
        });
        console.log(response.data['data']);
        toast.add({ severity: 'success', summary: 'Success', detail: 'Project created successfully', life: 3000 });
        await getAllProjects();
        projectPostDialog.value = false;
    } catch (error) {
        console.error(error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to create project', life: 3000 });
    }
};

const updateProject = async () => {
    try {
        const response = await axios.put(MicroService['simple'] + Ports['project'] + '/update_project', 
        {
            user_id: account.value,
            proj_name: projectName.value,
            proj_description: projectDescription.value,
            proj_image: uploadedFileName.value // Include uploaded file names in the request
        });
        console.log(response.data['data']);
        toast.add({ severity: 'success', summary: 'Success', detail: 'Project updated successfully', life: 3000 });
        await getAllProjects();
    } catch (error) {
        console.error(error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to update project', life: 3000 });
    }
};

const onUpload = (event) => {
    const uploadedFiles = event.files;
    uploadedFileName.value = uploadedFiles.map((file) => file.name).join(', '); // Store uploaded file names
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
};
const openNewPost = () => {
    // submitted.value = false;
    projectPostDialog.value = true;
};
const hideDialog = () => {
    projectPostDialog.value = false;
    projectEditDialog.value = false;
    // submitted.value = false;
};

const clearDialog = () => {
    projectName.value = '';
    projectDescription.value = '';
    uploadedFileName.value = '';
    projectEditDialog.value = false;
    projectPostDialog.value = false;
};


const deleteProject = async (projName) => {
  try {
    console.log('Deleting project:', projName);
    console.log('Account:', account.value);
    const response = await axios.delete(MicroService['simple'] + Ports['project'] + '/delete_project' + `/${account.value}/${projName}`);
    console.log(response.data);
    if (response.data.code === 200) {
      toast.add({ severity: 'success', summary: 'Success', detail: response.data.message });
      // Optionally, refresh your projects list here
      await getAllProjects();
    } else {
      toast.add({ severity: 'error', summary: 'Error', detail: response.data.message });
    }
  } catch (error) {
    console.error('Delete operation failed:', error);
    toast.add({ severity: 'error', summary: 'Error', detail: 'An error occurred while deleting the project.' });
  }
};

const editProject = (projData) => {
  projectName.value = projData.proj_name; // Assign current project's name
  projectDescription.value = projData.proj_description; // Assign current project's description
  projectEditDialog.value = true; // Show the edit dialog
};

onBeforeMount(() => {
    if (localStorage.id) {
        account.value = localStorage.id;
        console.log(localStorage.acc_type == 'cc');
    } else {
        router.push('/auth/login');
    }
});

onMounted(() => {
    getAllProjects();
});
</script>
<template>
    <div class="card">
        <div class="flex justify-content-between mx-3">
            <h2>Manage Projects</h2>
            <div class="">
                <Button label="Post" icon="pi pi-plus" class="mr-2" severity="help" @click="openNewPost" />
            </div>
        </div>
        <Dialog v-model:visible="projectPostDialog" :style="{ width: '450px' }" header="Product Details" :modal="true" class="p-fluid">
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
                <Button label="Cancel" icon="pi pi-times" text="" @click="hideDialog(); clearDialog()" />
                <Button label="Save" icon="pi pi-check" text="" @click="postProject(); clearDialog()" />
            </template>
        </Dialog>
        <!-- Loop to display creators dynamically -->
        <div class="grid m-3" style="width: 100%">
            <Card v-for="(project, index) in project" :key="index" style="width: 21rem; overflow: hidden" class="col-4 mx-auto">
                <template #header>
                    <img alt="user header" src="https://primefaces.org/cdn/primevue/images/usercard.png" />
                </template>
                <template #title>{{ project.proj_name }}</template>
                <template #subtitle>{{ project.proj_brand }}</template>
                <template #content>
                    <p class="m-0">
                        {{ project.proj_description }}
                    </p>
                    <br />
                    <div>
                        <Button label="Edit" class="mb-2 mr-2" @click="editProject(project)" />
                        <Dialog v-model:visible="projectEditDialog" modal header="Edit Profile" :style="{ width: '450px' }" class="p-fluid">
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
                                <Button label="Cancel" icon="pi pi-times" text="" @click="hideDialog(); clearDialog()" />
                                <Button label="Save1" icon="pi pi-check" text="" @click="updateProject(); clearDialog()" />
                            </template>
                        </Dialog>
                        <Button label="Delete" severity="danger" class="mb-2 mr-2" @click="deleteProject(project.proj_name)" />
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>
