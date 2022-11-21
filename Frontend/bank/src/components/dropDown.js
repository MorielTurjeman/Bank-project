import TextField from '@mui/material/TextField';
import MenuItem from "@mui/material/MenuItem";

export default function dropDown(props) {
    return (<TextField
        id="outlined-select-currency"
        select
        label={props.label}
        value={props.selectedItem}
        onChange={e => props.setSelectedItem(e.target.value)}
        error={props.error}
    >
        {props.items.map((option) => (
            <MenuItem key={option.name} value={option.name}>
                {option.name}
            </MenuItem>
        ))}
    </TextField>)
}