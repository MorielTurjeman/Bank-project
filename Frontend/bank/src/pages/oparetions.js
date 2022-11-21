
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import CategoryApi from '../data/categoryApi';
import React, { useState, useEffect } from 'react';
import DropDown from '../components/dropDown';
import TransactionsApi from '../data/transactionsApi';
import { isNegative, isNotNumber, isStringEmpty } from '../utils/validations';

export const DEPOSIT = 1
export const WITHDRAW = -1

function Oparetions() {
    const [categories, setCategories] = useState([])
    const [selectedCategory, setSelectedCategory] = useState('')
    const [amount, setAmount] = useState(0)
    const [vendor, setVendor] = useState("")

    const isVendorInvalid = isStringEmpty(vendor)
    const isAmountInvalid = isNotNumber(amount) || isNegative(amount)
    const isCategoryInvalid = isStringEmpty(selectedCategory)

    const buttonsDisabled = isVendorInvalid || isAmountInvalid || isCategoryInvalid

    useEffect(() => {
        CategoryApi.getCategories().then(categories => setCategories(categories)).catch((err) => {
            console.error(err)
        })
    }, [])

    const addTransaction = (transactionType) => {

        TransactionsApi.addTransaction(vendor, amount * transactionType, selectedCategory).then(() => {
            setVendor("")
            setAmount(0)
            setSelectedCategory('')
        })
    }

    return (
        <Card sx={{ maxWidth: 345, justifyContent: 'center' }}>
            <CardHeader title="Insert Transaction">
            </CardHeader>
            <CardContent>
                <Box
                    component="form"
                    sx={{
                        '& .MuiTextField-root': { m: 1, width: '25ch' },
                    }}
                    noValidate
                    autoComplete="off"
                >
                    <div>
                        <TextField
                            fullWidth
                            label="Transaction Vendor"
                            id="fullWidth"
                            onChange={e => setVendor(e.target.value)}
                            value={vendor}
                            required
                            helperText="Enter vendor name"

                        />
                    </div>
                    <div>
                        <TextField
                            id="outlined-basic"
                            label="Transaction Amount"
                            variant="outlined"
                            onChange={e => setAmount(e.target.value)}
                            value={amount}
                            helperText="Enter a positive number"
                        />
                    </div>
                    <div>
                        <DropDown
                            selectedItem={selectedCategory}
                            setSelectedItem={setSelectedCategory}
                            items={categories} label="categories"
                            helperText="must select category"
                        />
                    </div>
                    <Button variant="contained" color="success" onClick={() => addTransaction(DEPOSIT)} disabled={buttonsDisabled} >
                        Deposit
                    </Button>
                    <Button variant="contained" color="error" onClick={() => addTransaction(WITHDRAW)} disabled={buttonsDisabled}>
                        Withdraw
                    </Button>
                </Box>
            </CardContent>
        </Card>



    );
}

export default Oparetions;