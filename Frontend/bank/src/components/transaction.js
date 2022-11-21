
import TableCell from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import StatusChip from './statusChip';


function Transaction(props) {

    const { row } = props
    return (<TableRow
        key={row.name}
        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
    >
        <TableCell align="right">
            <StatusChip isStatusGreen={props.row.amount < 0} greenLabel={"Withdraw"} redLabel={"Deposit"} />
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