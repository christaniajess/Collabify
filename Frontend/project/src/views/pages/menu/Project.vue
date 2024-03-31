<script setup>
import { ref, onMounted } from 'vue';

const products = ref([]);
const images = ref([]);
const carouselResponsiveOptions = ref([
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


onMounted(() => {

});
</script>

<template>
    <div class="grid p-fluid">
        <div class="col-12">
            <div class="card">
                <h5>Carousel</h5>
                <Carousel :value="products" :numVisible="3" :numScroll="3" :circular="false" :responsiveOptions="carouselResponsiveOptions">
                    <template #item="product">
                        <div class="border-round m-2 text-center p-2" style="border: 1px solid var(--surface-d)">
                            <div class="my-5">
                                <img :src="'demo/images/product/' + product.data.image" :alt="product.data.name" class="product-image" />
                            </div>
                            <div>
                                <h5 class="mb-1">
                                    name
                                </h5>
                                <h6 class="mt-0 mb-3">hello</h6>
                                <Badge :class="'product-badge status-' + product.data.inventoryStatus.toLowerCase()">status</Badge>
                                <div class="my-5">
                                    <Button icon="pi pi-search" class="mr-2 p-button-rounded"></Button>
                                    <Button icon="pi pi-star-fill" class="mr-2 p-button-rounded p-button-success"></Button>
                                    <Button icon="pi pi-cog" class="p-button-rounded p-button-info"></Button>
                                </div>
                            </div>
                        </div>
                    </template>
                </Carousel>
            </div>
        </div>
    </div>
</template>
