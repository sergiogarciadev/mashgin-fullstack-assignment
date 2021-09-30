import { createApp } from 'vue';

import VueCreditCardValidation from 'vue-credit-card-validation';

import routes from './routes';
import store from './store';

import './styles/global.css';

import App from "./components/App.vue"

const app = createApp(App);

app.use(routes);
app.use(store);
app.use(VueCreditCardValidation);

app.mount('body');
