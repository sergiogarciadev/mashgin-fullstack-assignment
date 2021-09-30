import api from '../../api/items'

// initial state
const state = {
  all: []
}

// getters
const getters = {}

// actions
const actions = {
  async getAll ({ commit }) {
    const items = await api.getItems()
    commit('setItems', items)
  }
}

// mutations
const mutations = {
  setItems (state, items) {
    state.all = items
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
