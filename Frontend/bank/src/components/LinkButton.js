import { Button } from "@mui/material";
import { Link } from "react-router-dom";

function LinkButton(props) {
    return <Link to={props.to}>
        <Button
            key={props.to}
            onClick={props.onClick}
            sx={{ my: 2, color: 'white', display: 'block' }}>
            {props.to}
        </Button>
    </Link>;
}

export default LinkButton;