import axios from 'axios'
import { CATEGORY_API } from '../utils/consts'

export default class TransactionsApi {

    static async getCategories() {
        const categories = await axios.get(CATEGORY_API)
        return categories.data
    }
}