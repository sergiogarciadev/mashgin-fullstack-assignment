import axios from 'axios'

export default {
  async getItems () {
    const resp = await axios.get('/api/item')
    return resp.data
  },
}
