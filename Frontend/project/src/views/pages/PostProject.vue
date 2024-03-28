<script setup>
import { ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import axios from 'axios';

const toast = useToast();

const projectName = ref('');
const projectDescription = ref('');
const fileUploadRef = ref(null);
const account = ref('0210');
const uploadedFileName = ref('');

const clearFields = () => {
    projectName.value = '';
    projectDescription.value = '';
    fileUploadRef.value.clear(); // Clear uploaded files
};

const onUpload = (event) => {
    const uploadedFiles = event.files;
    uploadedFileName.value = uploadedFiles.map(file => file.name).join(', '); // Store uploaded file names
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
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
        clearFields();
    } catch (error) {
        console.error(error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to create project', life: 3000 });
    }
};
</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-12">
            <div class="card p-fluid">
                <h5>Post Project</h5>
                <div class="field">
                    <label for="name1">Project name:</label>
                    <InputText id="name1" type="text" v-model="projectName" />
                </div>
                <div class="field">
                    <label for="email1">Add images:</label>
                    <FileUpload ref="fileUploadRef" name="demo[]" @uploader="onUpload" :multiple="true" accept="image/*" :maxFileSize="1000000" customUpload />
                </div>
                <div class="field">
                    <label for="age1">Project description:</label>
                    <Textarea id="address" rows="4" v-model="projectDescription" />
                </div>
                <ButtonGroup class="md:col-4">
                    <Button label="Save" icon="pi pi-check" @click="postProject" />
                    <Button label="Delete" icon="pi pi-trash" @click="clearFields" />
                    <Button label="Cancel" icon="pi pi-times" />
                </ButtonGroup>
            </div>
        </div>
    </div>
</template>
