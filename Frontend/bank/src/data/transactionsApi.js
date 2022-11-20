import axios from 'axios'
export class TransactionsApi {

    static async getTransactions(params) {
        const transactions = await axios.get('http://localhost:3000/Transactions')
        return transactions
    }
}