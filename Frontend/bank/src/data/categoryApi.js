import axios from 'axios'

export default class TransactionsApi {

    static async getCategories() {
        const categories = await axios.get('http://localhost:8000/categories')
        return categories.data
    }
}