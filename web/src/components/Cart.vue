<template>
  <div class="w-1/2 mx-auto">
    <CartItem v-for="item in items" :item="item" :key="item.id" />
    <div class="relative h-10 py-2 mx-auto mt-2 text-2xl font-bold">
      <div class="absolute top-0 left-2">Total Due</div>
      <div class="absolute top-0 right-2">{{ total }}</div>
    </div>
    <button class="w-full py-2 mt-2 text-white bg-blue-600" @click="continueShopping">Continue Shopping</button>
    <button class="w-full py-2 mt-2 text-white bg-blue-800" @click="checkout">Checkout</button>
  </div>
</template>

<script>
import CartItem from './CartItem.vue';
import { sumBy } from 'lodash';

export default {
  created() {
    if (this.items.length == 0) {
      this.$router.push('/');
    }
  },
  data() {
    const cartItemKeys = Object.keys(this.$store.state.cart.items).map((i) => parseInt(i, 10));
    const cartItems = this.$store.state.items.all.filter((i) => cartItemKeys.indexOf(i.id) >= 0);

    return {
      items: cartItems,
    };
  },
  computed: {
    total() {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(
        sumBy(this.items, (i) => i.price * this.$store.state.cart.items[i.id])
      );
    },
  },
  methods: {
    continueShopping() {
      this.$router.push('/');
    },
    async checkout() {
      this.$router.push('/checkout');
    },
  },
  components: {
    CartItem,
  },
};
</script>
