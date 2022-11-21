import { Chip } from "@mui/material";

export default function StatusChip(props) {

    return (
        props.isStatusGreen ?
            <Chip color='success' label={props.greenLabel}></Chip> :
            <Chip color="error" label={props.redLabel}></Chip>

    );
}

