import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import AddToCart from '../components/AddToCart.vue';
import Cart from '../components/Cart.vue';
import CategoryList from '../components/CategoryList.vue';
import CategoryItemList from '../components/CategoryItemList.vue';
import Checkout from '../components/Checkout.vue';
import Success from '../components/Success.vue';

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/categories',
      name: 'Categories',
      component: CategoryList
    },
    {
      path: '/category/:id(\\d+)',
      name: 'Category',
      component: CategoryItemList
    },
    {
      path: '/addToCart/:id(\\d+)',
      name: 'AddToCart',
      component: AddToCart
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    },
    {
      path: '/checkout',
      name: 'Checkout',
      component: Checkout
    },
    {
      path: '/success',
      name: 'Success',
      component: Success
    },
  ],
});
