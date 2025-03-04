import './assets/main.css'

import { createApp } from 'vue'
import ElementUI from 'element-ui'
import App from './App.vue'
import router from './router'
Vue.use(ElementUI)
const app = createApp(App)

app.use(router)
app.mount('#app')
