<template>
  <div
    class="relative z-0 overflow-hidden text-2xl font-bold transition-transform rounded shadow-lg cursor-pointer hover:transform hover:scale-110 hover:z-10"
    @click="goToCategory"
  >
    <img class="object-cover w-full h-96 hover:filter hover:grayscale" :src="imagePath" :alt="category.name" />
    <div class="absolute bottom-0 w-full pt-2 text-center bg-white bg-opacity-70">
      <div class="mb-2">{{ category.name }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['category'],
  computed: {
    imagePath() {
      return `/images/${this.category.image_id}.jpg`;
    },
  },
  methods: {
    goToCategory() {
      this.$router.push(`/category/${this.category.id}`)
    }
  }
};
</script>
