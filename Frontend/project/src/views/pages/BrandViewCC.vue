<script setup>
import { ref, onMounted, onBeforeMount } from 'vue';
import axios from 'axios';
import Avatar from 'primevue/avatar';
import Button from 'primevue/button';
import Chip from 'primevue/chip';
import Carousel from 'primevue/carousel';
import ScrollPanel from 'primevue/scrollpanel';
import ScrollTop from 'primevue/scrolltop';
import Rating from 'primevue/rating';
import { Ports, MicroService } from '@/service/Constant.js';
import { useToast } from 'primevue/usetoast';
import { useRoute } from 'vue-router';

const toast = useToast();

const router = useRoute();
if (!router.params.user_id) {
    router.params.user_id = 123;
}
const account = ref(router.params.user_id);
const accountDetails = ref('');
const projectDetails = ref('');
const reviewDetails = ref('');
const collaborationDetails = ref('');
const recommendationDetails = ref('');
const accountPhoto = ref('');
const accountName = ref('');
const showReview = ref(false);

const responsiveOptions = ref([
    {
        breakpoint: '1024px',
        numVisible: 3,
        numScroll: 3
    },
    {
        breakpoint: '768px',
        numVisible: 2,
        numScroll: 2
    },
    {
        breakpoint: '560px',
        numVisible: 1,
        numScroll: 1
    }
]);

// clickedUserID
onBeforeMount(() => {
    if (localStorage.clickedUserID) {
        account.value = localStorage.clickedUserID;
    } else {
        console.log('No clicked user ID');
    }
});

const getCCProfile = async (user_id) => {
    try {
        console.log('HELLLOO');
        console.log(account.value);
        const response = await axios.get(MicroService['complex'] + Ports['complex_brandViewCC'] + '/view/cc/' + user_id);

        accountDetails.value = response.data.view.account;
        projectDetails.value = response.data.view.project;
        reviewDetails.value = response.data.view.review;
        collaborationDetails.value = response.data.view.collab;
        recommendationDetails.value = response.data.recommendation;

        console.log(accountDetails.value);
        console.log(projectDetails.value);
        console.log('TYPE OF PROJECT DETAILS')
        console.log(typeof(projectDetails.value));
        console.log(reviewDetails.value);
        console.log('TYPE  OF REVIEW DETAILS')
        console.log(typeof(reviewDetails.value));
        console.log(typeof(reviewDetails.value) === "object")
        if (typeof(reviewDetails.value) === "object") {
            showReview.value = true;
        }
        console.log(collaborationDetails.value);
        console.log('TYPE OF COLLAB DETAILS')
        console.log(typeof(collaborationDetails.value));
        console.log(recommendationDetails.value);
    } catch (error) {}
};

const getAccountImage = async (user_id) => {
    try {
        const response = await axios.get(MicroService['simple'] + Ports['account'] + '/users?user_id=' + user_id);

        accountPhoto.value = response.data.data.user_photo;
        accountName.value = response.data.data.full_name;
    } catch (error) {}
};

async function getBrandImages(details) {
    console.log("GETTING BRAND IMAGES")
    console.log(details.value);
    if (details.value.length > 0) {
      for (let detail of details.value) {
        console.log(detail);
        const photo = await getAccountImage(detail.brand_id);
        detail.brand_photo = accountPhoto.value;
        detail.brand_name = accountName.value;
    }
    }
    else {
      console.log("No details");
    }
}

const clickUser = (user_id) => {
  localStorage.clickedUserID = user_id;
  window.location.reload(true);
};

onMounted(async () => {
    await getCCProfile(account.value);
    await getBrandImages(reviewDetails);
    await getBrandImages(collaborationDetails);
});
</script>

<template>
    <div class="main-page">
        <!-- User Profile -->
        <div class="card">
            <div class="m-5">
                <div class="flex align-items-center gap-3">
                    <Avatar :image="'/src/assets/images/users/' + accountDetails.user_photo" class="mr-2" size="xlarge" shape="circle" />
                    <div>
                        <span class="font-medium text-3xl text-900">
                            {{ accountDetails.full_name }}
                        </span>
                        <div class="m-0 p-0 flex align-items-center">
                            <i class="pi pi-users m-0 p-0"></i>
                            <span class="m-0 ml-2 p-0 font-light">{{ collaborationDetails.length }} Collaborations</span>
                        </div>
                    </div>
                    <Chip label="CREATOR" />
                </div>
                <div class="flex align-items-start flex-column lg:justify-content-between lg:flex-row mt-2">
                    <div class="mt-3 lg:mt-0">
                        <Button label="Collaborate" class="p-button-outlined mr-2" icon="pi pi-user-plus"></Button>
                    </div>
                </div>
            </div>

            <hr />

            <div class="col-12">
                <div class="card">
                    <h5>{{ accountDetails.full_name }}'s Projects</h5>
                  
                    <Carousel v-if='!Array.isArray(projectDetails.value)' :value="projectDetails" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" circular :autoplayInterval="5000">
                        <template #item="slotProps">
                            <div class="border-1 surface-border border-round m-2 p-3">
                                <div class="mb-3">
                                    <div class="relative mx-auto">
                                        <img :src="'/src/assets/images/project/' + slotProps.data.proj_image" :alt="slotProps.data.proj_name" class="w-full border-round" style="height: 200px; object-fit: cover" />
                                    </div>
                                </div>
                                <div class="mb-3 font-medium">{{ slotProps.data.proj_name }}</div>
                                <div class="flex justify-content-between align-items-center">
                                    <h6 class="mt-0 font-light">{{ slotProps.data.proj_description }}</h6>
                                </div>
                            </div>
                        </template>
                    </Carousel>

                    <p v-else class="mx-auto">No projects yet</p>
                </div>
            </div>

            <hr />

            <div class="col-12">
                <h5>Reviews</h5>
                <div class="card">
                  

                    <ScrollPanel v-if='!showReview.value' class="mx-auto" style="width: 90%; height: 500px">
                        <div v-for="review in reviewDetails" :key="review.id" class="p-3">
                            <div class="flex gap-3 align-items-center">
                                <Avatar :image="'/src/assets/images/users/' + review.brand_photo" class="mr-2" size="xlarge" shape="circle" />
                                <div class="flex flex-column gap-1">
                                    <h5 class="p-0 m-0">{{ review.title }}</h5>
                                    <h6 class="p-0 m-0">{{ review.brand_name }}</h6>
                                    <Rating v-model="review.rating" readonly :cancel="false"></Rating>
                                </div>
                            </div>``
                            <p class="mt-3">
                                {{ review.content }}
                            </p>
                            <hr />
                        </div>
                        <ScrollTop
                            target="parent"
                            :threshold="100"
                            icon="pi pi-arrow-up"
                            :pt="{
                                root: 'w-2rem h-2rem border-round-sm bg-primary',
                                icon: {
                                    class: 'text-base'
                                }
                            }"
                        />
                    </ScrollPanel>
                    <p v-else class="mx-auto">No reviews yet</p>
                </div>
            </div>

            <hr />

            <div class="col-12">
                <div class="card">
                    <h5>{{ accountDetails.full_name }}'s Collaborations</h5>
                    <Carousel v-if="!Array.isArray(collaborationDetails.value)" :value="collaborationDetails" :numVisible="2" :numScroll="1" :responsiveOptions="responsiveOptions">
                        <template #item="slotProps">
                            <div class="border-1 surface-border border-round m-2 p-3">
                                <div class="mb-3">
                                    <div class="relative mx-auto">
                                        <img :src="'/src/assets/images/users/' + slotProps.data.brand_photo" :alt="slotProps.data.collab_title" class="w-full border-round" style="width: 250px !important" />
                                    </div>
                                </div>
                                <div class="mb-3 font-medium">{{ slotProps.data.collab_title }}</div>
                                <div class="flex justify-content-between align-items-center">
                                    <h6 class="mt-0 font-light">{{ slotProps.data.collab_status }}</h6>
                                </div>
                            </div>
                        </template>
                    </Carousel>
                    <p v-else class="mx-auto">No collaborations yet</p>
                </div>
            </div>

            <hr />

            <div class="col-12">
                <div class="card">
                    <h5>Recommended for you</h5>
                    <Carousel :value="recommendationDetails" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" circular :autoplayInterval="5000">
                        <template #item="slotProps">
                            <div v-ripple class="p-ripple cursor-pointer border-1 surface-border border-round m-2 p-3" @click="clickUser(slotProps.data.user_id)">
                                <div class="mb-3">
                                    <div class="relative mx-auto">
                                        <img :src="'/src/assets/images/users/' + slotProps.data.user_photo" :alt="slotProps.data.user_id" class="w-full border-round" style="height: 250px; object-fit: cover" />
                                    </div>
                                </div>
                                <div class="mb-3 font-medium">{{ slotProps.data.full_name }}</div>
                                <div class="flex justify-content-between align-items-center">
                                    <Chip v-for="interest in slotProps.data.interests.split(',')" :label="interest" />
                                </div>
                            </div>
                        </template>
                    </Carousel>
                </div>
            </div>
        </div>
    </div>
</template>
