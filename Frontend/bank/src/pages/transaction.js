
import TableCell from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';


function Transaction(props) {
    const { row } = props
    return (<TableRow
        key={row.name}
        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
    >
        <TableCell component="th" scope="row">
            {row.name}
        </TableCell>
        <TableCell align="right">{row.Vendor}</TableCell>
        <TableCell align="right">{row.Amount}</TableCell>
        <TableCell align="right">{row.Category}</TableCell>
        <TableCell align="right"><Button variant="outlined" startIcon={<DeleteIcon />}>
            Delete
        </Button></TableCell>
    </TableRow>)
}

export default Transaction;