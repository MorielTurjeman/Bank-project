import axios from 'axios'
import { TRANSACTION_API } from '../utils/consts'
export default class TransactionsApi {

    static async getTransactions() {
        const transactions = await axios.get(TRANSACTION_API)
        return transactions.data

    }

    static async deleteTransaction(id) {
        const transactionToDelete = await axios.put(`${TRANSACTION_API}/${id}`)
    }

    static async addTransaction(vendor, amount, category_name) {
        const newTransaction = await axios.post(TRANSACTION_API, {
            vendor,
            amount,
            category_name
        })
    }

    static async getBreakdowns() {
        const braekDowns = await axios.get(`${TRANSACTION_API}/breakdowns`)
        return braekDowns.data
    }

}