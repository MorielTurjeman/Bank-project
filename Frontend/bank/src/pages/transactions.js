
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Transaction from './transaction';
import React, { useState, useEffect } from 'react';
import TransactionsApi from '../data/transactionsApi'



function createData(Vendor, Amount, Category) {
    return { Vendor, Amount, Category };
}

const rows = [
    createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
    createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
    createData('Eclair', 262, 16.0, 24, 6.0),
    createData('Cupcake', 305, 3.7, 67, 4.3),
    createData('Gingerbread', 356, 16.0, 49, 3.9),
];

function Transactions() {
    useEffect(() => {
        TransactionsApi.getTransactions().then(transactions => console.log(transactions))
    })

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell align="right">Date</TableCell>
                        <TableCell align="right">Vendor</TableCell>
                        <TableCell align="right">Amount</TableCell>
                        <TableCell align="right">Category</TableCell>
                        <TableCell align="right"></TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {row.map((row) => <Transaction row={row} />)}
                </TableBody>
            </Table>
        </TableContainer >
    );
}
export default Transactions;