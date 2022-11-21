import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import LinkButton from './LinkButton';
import StatusChip from './statusChip';


const pages = ['Transactions', 'Operations', 'Breakdowns'];



export default function NavBar(props) {
    const [anchorElNav, setAnchorElNav] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };


    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    return (
        <AppBar position="static">
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}>
                        <LinkButton to={"Transactions"} onClick={handleOpenNavMenu} />
                        <LinkButton to={"Oparetions"} onClick={handleOpenNavMenu} />
                        <LinkButton to={"Breakdowns"} onClick={handleOpenNavMenu} />
                        {/* {pages.map((page) => (
                            <LinkButton target={page} 
                        ))} */}
                    </Box>
                    <Box sx={{ flexGrow: 0 }}>
                        <Typography size>
                            Balance: <StatusChip isStatusGreen={props.balance > 0} greenLabel={props.balance} redLabel={props.balance} />
                        </Typography>
                    </Box>
                </Toolbar>
            </Container>
        </AppBar>
    );
}





