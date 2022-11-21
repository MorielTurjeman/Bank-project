import axios from 'axios'
import { BALANCE_URL } from '../utils/consts'

export default class UserApi {

    static async getBalance() {
        const balance = await axios.get(BALANCE_URL)
        return balance.data.current_balance
    }

}