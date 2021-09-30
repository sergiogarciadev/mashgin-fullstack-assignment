import axios from 'axios'

export default {
  async addOrder (order) {
    const resp = await axios.post('/api/order', order)
    return resp.data
  },
}
