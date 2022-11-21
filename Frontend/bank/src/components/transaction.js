
import TableCell from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import TransactionsApi from '../data/transactionsApi';
import { Chip } from '@mui/material';


function Transaction(props) {



    const { row } = props
    return (<TableRow
        key={row.name}
        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
    >
        <TableCell component="th" scope="row">
            {row.amount < 0 ?
                <Chip color='error' label="Withdraw"></Chip> :
                <Chip color="success" label="Deposit"></Chip>}
        </TableCell>
        <TableCell align="right">{row.vendor}</TableCell>
        <TableCell align="right">{row.amount}</TableCell>
        <TableCell align="right">{row.category_name}</TableCell>
        <TableCell align="right"><Button variant="outlined" onClick={() => props.deleteTransaction(row.id)} startIcon={<DeleteIcon />}>
            Delete
        </Button></TableCell>
    </TableRow>)
}

export default Transaction;