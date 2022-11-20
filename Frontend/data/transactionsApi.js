

class TransactionApi {

    static async getTransactions(params) {
        const transactions = await axios.get('http://localhost:3000/Transactions')
        return transactions
    }
}