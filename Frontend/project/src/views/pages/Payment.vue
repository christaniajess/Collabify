<script setup>
import { ref } from 'vue';

const paymentProcess = () => {
  fetch("http://172.28.182.145:3010/checkout-session", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      items: [
        { id: 1, quantity: 3 }
      ],
    }),
  })
    .then(res => { 
      if (res.ok) return res.json()
      return res.json().then(json => Promise.reject(json))
    })
    .then(({ url }) => {
        // console.log(url)
      window.location = url
    })
    .catch(e => {
      console.error(e.error)
    })
};

</script>

<template>
    <div class="grid">
        <div class="col-12 md:col-6">
            <div class="card">
                <h5>Default</h5>
                <Button label="Payment" class="mr-2 mb-2" @click="paymentProcess"></Button>
            </div>
        </div>
    </div>
</template>
