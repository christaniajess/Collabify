<script setup>
import { ref, onMounted } from 'vue';

import { Ports, MicroService } from '@/service/Constant.js';
import { useRouter } from 'vue-router';
const router = useRouter();
const brand_id = ref();
const cc_id = ref();

const paymentProcess = () => {
    fetch(MicroService['service'] + Ports['complex_update_collab'] + '/update_request', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            brand_id: brand_id.value,
            cc_id: cc_id.value,
            collab_status: 'Completed'
        })
    })
        .then((res) => {
            if (res.ok) return res.json();
            return res.json().then((json) => Promise.reject(json));
        })
        .then(() => {
            // console.log(url)
            router.push('/Collab');
        })
        .catch((e) => {
            console.error(e.error);
        });
};

let urlParams = ref(null);

onMounted(async () => {
    const url = new URL(window.location.href);
    urlParams.value = Object.fromEntries(url.searchParams.entries());
    console.log(urlParams.value);
    brand_id.value = urlParams.value['brand_id'];
    cc_id.value = urlParams.value['cc_id'];
    await paymentProcess();
});
</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-6">
            <div class="card">
                <h5>Default</h5>
                <!-- <Button label="Payment" class="mr-2 mb-2" @click="paymentProcess('adi', 10000)"></Button> -->
            </div>
        </div>
    </div>
</template>
