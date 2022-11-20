import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import { Link } from 'react-router-dom';
import LinkButton from './LinkButton';



const pages = ['Transactions', 'Operations', 'Breakdowns'];


export default function NavBar() {
    const [anchorElNav, setAnchorElNav] = React.useState(null);
    const [anchorElUser, setAnchorElUser] = React.useState(null);

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
                            Balance:
                        </Typography>
                    </Box>
                </Toolbar>
            </Container>
        </AppBar>
    );
}





