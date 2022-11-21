import axios from 'axios'
export default class TransactionsApi {

    static async getTransactions() {
        const transactions = await axios.get('http://localhost:8000/transactions')
        return transactions.data

    }

    static async deleteTransaction(id) {
        const transactionToDelete = await axios.put(`http://localhost:8000/transactions/${id}`)
    }

    static async addTransaction(vendor, amount, category_name) {
        const newTransaction = await axios.post('http://localhost:8000/transactions', {
            vendor,
            amount,
            category_name
        })
    }

    static async getBreakdowns() {
        const braekDowns = await axios.get('http://localhost:8000/transactions/breakdowns')
        return braekDowns.data
    }
}