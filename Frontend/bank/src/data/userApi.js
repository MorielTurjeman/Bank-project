import axios from 'axios'

export default class UserApi {

    static async getBalance() {
        const balance = await axios.get(`http://localhost:8000/balance/1`)
        return balance.data.current_balance
    }

}