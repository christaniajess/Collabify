import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';

import Menubar from 'primevue/menubar';

import 'primevue/resources/themes/aura-light-green/theme.css'       //theme

const app = createApp(App)
app.use(PrimeVue)
app.component('Menubar', Menubar)
app.mount('#app')
  