<script setup>
import { ref } from 'vue';
import { useToast } from 'primevue/usetoast';

const toast = useToast();

const projectName = ref('');
const projectDescription = ref('');
const fileUploadRef = ref(null);

const clearFields = () => {
    projectName.value = '';
    projectDescription.value = '';
    fileUploadRef.value.clear(); // Clear uploaded files
};

const onUpload = () => {
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
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
                    <Button label="Save" icon="pi pi-check" />
                    <Button label="Delete" icon="pi pi-trash" @click="clearFields" />
                    <Button label="Cancel" icon="pi pi-times" />
                </ButtonGroup>
            </div>
        </div>
    </div>
</template>
