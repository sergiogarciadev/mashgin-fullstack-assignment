<template>
  <div class="w-1/2 mx-auto">
    <CheckoutItem v-for="item in items" :item="item" :key="item.id" />

    <div class="relative h-10 py-2 mx-auto mt-2 text-2xl font-bold">
      <div class="absolute top-0 left-2">Total Due</div>
      <div class="absolute top-0 right-2">{{ total }}</div>
    </div>

    <div class="w-full">
      <label for="payment" class="block text-sm mb-2">Credit Card</label>
      <div class="flex">
        <input
          ref="cardNumberInput"
          v-model="cardNumber"
          type="text"
          class="w-5/6 flex-1 text-sm bg-grey-light text-grey-darkest rounded-l p-3 focus:outline-none"
          placeholder="Card Number"
          v-cardformat:formatCardNumber
        />
        <input
          ref="cardExpiryInput"
          v-model="cardExpiry"
          type="text"
          class="w-1/6 inline-block text-sm bg-grey-light text-grey-darkest p-3 focus:outline-none"
          placeholder="MM / YY"
          v-cardformat:formatCardExpiry
        />
        <input
          ref="cardCvcInput"
          v-model="cardCvc"
          type="text"
          class="w-1/6 inline-block text-sm bg-grey-light text-grey-darkest rounded-r p-3 focus:outline-none"
          placeholder="CVC"
          v-cardformat:formatCardCVC
        />
      </div>
    </div>

    <button class="w-full py-2 mt-2 text-white " :class="isValid ? 'bg-blue-800' : 'bg-blue-400'" :disabled='!isValid' @click="checkout">Place Order</button>
  </div>
</template>

<script>
import CheckoutItem from './CheckoutItem.vue';
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
      cardNumber: '',
      cardExpiry: '',
      cardCvc: '',

      items: cartItems,
    };
  },
  computed: {
    isValid() {
      return this.$cardFormat.validateCardNumber(this.cardNumber) &&
          this.$cardFormat.validateCardExpiry(this.cardExpiry) &&
          this.cardCvc.length >= 3;
    },
    total() {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(
        sumBy(this.items, (i) => i.price * this.$store.state.cart.items[i.id])
      );
    },
  },
  methods: {
    async checkout() {
      await this.$store.dispatch('cart/checkout', {
        card: {
          cardNumber: this.cardNumber,
          cardExpiry: this.cardExpiry,
          cardCvc: this.cardCvc,
        },
        cartItems: this.items,
      });
      this.$router.push('/success');
    },
  },
  watch: {
    cardNumber: function (val) {
      if (this.$cardFormat.validateCardNumber(val)) {
        this.$refs.cardExpiryInput.focus();
      }
    },
    cardExpiry: function (val) {
      if (this.$cardFormat.validateCardExpiry(val)) {
        this.$refs.cardCvcInput.focus();
      }
    },
  },
  components: {
    CheckoutItem,
  },
};
</script>
