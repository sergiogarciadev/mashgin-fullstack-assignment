<template>
  <div class="text-4xl text-center pt-10">Thank you for your order.</div>
</template>

<script>
export default {
  created() {
    this.$store.dispatch('cart/newCart')
  },
};
</script>
