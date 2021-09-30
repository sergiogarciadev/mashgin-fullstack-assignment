import api from '../../api/categories'

// initial state
const state = {
  all: []
}

// getters
const getters = {}

// actions
const actions = {
  async getAll ({ commit }) {
    const categories = await api.getCategories()
    commit('setCategories', categories)
  }
}

// mutations
const mutations = {
  setCategories (state, categories) {
    state.all = categories
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
