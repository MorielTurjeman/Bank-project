
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Transaction from '../components/transaction';
import React, { useState, useEffect } from 'react';
import TransactionsApi from '../data/transactionsApi'

function Transactions(props) {
    const [transactions, setTransactions] = useState([])
    const [shouldReload, setShouldReload] = useState(true)

    const getTransactions = () => {
        if (shouldReload) {
            TransactionsApi.getTransactions()
                .then(transactions => setTransactions(transactions))
                .then(() => setShouldReload(false))
                .catch((err) => {
                    console.error(err)
                })
        }


    }
    useEffect(() => { getTransactions() }, [shouldReload])

    const deleteTransaction = (id) => { TransactionsApi.deleteTransaction(id).then(() => setShouldReload(true)).then(() => props.setShouldReloadBalance(true)) }

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell align="right">Type</TableCell>
                        <TableCell align="right">Vendor</TableCell>
                        <TableCell align="right">Amount ₪</TableCell>
                        <TableCell align="right">Category </TableCell>
                        <TableCell align="right"></TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {transactions.map((row) => <Transaction key={row.id} row={row} deleteTransaction={deleteTransaction} />)}
                </TableBody>
            </Table>
        </TableContainer >
    );
}
export default Transactions;