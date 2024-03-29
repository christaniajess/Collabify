<script setup>
import { ref } from 'vue';

const paymentProcess = (collab, amount) => {
    fetch('http://localhost:5000/checkout-session', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            items: [
                {
                    collab_title: collab,
                    amount: amount,
                    quantity: 1
                }
            ]
        })
    })
        .then((res) => {
            if (res.ok) return res.json();
            return res.json().then((json) => Promise.reject(json));
        })
        .then(({ url }) => {
            // console.log(url)
            window.location = url;
        })
        .catch((e) => {
            console.error(e.error);
        });
};



</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-6">
            <div class="card">
                <h5>Default</h5>
                <Button label="Payment" class="mr-2 mb-2" @click="paymentProcess('adi', 10000)"></Button>
            </div>
        </div>
    </div>
</template>
